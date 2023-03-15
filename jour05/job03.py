def string_length(s):
    if s == "":
        return 0
    else:
        return 1 + string_length(s[1:])

input_string = input("Enter a string: ")
result = string_length(input_string)
print("The length of the string is:", result)
