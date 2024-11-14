class Contact:
    def __init__(self,name,phone_number):
        self.name = name
        self.phone_number = phone_number
class ContactBook:
    def __init__(self):
        self.contacts = []
    def display(self):
        for index, contact in enumerate(self.contacts, start=1):
            print(f"{index} = {contact.name} {contact.phone_number}")
    def add(self,c):
        self.contacts.append(c)
    
    def search(self,query):
        for c in self.contacts:
            if  c.name == query or c.phone_number == query:
                print(f"{c.name} {c.phone_number}")
                return True
        return False
    def delete(self,contact):
        self.contacts.remove(contact)
            
    

c = [
    Contact("John Doe", "1234567890"),
    Contact("Jane Smith", "0987654321"),
    Contact("Alice Johnson", "9876543210")  # This contact number has been repeated for demonstration purposes.
]

bk_C = ContactBook()
for contact in c:
    bk_C.add(contact)

bk_C.display()
print(bk_C.search("John"))
bk_C.delete(c[0])
bk_C.display()

