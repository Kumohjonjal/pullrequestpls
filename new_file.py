class PhoneBook:
    def __init__(self):
        self.names = ('KIM', 'LEE', 'PARK')
        self.phones = ('111-1111', '222-2222', '333-3333')

    def search(self, name):
        if name in self.names:
            idx = self.names.index(name)
            return idx
        else:
            return None

    def print_one(self, idx):
        name = self.names[idx]
        print("{0}{1}'s phone number is {2}".format(name[0] ,name[1:], self.phones[idx]))

    def print_all(self):
        n = len(self.names)
        for i in range(n):
            self.print_one(i)

name = input('Input your name: ')
name = name.strip().upper()

phonebook = PhoneBook()

idx = phonebook.search(name)

if idx != None:
    phonebook.print_one(idx)
else:
    print('Not registered name')

phonebook.print_all()
