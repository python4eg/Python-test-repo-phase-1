from typing import Union

class Person:
    def __init__(self, first_name: str, last_name: str, phone: Union[int, str], city: str):
        self._first_name = first_name
        self._last_name = last_name
        self._full_name = f'{last_name}, {first_name}'
        if not (type(phone) == str and phone.isdigit()) and type(phone) != int:
            raise ValueError(f'{phone} must be integer')
        self._phone = int(phone)
        self._city = city
    
    def getFullName(self):
        return self._full_name
    
    def getPhone(self):
        return self._phone

# Test:
# 1) phone is int and saved
# 2) get full name returns valid full name
# 3) if phone is str then phone become int
# 4) if phone is text - raise and error
# 5) All attributes are saved

def test_phone_is_int_success():
    expected_phone = 123345
    test_person = Person('A', 'B', expected_phone, 'C')
    if test_person.getPhone() == expected_phone:
        print('Phone check success')

print(f'Module name: {__name__}')

test_phone_is_int_success()


def add(x:int, y: int) -> int:
    return x + y