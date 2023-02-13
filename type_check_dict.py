person = {
"name" : "Tanumoy",
"Age"  :  36,
"Address" : "Michaelnagar"
}
print(type(person))
print(type(person['name']))
print(type(person["Age"]))
print(person["name"])
#we can check of a ey in dictionery using in key word
print("name" in person)
print("name4" in person)

person["Age"]=30
print(person["Age"])

person.update({"Age":20})
print(person["Age"])

person["eyecolour"]="Brown"
print(person)

person.update({"Haircolour":"Black"})
print(person)

person.pop("Haircolour")
print(person)

person.popitem()
print(person)

del person["Age"]
print(person)

person.clear()
print(person)

person = {
"name" : "Tanumoy",
"Age"  :  36,
"Address" : "Michaelnagar"
}
print(person)
