"""Try and Excepts error"""
# Try = cause of exception
# Except = Do this block if there was an exception
# else = Do this if not exceptions
# finally = Do this no matter what happens
# raise = raise your own exceptions

# FileNotFound

# try:
#     file = open("a_file.txt")
#     a_dict = {"key": "value"}
#     print(a_dict["key"])
# # types of errors
# except FileNotFoundError:
#     with open("a_file.txt", "w") as file:
#         file.write("Something")
# # error message
# except KeyError as error_message:
#     print(f"That key {error_message} does not exit")
# else:
#     content = file.read()
#     print(content)
# finally:
#     # raises an error even if there are no errors in your code
#     raise TypeError("This is ane error I made up")
#


height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters")

bmi = weight / height ** 2
print(bmi)
