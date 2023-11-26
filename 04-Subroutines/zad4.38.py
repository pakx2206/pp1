def f(palindrome):
    for x in range(0, len(palindrome)):
        for y in range(len(palindrome)-1,-1,-1):
            if x>=y:
                break
            if palindrome[x]!=palindrome[y]:
                return False
    return True

print(f("radar"))
print(f("12-11-21"))
print(f("book"))