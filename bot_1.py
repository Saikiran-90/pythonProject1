#st =  "aRTificial INTELLIgence"
print("Enter a String !.")
str_name = input(" ")
print( "1.Convert the input string into upper case.")
print("2.Convert the input string into lower case.")
print("3.Check whether all the characters of the input string are in upper case.")
print("4.Check whether all the characters of the input string are in lower case.")
print("5.Replace the string INTELLIgence by “Neural Network.")
print("6.Check whether the given string starts with “T”.")
print("7.Check whether the given string ends with “e”.")
print("8.Convert the first letter of the input string into capital letter.")
print("9.	Convert the lower-case characters to upper case and vice versa")
print("10.Exit ")

num = int(input("Enter any Option!."))
if num == 1:
    print(str_name.upper())
elif num == 2:
    print(str_name.lower())
elif num == 3:
    print(str_name.isupper())
elif num == 4:
    print(str_name.islower())
elif num == 5:
    print(str_name.replace("INTELLIgence", "Neural Network"))
elif num == 6:
    print(str_name.startswith("T"))
elif num == 7:
    print(str_name.endswith("e"))
elif num == 8:
    print(str_name.capitalize())
elif num == 9:
    print(str.swapcase("aRTificial INTELLIgence"))
elif num == 10:
    print(exit())

