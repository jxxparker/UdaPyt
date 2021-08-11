def create_profile(given_name, *surnames, **details):
    print(given_name, *surnames)
    for key, value in details.items():
        print(key, value, sep=': ')
    

create_profile("Sam")
