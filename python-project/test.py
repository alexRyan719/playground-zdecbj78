import random, hashlib

print("Hello World")


# range of values for lowercase: 97-122
# range of values for uppercase: 65-90
def gen_first_name(length):
  name = ""
  print(length)
  for letter in range(length):
    name += chr(random.randrange(97,122))
  return name

def gen_last_name(length):
  return gen_first_name(length)

def gen_user_hash(f_name, l_name):
  to_hash = f_name+l_name
  hash = str(hashlib.md5(to_hash.encode()))
  return hash


# print(gen_hash(gen_first_name(5), gen_last_name(5))
first_name = gen_first_name(random.randrange(10))
last_name = gen_last_name(random.randrange(10))
hash = gen_user_hash(first_name, last_name)

print("First Name: ")
print(first_name)

print("Last Name: ")
print(last_name)

print("Hash: ")
print(hash)
