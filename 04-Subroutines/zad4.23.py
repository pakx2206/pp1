import howmany

def main():
    x = input("Enter your phrase: ")
    target = "e"
    return f'The number of letter "e": {howmany.howmanyx(x,target)}'

if __name__ == "__main__":
    print(main())