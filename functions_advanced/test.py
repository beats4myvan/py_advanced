def some_func(name, age):

    print(f"{name} is {age} years old")

person = {'age': 20, 'name': "Peter"}

some_func(**person)