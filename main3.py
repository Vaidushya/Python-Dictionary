con_code = {'India' : '0091',
                'Australia' : '0025',
                'Nepal' : '00977'}

print("Country code for India -")
print(con_code.get('India', 'Not Found'))

print("Country code for Australia -")
print(con_code.get('Australia', 'Not Found'))

print("Country code for Nepal -")
print(con_code.get('Nepal', 'Not Found'))

print("Country code for Japan -")
print(con_code.get('Japan', 'Not Found'))