names_list = []
with open("/Users/benjamin.chinwe/PycharmProjects/MailMerge/Input/Names/invited_names.txt") as f:
    name = f.read()
    with open("/Users/benjamin.chinwe/PycharmProjects/MailMerge/Input/Letters/starting_letter.txt") as f:
        letter = f.read()
        letter = letter.replace('[name]', name)
        print(letter)

    with open(f"/Users/benjamin.chinwe/PycharmProjects/MailMerge/Output/ReadyToSend/{name}.txt") as f:
        f.write(letter)