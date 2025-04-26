def to_lowercase(s):
    result = ""
    for char in s:
        if 'A' <= char <= 'Z':  
            result += chr(ord(char) + 32) 
        else:
            result += char  
    return result

def to_uppercase(s):
    result = ""
    for char in s:
        if 'a' <= char <= 'z': 
            result += chr(ord(char) - 32) 
        else:
            result += char  
    return result

def toggle_case(s):
    result = ""
    for char in s:
        if 'A' <= char <= 'Z':  
            result += chr(ord(char) + 32)
        elif 'a' <= char <= 'z':  
            result += chr(ord(char) - 32)
        else:
            result += char  
    return result

user_input = input("Enter a string: ")

print("Lowercase:", to_lowercase(user_input))
print("Uppercase:", to_uppercase(user_input))
print("Toggle case:", toggle_case(user_input))