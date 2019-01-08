def make_pizza(*toppings):
    "print all toppings from guest"
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushroom', 'green peppers', 'extra cheese')

def make_pizza_1(size,*toppings):
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
user_profile = build_profile('albert', 'einstein', location= 'princeton', field='physics')
print(user_profile)
