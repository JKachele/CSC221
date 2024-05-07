class contact:
    def __init__(self, name, number, email, address):
        self.name = name
        self.number = number
        self.email = email
        self.address = address

    def __str__(self):
        return f"{self.name} {self.number} {self.email} {self.address}"


contact1 = contact(("John", "Doe"), 1234567890, "jd@gmail.com", (4526, "Bob Rd", "Manassas", "VA", 20109))
contact2 = contact(("Jane", "Doe"), 9876543210, "jnd@gmail.com", (4526, "Bob Rd", "Manassas", "VA", 20109))
contact3 = contact(("Bob", "Lewis"), 9638257410, "bobl@gmail.com", (59871, "Doe Rd", "Fairfax", "VA", 22030))

print(contact1)
print(contact2)
print(contact3)

