import os


def create(file):
    open(file, 'w').close()


def add_file_content(file_name, content):
    with open(file_name, 'a') as file:
        file.write(content)
        file.write('\n')


def replace(file_name, old_str, new_str):
    with open(file_name, 'r+') as file:
        file_content = file.read()
        new_content = file_content.replace(old_str, new_str)
        file.seek(0)
        file.truncate()
        file.write(new_content)


command = input()
while not command == 'End':
    if command.startswith('Create'):
        file_name = command.split('-')[1]
        create(file_name)

    elif command.startswith('Add'):
        _, file_name, content = command.split('-')
        add_file_content(file_name, content)

    elif command.startswith('Replace'):
        _, file_name, old_string, new_string = command.split('-')
        if os.path.exists(file_name):
            replace(file_name, old_string, new_string)
        else:
            print("An error occurred")

    elif command.startswith('Delete'):
        _, file_name = command.split('-')
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print("An error occurred")

    command = input()

"""
Create-file.txt
Add-file.txt-First Line
Add-file.txt-Second Line
Replace-random.txt-Some-some
Replace-file.txt-First-1st
Replace-file.txt-Second-2nd
Delete-random.txt
End
"""

