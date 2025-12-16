class Location:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def myLocation(self):
        print("Hi, my name is " + self.name + " and I live in " + self.country +".")

# First instantiation of the class Location
loc1 = Location("Rosie", "Canada")
loc2 = Location("Ying", "China")
loc3 = Location("Amare", "Kenya")
loc4 = Location("Willian", "Brazil")

# Call a method from the instantiated class
loc1.myLocation()
loc2.myLocation()
loc3.myLocation()
loc4.myLocation()