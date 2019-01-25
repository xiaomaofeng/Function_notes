def make_pizza(*toppings):
    "print all toppings from guest"
    print(toppings)


make_pizza('pepperoni')
make_pizza('mushroom', 'green peppers', 'extra cheese')


def make_pizza_1(size, *toppings):
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza_1(16, 'pepperoni')
make_pizza_1(12, 'mushrooms', 'green peppers', 'extra cheese')


def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)


def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + " 's name is " + pet_name.title() + ".")


describe_pet(animal_type='hamster', pet_name='harry')


def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + '' + middle_name + '' + last_name
    else:
        full_name = first_name + '' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
