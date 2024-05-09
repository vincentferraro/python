print('hello world')

def iamPython():
    print("I'm backend developer Python")

iamPython()


class Person:
    def __init__(self,name: str, lastname : str):
        self._name= name
        self._lastname = lastname
    
    def set_name(self, name:str):
        self.name = name
    
    def get_name(self):
        return self._name
    
    def set_lastname(self, lastname:str) -> None:
        self._lastname = lastname
    
    def get_lastname(self) -> str:
        return self._lastname
    

vinc = Person("vinc", "f")

print(vinc.get_name())
vinc.set_name("Nah")
print(vinc.get_name())

print(vinc.get_lastname())