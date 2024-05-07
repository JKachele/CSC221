class contact:
    def __init__(self, name, number, email, address):
        self.name = name
        self.number = number
        self.email = email
        self.address = address
        self.nameStr = ' '.join(self.name)
        self.addressStr = ' '.join(self.address)

    def __str__(self):
        name = ' '.join(self.name)
        address = ' '.join(self.address)
        return f"{name:<12} {str(self.number):<12} {self.email:<15} {address:<12}"


contact1 = contact(("John", "Doe"), 1234567890, "jd@gmail.com", ("4526", "Bob Rd", "Manassas", "VA", "20109"))
contact2 = contact(("Jane", "Doe"), 9876543210, "jnd@gmail.com", ("4527", "Bob Rd", "Manassas", "VA", "20109"))
contact3 = contact(("Bob", "Lewis"), 9638257410, "bobl@gmail.com", ("59871", "Doe Rd", "Fairfax", "VA", "22030"))

print(contact1)
print(contact2)
print(contact3)
print()

print(f"{'Name':<13}{'Number'}")
print(f"{' '.join(contact1.name):<13}{contact1.number}")
print(f"{' '.join(contact2.name):<13}{contact2.number}")
print(f"{' '.join(contact3.name):<13}{contact3.number}")
print()

nameInput = input("Input full name: ").lower()
if nameInput == contact1.nameStr.lower():
    print(f"Phone Number: {contact1.number}")
elif nameInput == contact2.nameStr.lower():
    print(f"Phone Number: {contact1.number}")
elif nameInput == contact3.nameStr.lower():
    print(f"Phone Number: {contact3.number}")
else:
    print("Name Not Found")
print()

nameInput = input("Input first name: ").lower()
if nameInput == contact1.name[0].lower():
    print(f"Address: {contact1.addressStr}")
elif nameInput == contact2.name[0].lower():
    print(f"Address: {contact2.addressStr}")
elif nameInput == contact3.name[0].lower():
    print(f"Address: {contact3.addressStr}")
else:
    print("Name Not Found")


