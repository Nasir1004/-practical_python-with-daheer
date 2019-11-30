requested_cars =['honda','toyota','bmw']
available_cars=['subaru','venz','qlink']
car =(input("what type of car do you like?"))
if ['honda','toyota','bmw'] in requested_cars:
    print(f"we don't have {car.title()}")
else:
    print (f"\nlet me see if i can find you{available_cars}")