skin_type = None

class Animal:
    breathing_organ = None
    limbs = []
    skin_type = None

    def __init__(self, tail=None):
        self.tail = tail

    def eat(self):
        self.skin_type 

    def move(self):
        print('Я йду, не наклич на нас біду, зачекай мене я йду!')

    def consume_oxygen(self):
        self.move()
    
    def get_skin_type(self):
        print(f'мій тип шкіри {self.skin_type}')
        print(f'Мейнстрімний тип шкіри {Animal.skin_type}')

animal = Animal()
animal.skin_type = 'Луска'

print(f'animal skin type {animal.skin_type}')
other_animal = Animal(tail='Корма')

print(f'other_animal skin type {other_animal.skin_type}')
third_animal = Animal()

Animal.skin_type = 'Fur'
print(f'animal skin type after chaging default {animal.skin_type}')
print(f'other_animal skin type after chaging default {other_animal.skin_type}')
print(f'third_animal skin type after chaging default {third_animal.skin_type}')

print(Animal.skin_type is animal.skin_type)
print(Animal.skin_type is other_animal.skin_type)
other_animal.skin_type = 'Волосся'
animal.tail = 'Sword tail'

animal.get_skin_type()
Animal.get_skin_type(animal)

Animal.get_skin_type(other_animal)

print('Default Animal methods and attributes')
print(Animal.__dict__)
print('Object animal methods and attributes')
print(animal.__dict__)

print(f'animal tail {animal.tail}')
print(f'other_animal tail {other_animal.tail}')

Animal.get_skin_type(animal)


print(f'animal class name {animal.__class__.__name__}')

class FakeTaxi: pass

print(isinstance(animal, Animal))
print(isinstance(animal, FakeTaxi))

