class Person:
    def __init__(self, first_name:str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name  
    
    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'
    
    def __format__(self, format_spec: str) -> str:
        return f"""{self.first_name}{format_spec} {self.last_name}"""
    

    def __str__(self):
        #return f'first={self.first_name} , last={self.last_name}'
        return self.__format__('->')  

if __name__=="__main__":
    person = Person('John', 'Doe')
    print(person)