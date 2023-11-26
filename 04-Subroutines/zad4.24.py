import isinrange
def main():
    num = int(input("A number: "))
    set_x = 2
    set_y = 15
    if isinrange.range(num, set_x, set_y)==True:
        return f'Number {num} in the range <{set_x},{set_y}>: yes'
    else:
        return f'Number {num} in the range <{set_x},{set_y}>: no'
    

if __name__=="__main__":
    print(main())
    