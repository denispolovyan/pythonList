def getArrayFromUser():
    array = []
    enterArray = True

    while enterArray:
        el = input('\tPrint array element: ')
        if not el.isnumeric():
            if len(array) < 3:
                print('\t\tError. Array must include at least 3 elements')
                continue
            else:
                enterArray = False
        else:
            array.append(el)

    return array


def changeElementsToInt(array):
    newArray = []

    for el in array:
        newArray.append(int(el))
    return newArray


def changeNumByIndex(array):
    newArray = array
    oldNum = int(input('\tEnter index of array you wanna change: '))
    while oldNum > len(newArray) or oldNum < 1:
        oldNum = int(input('\t\tError. Enter existing index: '))
    newNum = int(input('\tEnter value of array you wanna set: '))

    newArray[oldNum - 1] = newNum
    return newArray


def changeNumByValue(array):
    newArray = array
    coincidence = False
    counter = 0

    oldNum = int(input('\tEnter value of array you wanna change: '))
    while not coincidence:
        for el in newArray:
            if oldNum == el:
                coincidence = True
        if not coincidence:
            oldNum = int(input('\t\tError. Enter existing value: '))
    newNum = int(input('\tEnter value of array you wanna set: '))

    for el in newArray:
        if el == oldNum:
            break
        else:
            counter += 1
    newArray.insert(counter, newNum)
    newArray.remove(oldNum)

    return newArray


print('\nEnter array from number, type number and click "Enter"\nTo stop adding elements write anything but number')
userArray = getArrayFromUser()

arr = changeElementsToInt(userArray)

print('\nYour array: ', arr)

choice = input('\nYou can change element of array by index (i) or by value (v)\n\tChoose your route: ')
while choice != 'i' and choice != 'v':
    choice = input('\t\tError. Enter i or v: ')

if choice == 'i':
    arr = changeNumByIndex(arr)
else:
    arr = changeNumByValue(arr)

print('\nNew array: ', arr)