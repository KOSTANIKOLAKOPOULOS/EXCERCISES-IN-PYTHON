#INSPECTOR LEKAS
from sys import argv
 
script, sample = argv
print(f"we're going to erase {sample}.")
print("if you don't want that, hit CTRL-C (^C).")
print("IF YOU DO want that, hit RETURN.")
input("?")
print("opening the file ...")
target = open(sample, 'w')
print("truncating the file. goodbye !")
target.truncate()
print("now i'm going to ask you for three lines.")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("i'm going to write to the file .")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("and finally , we close it .")
target.close()