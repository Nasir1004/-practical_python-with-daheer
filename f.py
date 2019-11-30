responses ={}
#set a flag indicate  that polling unit is active.
polling_active = True

while polling_active:
    #prompt for the person name response.
    
    name =input("\nwhat is your name?")
    response =input("which mountain whould you like to climb")
    #store the response in the dictionary
    responses[name] =response
    
    #find out if anyone else is going to take the poool
    repeat=input("whold you like to let another person response? (yes/no)")
if  repeat == 'no':
    polling_active = False
    
    # polling is comlete show the result.
    print("\n=====poll result========")
for name ,response in responses.items():
    print(f"{name} would you like to climb {response}.")
            