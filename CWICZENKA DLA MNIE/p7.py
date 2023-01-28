class C:
    @staticmethod
    def m1(n):
        return int("".join([d for d in str(n) if int(d) % 2 == 0]))
    
    @staticmethod
    def m2(n):
        digits = [int(d) for d in str(n)]
        for i in range(1, len(digits)):
            if digits[i] < digits[i - 1]:
                return False
        return True
    
    @staticmethod
    def m3(n):
        missing_digits = set(str(i) for i in range(10)) - set(str(n))
        return "".join(sorted(missing_digits))
