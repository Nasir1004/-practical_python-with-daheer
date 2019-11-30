users ={
    'Nasir':{
     'first':' nasir ibrahim',
     'last': 'abba',
     'location': 'london',
     
    },
    
    'ahmad':{
        'first': ' ahmad musa',
        'last': 'jibril',
        'location': 'paris',
        },
    
     'abbas':{
         'first': 'abbas kabir ',
         'last': ' Dahir',
         'location': 'nigeria',
         },
    
    }
for username, user_info in users.items():
    print(f"\nusername: {username})")
    full_name =f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tfull name: {full_name.title()}")
    print(f"\tlocation: {location.title()}")

    