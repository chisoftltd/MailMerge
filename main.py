
#   Get the guest list from file
with open("./Input/Names/invited_names.txt") as fname:
    names_list = fname.readlines()

#   Get invite letter template from file
with open("./Input/Letters/starting_letter.txt") as fletter:
    letter = fletter.read()

#   Insert invitees name into temple letter
inviteLetter = []
for name in names_list:
    inviteLetter = letter.replace('[name]', f"{name.strip()}")

    # Write the invite letters to file
    with open(f"./Output/ReadyToSend/{name.strip()}.txt", mode="w") as f:
        print(inviteLetter)
        f.write(inviteLetter)

