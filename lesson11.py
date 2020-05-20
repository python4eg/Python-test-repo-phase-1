class Example:
    name = 'Deafult'

    def __init__(self, name):
        self.name = name
    
    def reset(self):
        self.name = Example.name

class Counter:

    def __init__(self, ppl):
        self.ppl = ppl
        self.person_number = 1
    
    def get_current_person(self):
        return self.ppl[self.person_number - 1]

    def next_person_version_1(self):
        if self.person_number >= len(self.ppl):
            self.person_number = 1
        else:
            self.person_number += 1
        return self.get_current_person()

    def next_prev_version_1(self):
        if self.person_number == 1:
            self.person_number = len(self.ppl)
        else:
            self.person_number -= 1
        return self.get_current_person()

    def get_person(self, index):
        if 0 < index <= len(self.ppl):
            self.person_number = index
        return self.get_current_person()

ppl = 'Стакан води вийти ти стакан сиропу їдь в Європу'.split(' ')
counter = Counter(ppl)
print(counter.get_current_person())
print(counter.next_person_version_1())
print(counter.next_person_version_1())
print(counter.next_person_version_1())
print(counter.next_person_version_1())
print(counter.next_person_version_1())
print(counter.next_person_version_1())
print(counter.next_person_version_1())
print(counter.next_person_version_1())


index = 0
while False:
    print(ppl[index])
    index = (index + 1) % len(ppl)


class EvenCounter(Counter):

    def __init__(self, ppl):
        super().__init__(ppl)
        self.person_number = 2

    def get_next_even(self):
        if self.person_number % 2 == 0:
            self.person_number += 2
        else:
            self.person_number += 1
        if self.person_number > len(self.ppl):
            self.person_number = 2
        return self.get_current_person()

evenCounter = EvenCounter(['Микола', 'Галина', 'Дзвінка', 'Золтан', 'Болтан', 'Іезікеїл', 'Двейн', 'Флойд'])
print(evenCounter.get_current_person())
print(evenCounter.get_next_even())
print(evenCounter.get_next_even())
print(evenCounter.get_next_even())
print(evenCounter.get_next_even())
print(evenCounter.get_next_even())
print(evenCounter.get_next_even())

print(Counter.__dict__)
print(EvenCounter.__dict__)
print(evenCounter.__dict__)


class Person:
    def __init__(self, first_name, last_name):
        print('Person.__init__() ->')
        self.first_name = first_name
        self.last_name = last_name
        print('Person.__init__() <-')


class FullNamePerson(Person):
    def __init__(self, first_name, last_name):
        print('FullNamePerson.__init__() ->')
        super().__init__(first_name, last_name)
        self.full_name = f'{self.last_name}, {self.first_name}'
        print('FullNamePerson.__init__() <-')


class AbbrevPerson(Person):
    def __init__(self, first_name, last_name):
        print('AbbrevPerson.__init__() ->')
        super().__init__(first_name, last_name)
        self.abbrev = f'{self.last_name} {self.first_name[0]}'
        print('AbbrevPerson.__init__() <-')


class RealPerson(AbbrevPerson, FullNamePerson):
    def __init__(self, first_name, last_name):
        print('RealPerson.__init__() ->')
        super().__init__(first_name, last_name)
        print('RealPerson.__init__() <-')


rp = RealPerson('Master', 'Chief')
print(RealPerson.mro())
print('--------')
print(rp.first_name)
print(rp.last_name)
print(rp.full_name)
print(rp.abbrev)

#Old style inheritance example
class Person:
    def __init__(self, first_name, last_name):
        print('Person.__init__() ->')
        self.first_name = first_name
        self.last_name = last_name
        print('Person.__init__() <-')


class FullNamePerson(Person):
    def __init__(self, first_name, last_name):
        print('FullNamePerson.__init__() ->')
        Person.__init__(self, first_name, last_name)
        self.full_name = f'{self.last_name}, {self.first_name}'
        print('FullNamePerson.__init__() <-')


class AbbrevPerson(Person):
    def __init__(self, first_name, last_name):
        print('AbbrevPerson.__init__() ->')
        Person.__init__(self, first_name, last_name)
        self.abbrev = f'{self.last_name} {self.first_name[0]}'
        print('AbbrevPerson.__init__() <-')


class RealPerson(AbbrevPerson, FullNamePerson):
    def __init__(self, first_name, last_name):
        AbbrevPerson.__init__(self, first_name, last_name)
        FullNamePerson.__init__(self, first_name, last_name)
rp = RealPerson('Master', 'Chief')
print(RealPerson.mro())
print('--------')
print(rp.first_name)
print(rp.last_name)
print(rp.full_name)
print(rp.abbrev)


class Person:
    def __init__(self, first_name, last_name, *args, **kwargs):
        print('Person.__init__() ->')
        self.first_name = first_name
        self.last_name = last_name
        print('Person.__init__() <-')


class Covid5GPerson(Person):
    def __init__(self, first_name, last_name, chip_id, bat_dna, *args, **kwargs):
        print('Covid5GPerson.__init__() ->')
        super().__init__(first_name, last_name, chip_id, bat_dna, *args, **kwargs)
        self.full_name = f'{self.last_name}, {self.first_name}'
        self.chip_id = chip_id
        self.bat_dna = bat_dna
        print('Covid5GPerson.__init__() <-')

class AbbrevPerson(Person):
    def __init__(self, first_name, last_name, *args, **kwargs):
        print('AbbrevPerson.__init__() ->')
        super().__init__(first_name, last_name, *args, **kwargs)
        self.abbrev = f'{self.last_name} {self.first_name[0]}'
        print('AbbrevPerson.__init__() <-')


class RealPerson(AbbrevPerson, Covid5GPerson):
    def __init__(self, first_name, last_name, chip_id, bat_dna):
        print('RealPerson.__init__() ->')
        super().__init__(first_name, last_name, chip_id, bat_dna)
        print('RealPerson.__init__() <-')

rp = RealPerson('Bill', 'gates', 665, 'TATACGTC')
print('--------')
print(rp.first_name)
print(rp.last_name)
print(rp.full_name)
print(rp.abbrev)

def infinite_args(*args, **kwargs):
    print(args)
    print(kwargs)

infinite_args(1, 2, 3, 4, key=4, smth=6)


class Engine:
    def __init__(self, power):
        self.power = power


class Car:
    def __init__(self, ppl):
        self.ppl = ppl
        self.engine = Engine(power)

class Brain:
    pass

class StrangePerson:
    def __init__(self, clothes):
        self.clothes = clothes
        self.brain = Brain()