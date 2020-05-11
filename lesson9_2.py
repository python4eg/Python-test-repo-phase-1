"""
Acceptance Criteria
1. File present, if file doesn't exists - raise an error
2. Application works with json read and save
3. Promt user with options:
   a. Add entry
   b. Find entry:
        Search by first name 
        Search by last name 
        Search by full name
        Search by telephone number
        Search by city or state
   c. Delete entry by phonenumber
   d. Update entry by phonenumber
   e. Exit app
4. Save phone book into json file after exit
5. Read existing phonebook from json file

The first argument to the application should be the name of the phonebook.

Algorithm:
1. open file
2. raise an error if file doesn't exist
3. read json
4. if during reading error appears ignore and create empty list
5. try except finally on global level to save file anyway
6. Print menu
7. if user selected add new record:
   1. Ask user put data
   2. Append data to list
8. if user selected search/delete record:
   1. ...
"""
import json
import sys

print(sys.argv)
if len(sys.argv) < 2:
    print('Please specify json file name')
    exit()
filename = sys.argv[1]
json_file = open(filename)
try:
    phonebook = json.load(json_file)
except json.decoder.JSONDecodeError:
    phonebook = []
json_file.close()

dict_pattern = {
    'first_name': '',
    'last_name': '',
    'full_name': '',
    'phone': '',
    'city': ''
}

try:
    while True:
        command = input('Select command: ').strip().lower()
        if command == 'add':
            first_name = input('Print first name: ')
            last_name = input('Print last name: ')
            full_name  = first_name + ' ' + last_name
            phone = input('Print phone: ')
            city = input('Print city: ')
            new_entry = dict_pattern.copy()
            new_entry['first_name'] = first_name
            new_entry['last_name'] = last_name
            new_entry['full_name'] = full_name
            new_entry['phone'] = phone
            new_entry['city'] = city
            phonebook.append(new_entry)
            print('new_entry id: ' + str(id(new_entry)))
            print('dict_pattern id: ' + str(id(dict_pattern)))
            print('Ids in list: ' + ','.join([str(id(item)) for item in phonebook]))
            print('New entry:')
            print(new_entry)
            print('List of items')
            print(phonebook)
            # If you don't use copy in new_entry = dict_pattern.copy()
            # This code will change all items in list
            phonebook[0]['first_name'] = 'NEW'
            print('List of items after changing first element')
            print(phonebook)
        elif command == 'search':
            query = input('First name: ')

            for item in phonebook:
                if item['first_name'] == query:
                    print('Found person:')
                    print(item)
                    action = input("""What to do next: 
                    next - search next record
                    delete - remvoe record
                    menu - return to menu
: """).strip().lower()
                    if action == 'menu':
                        break
                    elif action == 'next':
                        continue
                    elif action == 'delete':
                        phonebook.remove(item)
                        break
            
except Exception as e:
    print('Unexpected error.')
    print(e)
finally:
    with open(filename, 'w') as json_file:
        json.dump(phonebook, json_file, indent=4)