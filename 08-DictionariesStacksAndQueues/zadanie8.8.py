person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
   }
print("a.", person)

print("b.", person["name"])

print("c.", *person["hobby"])

x = person["surname"] = "Nowak"
print("d.", x)

person["married"] = False
print("e.", person["married"])

person["gender"] = "male"
print("f.",person["gender"])

person["hobby"].append("bicycle")
print("g.",person["hobby"])

person["phone"]["workphone"] = "313131444"
print("h.",person["phone"])