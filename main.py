arr = [21, 2, 7, 4, 9]
counter = 0
coincidence = False

choice = input('\nYou can change el of array by index (i) or by value (v)\nChoose your route: ')
while choice != 'i' and choice != 'v':
    choice = input('\t\tError. Enter i or v: ')

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
    while not coincidence:
        for el in arr:
            if oldNum == el:
                coincidence = True
        if not coincidence:
            oldNum = int(input('\t\tError. Enter existing value: '))
    newNum = int(input('\tEnter value of array you wanna set: '))

    for el in arr:
        if el == oldNum:
            break
        else:
            counter += 1
    arr.insert(counter, newNum)
    arr.remove(oldNum)

print('Array: ', arr)
