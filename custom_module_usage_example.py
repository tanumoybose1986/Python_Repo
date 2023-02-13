# print("Normal module usage ")
# import custom_module_example
# custom_module_example.greet_person("Tanumoy")

# using alisas and accessing variables
# print("using alisas and accessing variables")
# import custom_module_example as cme
# a = cme.personExample["Age"]
# print(a)


# use dir function to get all the variable
print("use dir function to get all the function both in build and custom")
import custom_module_example
x=dir(custom_module_example)
print(x)