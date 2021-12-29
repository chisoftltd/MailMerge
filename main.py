with open("/Users/benjamin.chinwe/PycharmProjects/MailMerge/Input/Names/invited_names.txt") as fname:
    names_list = fname.readline().rsplit()

    while names_list:
        with open("/Users/benjamin.chinwe/PycharmProjects/MailMerge/Input/Letters/starting_letter.txt") as fletter:
            letter = fletter.read()
            letter = letter.replace('[name]', fname.readline().replace("\n", ""))
            print(letter)
            name = fname.readline().replace("\n", "")
        with open(f"/Users/benjamin.chinwe/PycharmProjects/MailMerge/Output/ReadyToSend/{name}.txt", mode="w") as f:
            f.write(letter)
