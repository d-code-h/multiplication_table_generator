print('''
Welcome to this Multiplcation Table Generator
''')

print('Which Multiplication table do you desire?')
table = int(input())

print('The table should ends at? (e.g. 12)')
end_point = int(input())

print('Any interval? (Empty or no interval)')
interval = input()

if interval:
    for i in range(1, end_point+1, int(interval)):
        print(str(table) + ' x ' + str(i) + ' = ' + str(table * i))
else:
    for i in range(1, end_point+1):
        print(str(table) + ' x ' + str(i) + ' = ' + str(table * i))