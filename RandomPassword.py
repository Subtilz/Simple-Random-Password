from lib2to3.pygram import Symbols
import numbers
import random
import string 

lower = "abcdefghijklmnopqrstuvwxzy"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXZY"
numbers = "0123456789"
Symbols = "!@#$%^&*()."

string = lower + upper + numbers + Symbols
length = 10
password = "".join(random.sample(string,length))

print("Your new Password Is : " + password)