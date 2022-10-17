# num1 = 2.6
# print(int(num1))

# num2 = 5
# print(float(num2))

# num3=2.5
# num4=7
# print(num3+num4)
# print(num4+int(num3))
# print(num3+float(num4))

nombre = input('\nHola! Dime tu nombre: ')
ventas = float(input('¿Cual fue el importe de tus ventas?: '))

print(f'\nOk, {nombre} tus comisiones son ${(ventas*13)/100}\n')
