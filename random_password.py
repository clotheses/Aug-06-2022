import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "1234567890"
symbol = "!@#$%^&*()_+:;"

string = lower + upper + number + symbol
length = 20

password = "".join(random.sample(string,length))

name = input("Your name: ")

print("Hey " + name + ", Your password is: " + password)