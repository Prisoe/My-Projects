#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Get all names from file into a list
all_names = []
PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt", mode='r') as file:
    names = file.readlines()
    for name in names:
        space_remove = name.strip()
        all_names.append(space_remove)

    # print(all_names)


# Open starting_letter.txt line by line and loop to replace names
with open("./Input/Letters/starting_letter.txt", mode='r') as file:
    words = file.read()
    for name in all_names:
        complete = words.replace(PLACEHOLDER, name)
        # append letter to Ready to send
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode='w') as ready:
            ready.write(complete)




