class C():
    def __init__(self, numb):
        self.numb = numb

    def m1(self):
        return self.numb

    def m2(self):
        self.numb += 1

    def m3(self):
        self.numb -= 1

    def m4(self, n):
        self.numb += n



c = C(5)
c.m1()
c.m2()
c.m1()
c.m4(-8)
c.m1()
c.m3()
c.m1()
c.m4(10)
c.m1()
