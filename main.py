arr = [21, 2, 7, 4, 9]
choice = input('\nYou can change el by index (i) or by value (v)\nChoose your route: ')
counter = 0

while choice != 'i' and choice != 'v':
    choice = input('\tError. Enter i or v: ')

print('Array: ', arr)

if choice == 'i':
    oldNum = int(input('\tEnter index of array you wanna change: '))
    while oldNum > 5 or oldNum < 1:
        oldNum = int(input('\t\tError. Enter existing index: '))
    newNum = int(input('\tEnter value of array you wanna set: '))

    res = arr
    arr[oldNum - 1] = newNum
else:
    oldNum = int(input('\tEnter value of array you wanna change: '))
    newNum = int(input('\tEnter value of array you wanna set: '))

    for el in arr:
        if el == oldNum:
            break
        else:
            counter += 1
    arr.insert(counter, newNum)
    arr.remove(oldNum)

print(arr)
