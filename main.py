
#   Get the guest list from file
with open("/Users/benjamin.chinwe/PycharmProjects/MailMerge/Input/Names/invited_names.txt") as fname:
    names_list = fname.read().rsplit()

#   Get invite letter template from file
with open("/Users/benjamin.chinwe/PycharmProjects/MailMerge/Input/Letters/starting_letter.txt") as fletter:
    letter = fletter.read()

#   Insert invitees name into temple letter
inviteLetter = []
for name in names_list:
    inviteLetter = letter.replace('[name]', f"{name}")

    # Write the invite letters to file
    with open(f"/Users/benjamin.chinwe/PycharmProjects/MailMerge/Output/ReadyToSend/{name}.txt", mode="w") as f:
        print(inviteLetter)
        f.write(inviteLetter)

