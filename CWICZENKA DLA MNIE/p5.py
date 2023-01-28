class C():
    def __init__(self, numbers) -> None:
        self.numbers = numbers
    def __str__(self) -> str:
        x = '+'.join(map(str,(self.numbers)))
        suma = sum(self.numbers)
        return f"{x}={suma}"

print(C([5,12]))