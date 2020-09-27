from faker import Faker
f= Faker('tr')
f.name()
f.address()
f.email()
print(f'name: {f.name()}')
print(f'address: {f.address()}')
print(f'mail: {f.email()}')
