with open('07-FileHandling/shoppinglist.txt','w') as shop:
    with open('07-FileHandling/GrainsAndBread.txt','r') as gab:
        with open('07-FileHandling/MeatAndFish.txt','r') as maf:
            for line in gab:
                shop.write(line)
            for line in maf:
                shop.write(line)
