# "What have the Romans ever done for us?"

import random, hashlib

us_states = ["Alabama", "Alaska", "Arizona", "Arkansas", "American Samoa", "California", "Colorado", "Connecticut", "Delaware", 
             "District of Columbia", "Florida", "Georgia", "Guam", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas",
             "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri",
            "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", 
            "Northern Mariana Islands", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina",
            "South Dakota", "Tennessee", "Texas", "Trust Territories", "Utah", "Vermont", "Virginia", "Virgin Islands", 
             "Washington", "West Virginia", "Wisconsin", "Wyoming"]

# us_state_codes = ["AL",	"KY", "OH", "AK", "LA",	"OK", "AZ",	"ME", "OR", "AR", "MD", "PA", "AS",	"MA", "PR", "CA", "MI", "RI", "CO		MN		SC
# 	              CT		MS		SD
# 	              DE		MO		TN
# 	              DC		MT		TX
# 	              FL		NE		TT
# 	              GA		NV		UT
# 	              GU		NH		VT
# 	              HI		NJ		VA
# 	              ID		NM		VI
# 	              IL		NY		WA
# 	              IN		NC		WV
# 	              IA		ND		WI
# 	              KS		MP		WY]


# range of values for lowercase: 97-122
# range of values for uppercase: 65-90
def gen_first_name(length):
  name = ""
  name += chr(random.randrange(65,90))
  for letter in range(length-1):
    name += chr(random.randrange(97,122))
  return name

def gen_last_name(length):
  return gen_first_name(length)

def gen_user_hash_md5(f_name, l_name):
  to_hash = f_name+l_name
  hash = hashlib.md5(to_hash.encode())
  return hash

def gen_user_hash_sha256(f_name, l_name):
  to_hash = f_name+l_name
  hash = hashlib.sha256(to_hash.encode())
  return hash

def gen_user_hash_sha512(f_name, l_name):
  to_hash = f_name+l_name
  hash = hashlib.sha512(to_hash.encode())
  return hash


# print(gen_hash(gen_first_name(5), gen_last_name(5))
first_name = gen_first_name(random.randrange(3,10))
last_name = gen_last_name(random.randrange(4,10))

# Weak hash, MD5
hash_md5 = gen_user_hash_md5(first_name, last_name)

# Stronger hash, SHA256
hash_sha256 = gen_user_hash_sha256(first_name, last_name)

# Even Stronger hash but potential performance issues, SHA512
hash_sha512 = gen_user_hash_sha512(first_name, last_name)

print("First Name: ")
print(first_name)
print()

print("Last Name: ")
print(last_name)
print()

print("MD5 Hash : ")
print(hash_md5.hexdigest())
print()

print("SHA256 Hash: ")
print(hash_sha256.hexdigest())
print()

print("SHA512 Hash: ")
print(hash_sha512.hexdigest())
print()

print("US States: ")
print(us_states)
