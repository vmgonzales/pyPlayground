import math

def fibonacci(x):
    return x if (x <= 1) else (fibonacci(x-1) + fibonacci(x-2))


def gcd(x,y):
    while y != 0:
        (x,y) = (y, x % y)
    return x


def insertion_sort(a):    #sorts array a
    j=1
    while j < len(a):
        key = a[j]
        i = j - 1
        while (i >= 0 and a[i] > key):
            a[i+1] = a[i]
            i = i - 1
        a[i+1] = key
        j = j + 1
    return a


def isPalindrome(x): #tests whether the input number is a palindrome
    a = str(x)
    for i in range(0, int(math.ceil(float(len(str(x)))/2))):
      if a[i] != a[-1-i]:
        return False
      else:
        return True


def isPal(x): #a shorter way of testing for palindromes
    if str(x) == str(x)[::-1]:
        return True
    else:
        return False


def lcm(*values):
    values = set([abs(int(v)) for v in values])
    if values and 0 not in values:
        n = n0 = max(values)
        values.remove(n)
        while any(n % m for m in values):
            n += n0
        return n
    return 0