import random

print("Hello World")


# range of values for lowercase: 97-122
# range of values for uppercase: 65-90
def gen_first_name(length):
  name = ""
  print(length)
  for letter in range(length):
    name += char(random.randrange(97,122))
  return name



#def create_user_hash(f_name, l_name):

print(gen_first_name(random.randrange(20)))
