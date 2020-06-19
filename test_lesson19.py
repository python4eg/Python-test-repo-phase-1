import unittest
from lesson19 import Person, add


class TestPerson(unittest.TestCase):
    @unittest.skip('Ancient approach. No more pure asserts.!!!')
    def test_phone_is_int_old_way_success(self):
        expected_phone = 123345
        test_person = Person('A', 'B', expected_phone, 'C')
        actual_phone = test_person.getPhone()
        assert actual_phone == expected_phone
        actual_phone = test_person.getPhone()
        assert type(actual_phone) == int
 
    def test_phone_is_int_success(self):
        expected_phone = 123345
        test_person = Person('A', 'B', expected_phone, 'C')
        actual_phone = test_person.getPhone()
        self.assertEqual(actual_phone, expected_phone)

    def test_fullname_success(self):
        expected_fullname = 'B, A'
        test_person = Person('A', 'B', 12345, 'C')
        actual_fullname = test_person.getFullName()
        self.assertEqual(actual_fullname, expected_fullname)
 
    def test_str_phone_is_int_success(self):
        expected_phone = 123345
        test_person = Person('A', 'B', str(expected_phone), 'C')
        actual_phone = test_person.getPhone()
        self.assertEqual(actual_phone, expected_phone)
 
    def test_text_phone_failed(self):
        with self.assertRaises(ValueError) as context:
            test_person = Person('A', 'B', 'expected_phone', 'C')
        self.assertEqual('expected_phone must be integer', str(context.exception))

    def test_person_attrs_saved_success(self):
        expected_fname = 'A'
        expected_lname = 'B'
        expected_phone = 123345
        expected_city = 'C'
        expected_fullname = 'B, A'
        test_person = Person(expected_fname, 
                             expected_lname,
                             expected_phone,
                             expected_city)
        self.assertEqual(test_person._first_name, expected_fname)
        self.assertEqual(test_person._last_name, expected_lname)
        self.assertEqual(test_person._full_name, expected_fullname)
        self.assertEqual(test_person._phone, expected_phone)
        self.assertEqual(test_person._city, expected_city)

class TestAdd(unittest.TestCase):
    def test_add_success(self):
        x = 1
        y = 2
        expected_result = 3
        actual_result = add(x, y)
        assert actual_result == expected_result, f'Result of adding 1 and 2 should be 3 but got {actual_result}'

if __name__ == '__main__':
    unittest.main()
