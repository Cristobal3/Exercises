
#Problem 1
class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0
    
    def __str__(self):
        return 'Person: {} {} {}'.format(self.name, self.email, self.phone)

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
        self.greeting_count += 1

    def print_contact_info(self):
        print('{}\'s email is {}, {}\'s phone number: {}'.format(self.name, self.email, self.name, self.phone))
    
    def add_friend(self,friend):
        self.friends.append(friend.name)
    
    def num_friends(self):
        print(len(self.friends))
    



sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')

sonny.greet(jordan)
jordan.greet(sonny)
sonny.add_friend(jordan)
sonny.num_friends()

#Prblem 2
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def print_info(self):
        print('{} {} {}'.format(name.year,name.make,name.model))

       
