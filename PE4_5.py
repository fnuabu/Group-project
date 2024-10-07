#6_A
n=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]   
print(n, n[:])     #print 1 through 10 twice.
print(n[0], n[-10])         #print 1 twice because of it says "n" two times
print(n[9], n[-1])          #print 10 twice 
print(n[3:])                # print the number from 4 to 10
print(n[:5])                # print 1 to 5
print(n[-5:-1])             # print 6 to 9 
print(n[4:8])               # print 5 to 8
#B
print(n[-1] + n[-2])        # prints 19 cause of addition sign
print(n[9] - n[1])          # prints 8 because it subtracted 
print(n[2] * n[5])          # multipy 
print(n[8] / n[2])          # division operator
print(len(n), n[:len(n)], sep = '\n')  # prints 10
print(min(n), max(n), type(n), sep = '\t') # prints 1 through 10

#C 
n[0], n[9] = "apple", 'cherry'
n.insert(3, "banana")
n.insert(-1, "kiwi")
print(n) # It prints ['apple', 2, 3, 'banana', 4, 5, 6, 7, 8, 9, 'kiwi', 'cherry']
print(f"Do you like {n[0].upper()} or {n[-1].upper()}?") # it prints do u like APPLE or CHERRY and note that apple and cheery are in upper letter.

#D 
n.append(-11)
n.append("orange")
n[0], n[1] = n[-1], n[-2]
print(n+n) #['orange', -11, 3, 'banana', 4, 5, 6, 7, 8, 9, 'kiwi', 'cherry', -11, 'orange', 'orange', 
print(n*2) #-11, 3, 'banana', 4, 5, 6, 7, 8, 9, 'kiwi', 'cherry', -11, 'orange']

#E
item1 = n.pop(0)
print(f"{item1} is removed.") #orrange is removed
item2 = n.pop()
print(f"{item2} is removed.") # again orange rmoved
print('n = ', n) #n =  [-11, 3, 'banana', 4, 5, 6, 7, 8, 9, 'kiwi', 'cherry', -11]
print(f'Removed items: {item1} & {item2}') #Removed items: orange & orange

#F
n.insert(6, 'pear')
del n[-1]
del n[0]
print(n) #[3, 'banana', 4, 5, 6, 'pear', 7, 8, 9, 'kiwi', 'cherry']
n.remove("pear")
n.remove(6)
print('n = ', n) #n =  [3, 'banana', 4, 5, 7, 8, 9, 'kiwi', 'cherry']
n.clear()
print(f'n = {n}') #n = []

#G
fruits = ['kiwi', 'pear', 'orange', 'apple', 'cherry'] 
fruits.sort()
print(fruits[0], fruits[-1]) # just prints apple and pear
fruits.sort(reverse=True)
print(fruits[0], fruits[-1]) # prints apple, pear

#H
fruits = ['kiwi', 'pear', 'orange', 'apple', 'cherry'] 
print(sorted(fruits)) # change the places of fruits.
print(fruits[0], fruits[-1]) # prints Kiwi and cherry
print(sorted(fruits, reverse=True)) #print the same thing but sorted the fruits.
print(fruits[0], fruits[-1]) #prints kiwi, cherry
