class University():

    
    def __init__(self) -> None:
        self.name = 'CUE'
    def set_name(self,name):
        self.name = name
    def print_name(self):
        print(self.name)

x = University()
x.set_name('pakx')
x.print_name()