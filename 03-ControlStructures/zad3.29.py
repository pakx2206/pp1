def washing_machine(washing_product, rinse, spin):
    sum = 0
    if washing_product == "shoes":
        sum += 20
    if washing_product == "jacket":
        sum += 40
    if washing_product == "underwear":
        sum += 70
    if rinse == True:
        sum += 15
    if spin == True:
        sum += 9
    return f'Total washing time: {sum} minutes'

print(washing_machine("shoes",True,False))