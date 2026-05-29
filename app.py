import re
import math
# import 2 python built in libraries. re for REGEX, math for log2() in entropy formula.
from flask import Flask, render_template, request
# Flask - create web app, render_template - loads your HTML file, request - read what user typed in the form
app = Flask(__name__)
#create your web application
with open('10-million-password-list-top-1000.txt') as file : 
  common_password = file.read()

@app.route("/", methods = ["GET", "POST"])
#Tells Flask this function handles the home page /. 
def index(): 
 #This function runs every time someone visit that page. Flask calls it automatically
  result = None
  user_name = ""
#Default empty values. 
  if request.method == "POST" :
    user_name = request.form.get("user_name", "")
    user_password = request.form.get("user_password","")
#Reads what user typed in the form

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

    if charset_size == 0 :
      charset_size = 1

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
      missing.append("length must be between 6 and 60 characters ")
    if not has_digit : 
      missing.append("at least one digit (0-9)")
    if not has_special :
      missing.append("at least one special character like ! @ $ % . . . . etc. ")

    is_valid = has_upper and has_lower and has_digit and has_special and length_ok
    is_common = user_password in common_password

    result = {
      "is_valid"        : is_valid,
      "is_common"       : is_common,
      "score"           : score,
      "missing"         : missing,
      "entropy"         : round(entropy, 2),
      "entropy_label"   : entropy_label,
      "password_length" : len(user_password)
        }
      
  return render_template("index.html", result=result, user_name=user_name)

if __name__ == '__main__' :
  app.run(debug=True)
