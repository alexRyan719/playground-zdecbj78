import random

print("Hello World")

def gen_first_name(length):
  name = ""
  for letter in range(length):
    name += 'a'
  return name



#def create_user_hash(f_name, l_name):

print(gen_first_name(randrange(5)))
