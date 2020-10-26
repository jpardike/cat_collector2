from django.db import models

# Create your models here.
class Cat:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

felix = Cat('Felix', 'ally cat', 'trouble maker', 5)

print(felix)