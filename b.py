fevourite_language = {
    'nasir':['python','php' 'ruby'],
    'umar':['java','node'],
    'ahmad':['matlab','js'],
    'sharu':[ 'vb'],
    'abba':  ['c#']
    }
freinds= ['ahmad', 'umar']
for name,language in fevourite_language.items():
    print(name.title())
    
for name, language in fevourite_language.items():
    print(f"\n{name.title()} my fevourite language is, {language}")
    
    
if name in freinds:
    language = fevourite_language [name].title()
print(f"\t{name.title()}, i see you fevourite language is {language}")
if 'nuhu' not in fevourite_language.keys():
    print ('\nnuhu you are not i n our pool')
    