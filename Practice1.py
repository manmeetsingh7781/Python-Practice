// Define a class
class Person:
    // A construstor
    def __init__(self, name, dob):
        self.name = name;
        self.dob = dob;
    
    // prints name and dob to string aka magic functions with double underscores
    def __str__(self):
        print(self.name +  " is " + str(self.dob));
    
    // Add, compare two class instances 
    def __add__(self, other):
        if(self.dob > other.dob):
            print(self.name + " meet " + other.name);
        else: print(other.name + " meet " + self.name);

// prints number 1 to 9
for i in range(1, 10):
    print(i);

// creates a array of numbers, start -> stop -> step
print(list(range(1, 100, 10)))


harry =  Person("Manmeet Singh", 20);
honey =  Person("Harmeet Singh", 22);
harry.__str__();
honey.__str__();
harry.__add__(honey);
