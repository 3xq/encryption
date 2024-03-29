import random, math
from PIL import Image

def fixed_length_password(length, point):
    return length % point

def generate_characters_from_password(password, length):
    fixed = []

    for character in list( (password * length)[:length] ):
        session_seed = ord(character) * 678
        random_session = random.Random(session_seed)
        random_number = random_session.randint(457, 875)
        character = chr(random_number)

        fixed.append(character)

    return fixed

def encrypt(string, password):
    characters = []
    generated_characters = generate_characters_from_password(password, 8)

    for _ in range(len(string)):
        string_character_ascii = ord( list(string)[_] )
        password_character_ascii = ord( password[ fixed_length_password( _ + 1, len(password) ) - 1 ] )
        reversed_character_ascii = ord(password[::-1][0])

        characters.append(chr(
            string_character_ascii + 
            password_character_ascii +
            reversed_character_ascii
        ))

    characters = list(''.join(
        '%s%s' % (character, (random.choice(generated_characters) if random.random() > 0.5 else ''))
        for character in ''.join(characters)))

    character_hexes = []
    scrambled_hexes = []
    filler_characters = list('ghijklmno')
    split_characters = list('pqrstuv')

    for character in characters:
        hex_code = str(hex(ord(character)))
        hex_code = hex_code.split('0x')[1]

        character_hexes.append(hex_code)

    for character_hex in character_hexes:
        filled_hex = character_hex + random.choice(filler_characters)
        scrambled_hexes.append(filled_hex)

    scrambled_hexes = ''.join(scrambled_hexes)[:-1]

    return scrambled_hexes.upper()[::-1] + random.choice(split_characters).upper() + str(random.randint(137, 975))

def decrypt(string, password):
    encrypted = string[:-4].lower()[::-1]
    generated_characters = generate_characters_from_password(password, 8)

    for character in list('ghijklmno'):
        encrypted = encrypted.replace(character, '#')

    scrambled_hexes = encrypted.split('#')
    characters = []
    non_generated_characters = []

    decrypted = []

    for i in scrambled_hexes:
        hex_code = eval('0x' + i)
        character = chr(hex_code)

        characters.append(character)

    for character in characters:
        if character not in generated_characters:
            non_generated_characters.append(character)

    for _ in range(len(non_generated_characters)):
        string_character_ascii = ord( list(non_generated_characters)[_] )
        password_character_ascii = ord( password[fixed_length_password( _ + 1, len(password)) - 1] )
        reversed_character_ascii = ord( password[::-1][0] )

        decrypted.append(chr(
            string_character_ascii -
            password_character_ascii -
            reversed_character_ascii
        ))

    return ''.join(decrypted)

def encrypt_to_image(string, password, file_name):
    encrypted = encrypt(string, password)
    
    characters = list(encrypted)
    iteration = 0
    
    side_length = math.ceil(math.sqrt(len(encrypted)))
    
    image = Image.new('RGB', (side_length, side_length))
    pixels = image.load()

    for x in range(side_length):
        for y in range(side_length):
            iteration = iteration + 1

            if iteration <= len(characters):
                character_code = ord(characters[iteration-1])

                red = character_code - random.randint(0, character_code)
                blue = character_code - red
                
                pixels[x, y] = (blue + red, int(red*2), blue + red)

    image.save(file_name)

def decrypt_from_image(file_name, password):
    image = Image.open(file_name)
    pixels = image.load()

    side_length = image.size[1]
    characters = []

    for x in range(side_length):
        for y in range(side_length):
            pixel = pixels[x, y]

            if pixel[0] != 0:
                character = chr(int(pixel[0]))
                characters.append(character)

    return decrypt(''.join(characters), password)
