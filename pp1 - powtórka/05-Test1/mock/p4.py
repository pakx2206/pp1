def f(card_number):
    return card_number[:2] + "*"*10 + card_number[12:]

print(f("5290312400019022"))