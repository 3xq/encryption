# encryption
a simple encryption algorithm coded in python.

 generating the same thing with the same password
 will result in different responses each time that
 will decode to the same thing.

# usage

main.py > encrypt(string, password):
  input: hello, world
  output 1: FE1N731KFE1IC31G3B2G241MFE1O831O341V393
  output 2: D02L731GFE1NC31K241KD02K831M341V535

  same arguments will yield different reponses 
  if generated more than once as said before.

main.py > decrypt(string, password):
  input: FE1N731KFE1IC31G3B2G241MFE1O831O341V393, world
  output: hello
  
  input: D02L731GFE1NC31K241KD02K831M341V535, world
  output: hello
  
  if the wrong password is entered it will output
  a random heap of characters depending on how long
  your encryption string was.
  
  input: FE1N731KFE1IC31G3B2G241MFE1O831O341V393, **wrodl**
  output: `Zgl_

# happy encrypting :^)
