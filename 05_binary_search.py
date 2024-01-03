# Project 05
# Binary Search

def search(list, n):
    l = 0
    u = len(list)
    pos = -1

    while (u >= l):
        mid = int((l+u)/2)      #for int value: (l+u)//2

        if list[mid] > n:
            u = mid - 1
        elif list[mid] < n:
            l = mid + 1
        else:
            pos = mid
            break

    return pos

list = [1,5,10,50,100,500,1000,5000,10000,50000,100000]
print("Here is the list -> ", list)

n = int(input("Enter the number you want to search in the list: "))

pos = search(list, n)

if pos == -1:
    print("Number", n ,"was not found in the list.")
else:
    print("Found the number", n ,"at index: ", pos)
