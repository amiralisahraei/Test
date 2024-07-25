import re


my_text = "Hello, https my name is amirali, http I am from Iran. I am 26 years old. My height is 183 cms. a.sahraei98@gmail.com"

pattern = "I am [""] [a-zA-Z0-9]+"
pattern2 = "\d+"
pattern3 = "^Hello"
pattern4 = "cms$"
pattern5 = "Hello,.*name"
pattern6 = "m.+ I"
pattern7 = "http[s]* .+"
pattern8 = "http[s]+ .+"
email_pattern = "[.a-zA-Z0-9]+@[a-zA-Z]+.[a-zA-Z]+"

result = re.findall(email_pattern, my_text)
print(result)