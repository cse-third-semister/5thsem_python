tdls = {"canada":"ca","United state":"us","mexico":"mx"}
#a
if(tdls.__contains__("canada")):
    print("yes")
else:
    print("No")
#b
if(tdls.__contains__("canada")):
    print("yes")
else:
    print("No")
#c
for key,value in tdls.items():
    print(f'{key} : {value}')
#d
tdls["sweden"] = "sw"
print(tdls)
#e
tdls["sweden"] = "se"
print(tdls)
#f
reversed_dict = {value: key for key, value in tdls.items()}
print(reversed_dict)



# yes
# yes
# canada : ca
# United state : us
# mexico : mx
# {'canada': 'ca', 'United state': 'us', 'mexico': 'mx', 'sweden': 'sw'}
# {'canada': 'ca', 'United state': 'us', 'mexico': 'mx', 'sweden': 'se'}
# {'ca': 'canada', 'us': 'United state', 'mx': 'mexico', 'se': 'sweden'}