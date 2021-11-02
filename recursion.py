'''
implement a recursive function that cycles a list n times. 
cycling a list involves taking an element off the end of the list and adding it to the beginning. 
cycling abcde once returns eabcd. cycling it twice returns deabc. 
'''

def cycle(lst, n):
    if n == 0: # if there is no n
        return lst
    elif n > len(lst): # if n is greater than the length of the list(10)
        n = str(n)
        n = int(n[len(n)-1])
        print("number of shifts:", n)
        return cycle(lst, n)
    elif n < 0: # if n is a negative number
        n = str(n)
        n = int(n[len(n)-1])  * -1
        n = len(lst) + n
        print("number of shifts:", n)
        return cycle(lst, n)
    else:
        lst.insert(0, lst.pop())
        return cycle(lst, n - 1)

def test():
  lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  assert cycle(lst, 3) == [8,9,10,1,2,3,4,5,6,7]
  print(cycle(lst, 23452459))
test()
