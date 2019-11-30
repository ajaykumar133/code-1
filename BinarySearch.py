pos = -1

def search(list, seach_element):
    lb = 0
    ub = len(list)-1

    while lb <= ub:
        mid = (lb + ub) // 2

        if list[mid] == search_element:
            globals()['pos'] = mid
            #print('found at ', pos + 1)
            return True

        else:
            if list[mid] < search_element:
                lb = mid + 1
            else:
                ub = mid - 1

    return False

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
search_element = int(input('enter the no. you want to search in list :'))

if search(list, search_element):
    print('founded at ',pos+1)
else:
    print('not in list')

