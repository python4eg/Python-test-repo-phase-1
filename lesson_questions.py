import json

example_dict = {
    'name': None
}

class Example:
    name = None

example_list = []

new_dict = example_dict
new_dict['name'] = 'Name 1'
example_list.append(new_dict)

new_dict = example_dict
new_dict['name'] = 'Name 2'
example_list.append(new_dict)
print(example_list)
print(', '.join(str(id(i)) for i in example_list))

example_list = []

person = Example()
person.name = 'Name 1'
example_list.append(person)

person = Example()
person.name = 'Name 2'
example_list.append(person)
print(', '.join(i.name for i in example_list))
print(', '.join(str(id(i)) for i in example_list))


file_obj = open('test.json')
try:
    json_data = json.load(file_obj)
    print(json_data)
except json.decoder.JSONDecodeError as e:
    json_data = []
if type(json_data) != list:
    json_data = []
print(json_data)

dict_pattern = {
    'name': None
}
ppl = []

def create_person():
    first_name = input('first name')
    new_person = dict_pattern.copy()
    new_person['name'] = first_name
    return new_person

ppl.append(create_person())
print(ppl)


def print_data(data)
    data += 1
    print(data)


print_data(1234)


def get_data(data)
    data += 1
    return data
print(get_data(1234))

