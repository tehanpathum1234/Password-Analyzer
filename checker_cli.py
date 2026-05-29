import re
import math
with open('10-million-password-list-top-1000.txt') as file : 
  common_password = file.read()
user_name  = input("Enter your name : ")
print()
user_password = input(f"Enter your Password : ")
score = 0
charset_size = 0
has_upper = False
has_lower = False
has_digit = False
has_special = False
length_ok = False
special_chars = "!@#$%^&*()_+-=[]{};:'\"\\|,.<>/?"
if 6 <= len(user_password) <= 60 :
  length_ok = True
for ch in user_password :
  if ch.isupper() :
    has_upper = True
  elif ch.islower() : 
    has_lower = True
  elif ch.isdigit() :
    has_digit = True
  elif ch in special_chars : 
    has_special = True
if has_upper :
  charset_size += 26
if has_lower :
  charset_size += 26
if has_digit :
  charset_size += 10
if has_special :
  charset_size += len(special_chars)
entropy = len(user_password) * math.log2(charset_size)
if entropy < 28 :
  entropy_label = "Very Weak"
elif entropy < 36 :
  entropy_label = "Weak"
elif entropy < 60 :
  entropy_label = "Reasonable"
elif entropy < 128 :
  entropy_label = "Strong"
else :
  entropy_label = "Very Strong"
if has_upper :
  score = score + 1
if has_lower : 
  score = score + 1
if has_digit :
  score = score + 1
if has_special :
  score = score + 1
if length_ok : 
  score = score + 1
missing = []
if not has_upper :
  missing.append("at least one uppercase letter (A-Z) ")
if not has_lower : 
  missing.append("at least one lowecase letter (a-z) ")
if not length_ok : 
  missing.append("length must be between 8 and 12 characters ")
if not has_digit : 
  missing.append("at least one digit (0-9)")
if not has_special :
  missing.append("at least one special character like ! @ $ % . . . . etc. ")
if has_upper and has_lower and has_digit and has_special and length_ok : 
  print("Password is valid  :) ")
  print()
  if user_password in common_password :
    print("Your password use many users (Common Password). ")
  print()
  print(f"Score : {score} ")
  if score >= 0 and score <= 1 :
    print("Password is Weak (Based on Score)")
  elif score >= 2 and score <= 4 :
    print("Password is Fair (Based on Score)")
  elif score >4 and score <= 5 :
    print("Password is Strong (Based on Score)")
  print()
  print("Entropy Calculation : ")
  print(f"Password length: {len(user_password)} characters")
  print(f"Entropy : {entropy:.2f} bits")
  print(f"Strength : {entropy_label} ")
  print()
else :
  print("Your password is easy to break :( ")
  print()
  for req in missing :
    print(f"- {req}")
