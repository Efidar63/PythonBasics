#class

class Person:
#class attributes

  address ='no information'

#constructor(yapici method)
def __init__(self, name, year):
    #object attributes
    self.name=name
    self.year=year
    print('init method working')

#methods

#objects(instance)
p1=Person(name='ali', year=1999)
p2=Person(name='efidar', year=2000)


#updating

p1.name='can'
p2.address='almanya'
#accessing object attributes

print(f'p1 : name: {p1.name} year: {p1.year} adress: {p1.address}')
print(f'21 : name: {p2.name} year: {p2.year} adress: {p2.address}')


print(p1)
print(p2)
print(type(p1))
print(type(p2))
print(p1==p2)
