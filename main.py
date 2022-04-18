from math import factorial
def pascal(n):
    list1=[]
    list1.append(1)
    if n<1:
        return list1
    if n==1:
        list1.append(1)
        return list1
    if n==2:
        list1.append(n)
        list1.append(1)
        return list1
    if n==3:
        list1.append(n)
        list1.append(n)
        list1.append(1)
        return list1
    if n>3 and n%2==0:
        list1.append(n)
        for m in range(2,n//2+1):
            k =int(factorial(n)/(factorial(m)*factorial(n-m)))
            list1.append(k)
        list2 = list1[::-1][1:]
        list1.extend(list2)
        return list1
    if n>3 and n%2!=0:
        list1.append(n)
        for m in range(2,n//2+1):
            k =int(factorial(n)/(factorial(m)*factorial(n-m)))
            list1.append(k)
        list2 = list1[::-1]
        list1.extend(list2)
        return list1


x = int(input())
print(pascal(x))
