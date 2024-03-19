# Lesson 4 : Design Pattern (Prototype)

# Clone Library
import copy

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def clone(self):
        return User(self.name, self.age)
    
    def __eq__(self, other):
        if self is other:
            return True
        if other is None or type(self) != type(other):
            return False
        
        return self.name == other.name
    
    # Define String for `User` class
    # __repr__ used when print an instance
    def __repr__(self):
        return f"{self.name}, age={self.age}"
    
    def hashCode(self):
        return hash((self.name, self))
    
    
class PrototypePattern:
    @staticmethod
    def main():
        original = User("Hazim", 23)
        clone = original.clone()
        
        # Print original and not original
        # Print whether is the product is original or not (True or False)
        print(original, original is original)
        print(clone, original is clone)
        
# Run
if __name__ == "__main__":
    PrototypePattern.main()