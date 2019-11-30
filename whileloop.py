#start with user that need to verified
# and an empty list to told confirmed users.
unconfirmed_users =['alice', 'brain', 'candace']
confirmed_users =[]

#verify each user  untill there are no more unconfirmed users
#move each verified user in to the list of confirmed users
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"verified user: {current_user.title()}")
    confirmed_users.append(current_user)
    
    # display all confirmed user_users
    print("\nthe following users have been confirmed:")
    for confirmed_user in confirmed_users:
        print(confirmed_user.title())
        
    
    