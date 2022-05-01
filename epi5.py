## Solutions to some exercises from the Elements of Programming Interviews
## (Aziz, Lee, and Prakash 2014)

# Problem 6.1: Dutch National Flag
def dutch_national_flag(a, index):
    length = len(a)
    print ("length: ", length)
    
    pivot = a[index]
    smaller, equal, larger = 0, 0, length - 1
    
    while (equal <= larger):
        if a[equal] < pivot:
            a[smaller], a[equal] = a[equal], a[smaller]
            smaller += 1
            equal += 1
        elif a[equal] == pivot:
            equal += 1
        else:
            a[equal], a[larger] = a[larger], a[equal]
            larger -= 1
    return a

#test_array = [5, 6, 5, 4, 4, 3, 2, 1, 4, 5, 2]
#print (dutch_national_flag(test_array, 6))
