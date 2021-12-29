
#   Get the guest list from file
with open("./Input/Names/invited_names.txt") as fname:
    names_list = fname.readlines()

#   Get invite letter template from file
with open("./Input/Letters/starting_letter.txt") as fletter:
    letter = fletter.read()

#   Insert invitees name into temple letter
inviteLetter = []
for name in names_list:
    new_name = name.strip()
    inviteLetter = letter.replace('[name]', f"{new_name}")

    # Write the invite letters to file
    with open(f"./Output/ReadyToSend/Letter_for_{new_name}.txt", mode="w") as f:
        print(inviteLetter)
        f.write(inviteLetter)

