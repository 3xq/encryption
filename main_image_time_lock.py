import random, math, time
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

def encrypt_to_image(string, password, file_name, lock_time = 0):
    encrypted = encrypt(string, password)
    
    encryption_iteration = 0
    time_lock_iteration = 0
    
    side_length = math.ceil(math.sqrt(len(encrypted)))
    time_lock = encrypt(str(time.time() + lock_time), 'time-lock')
    
    image = Image.new('RGB', (side_length, side_length + math.ceil(len(time_lock) / side_length)))
    pixels = image.load()

    random_colors = [(65, 18, 66), (68, 134, 69), (48, 50, 49), (77, 88, 78), (65, 74, 66), (47, 54, 48), (48, 76, 49), (74, 136, 75), (53, 96, 54), (52, 10, 53), (48, 90, 49), (72, 10, 73), (56, 68, 57), (52, 78, 53), (48, 94, 49), (73, 40, 74), (67, 0, 68), (52, 80, 53), (48, 88, 49), (76, 106, 77), (65, 34, 66), (68, 128, 69), (48, 32, 49), (72, 26, 73), (67, 94, 68), (51, 12, 52), (48, 96, 49), (75, 128, 76), (49, 94, 50), (68, 10, 69), (49, 82, 50), (76, 152, 77), (54, 34, 55), (53, 84, 54), (48, 6, 49), (75, 14, 76), (64, 90, 65), (47, 76, 48), (48, 82, 49), (74, 132, 75), (68, 40, 69), (48, 28, 49), (48, 98, 49), (73, 48, 74), (55, 104, 56), (67, 124, 68), (49, 50, 50), (72, 10, 73), (66, 94, 67), (52, 64, 53), (48, 62, 49), (73, 120, 74), (54, 56, 55), (49, 92, 50), (49, 52, 50), (72, 60, 73), (54, 58, 55), (52, 78, 53), (48, 22, 49), (72, 122, 73), (65, 100, 66), (68, 46, 69), (48, 86, 49), (71, 22, 72), (64, 26, 65), (51, 0, 52), (48, 44, 49), (78, 56, 79), (52, 78, 53), (52, 42, 53), (48, 76, 49), (70, 34, 71), (50, 74, 51), (65, 82, 66), (49, 68, 50), (71, 120, 72), (49, 2, 50), (52, 68, 53), (48, 32, 49), (82, 40, 83), (50, 38, 51), (49, 26, 50), (48, 96, 49)]

    for x in range(side_length):
        for y in range(side_length + math.ceil(len(time_lock) / side_length)):
            pixels[x, y] = random_colors[random.randint(0,len(random_colors)-1)]
    
    for x in range(side_length):
        for y in range(side_length):
            encryption_iteration = encryption_iteration + 1

            if encryption_iteration <= len(encrypted):
                character_code = ord(encrypted[encryption_iteration - 1])

                red = character_code - random.randint(0, character_code)
                blue = character_code - red
                
                pixels[x, y] = (blue + red, int(red * 2), blue + red)

    for x in range(side_length):
        for y in range(side_length, side_length + math.ceil(len(time_lock) / side_length)):
            time_lock_iteration = time_lock_iteration + 1
            
            if time_lock_iteration <= len(time_lock):
                character_code = ord(time_lock[time_lock_iteration - 1])
                
                red = character_code - random.randint(0, character_code)
                blue = character_code - red
                
                pixels[x, y] = (blue + red, int(red * 2), blue + red)

    image.save(file_name)
    
def decrypt_from_image(file_name, password):
    image = Image.open(file_name)
    pixels = image.load()

    side_length = image.size[0]
    characters = []

    time_lock = []

    for x in range(side_length):
        for y in range(side_length):
            pixel = pixels[x, y]

            if pixel[0] == pixel[2]:
                character = chr(int(pixel[0]))
                characters.append(character)

    for x in range(side_length):
        for y in range(side_length, image.size[1]):
            pixel = pixels[x, y]

            if pixel[0] == pixel[2]:
                character = chr(int(pixel[0]))
                time_lock.append(character)

    if float(decrypt(''.join(time_lock), 'time-lock')) > time.time():
        return decrypt(''.join(characters), password)
    else:
        return None
