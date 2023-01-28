class Student:
    id = 100000
    def __init__(self, name, surname, kierunek) -> None:
        self.name = name
        self.surname = surname
        Student.id += 1
        self.id = Student.id
        self.kierunek = kierunek
    def __str__(self) -> str:
        return f'{self.name}, {self.surname}, {self.id}, {self.kierunek}, UEK'
    
x = Student("Anna", "Maj", "Applied Informatics")
print(x)
x = Student("Anna", "Chech", "Applied Informatics")
print(x)


