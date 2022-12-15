# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("./Input/Letters/starting_letter.txt", mode="r") as starting_letter:
    letter = starting_letter.read()

with open("./Input/Names/invited_names.txt", mode="r") as names_list:
    list_of_names = names_list.readlines()


for i, name in enumerate(list_of_names):

    name = name.strip()
    replaced_letter = letter.replace("[name]", name)

    with open(f"./Output/ReadyToSend/letter_to_{name}.txt", mode="w") as ready_to_send:
        ready_to_send.write(replaced_letter)

print(list_of_names)
