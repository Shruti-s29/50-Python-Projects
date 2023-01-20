PLACEHOLDER = "[name]"
output = []

with open("24.Template_mail_generator.py\members.txt") as names_file:
    names = names_file.readlines()


with open('24.Template_mail_generator.py\message.txt') as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        output.append([new_letter])

    print(output)
