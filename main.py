arr = []
counter = 0
coincidence = False

userArray = input('\nEnter array from numbers divided with ","\n\tYour array: ')
userArray = userArray.split(',')
for el in userArray:
    arr.append(int(el))

choice = input('\nYou can change element of array by index (i) or by value (v)\n\tChoose your route: ')
while choice != 'i' and choice != 'v':
    choice = input('\t\tError. Enter i or v: ')

print('\nOld array: ', arr)

if choice == 'i':
    oldNum = int(input('\tEnter index of array you wanna change: '))
    while oldNum > len(arr) or oldNum < 1:
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

print('\nNew array: ', arr)
