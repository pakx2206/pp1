a = str(input("Enter EAN-13 article number:"))
if len(a)!=13:
    print("Aricle number is incorrect")
else:
    print("Aricle number is correct")
    if a[0]=="5" and a[1]=="9" and a[2]=="0":
        print("Article manufactured in Poland")