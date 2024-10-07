JULIANS WORK
#PE4_1.py
#determining the output displayed
print("Python")
print("Python"[0])
print("Python"[-1])
print("Python"[:])
print()
str = "Python 123"
print(str)
print(str[0])
print(str[-1])
print(str[:])
print()
strNum = "0, 1, 2, 3, 4, 5, 6, 7, 8, 9"
print(strNum[1], strNum[-1], len(strNum))
print(strNum[:len(strNum)])
print(strNum[1]+strNum[-3])
print()
print()


#PE4_2.py
#Creating an empty list
n = []

#Add 2 and 4 into the list
n.append(2)
n.append(4)

print(n)  # Output: [2, 4]

#Adding 0, 1 and 3 in proper order.
n.extend([0, 1, 3])
n.sort()  # Sort the list to maintain order

print(n)  # Output: [0, 1, 2, 3, 4]

#Adding 5 in proper order.
n.append(5)
n.sort()  # Sort the list to maintain order

print(n)  # Output: [0, 1, 2, 3, 4, 5]

#Removing 0 from the list.
n.remove(0)

print(n)  # Output: [1, 2, 3, 4, 5]

#Removing and printing 2 from the list.
removed_2 = n.pop(n.index(2))

print(n)  # Output: [1, 3, 4, 5]

#Removing and printing 4 from the list.
removed_4 = n.pop(n.index(4))
print(removed_2)  # Output: 4

print(n)  # Output: [1, 3, 5]
print(removed_4)
print()
#Adding all the removed numbers and print the sum.
removed_sum = 0 + removed_2 + removed_4  # 0 (removed) + 2 + 4
print("sum of all removed numbers = ",removed_sum)  # Output: 6
print()
#Changing the first item to 100 and last item to 9.9.
n[0] = 100
n[-1] = 9.9

#Copying the list n to a newNum list.
newNum = n.copy()

n.clear()

#Printing the original list (newNum), n, and the newNum list.
print(newNum)  # Output: Original list (newNum): [100, 3, 9.9]
print()
print("Oringinal list :", n)                # Output: Cleared list n: []
print("New list = ",newNum)
#Deleting the list n.
del n
print()
print()



#PE4_3.py
#Creating a list containing the names of my current courses.
courses = ["ENGL101", "SOCY101", "ET710", "History", "ET574"]

#Printing the list of courses.
print("List of courses:", courses)
print("I am taking", len(courses), "courses")
print(courses[0], courses[-1])
print(courses[:4])
print(courses[-4:])
print(courses[1:-1])
print()
print()


#PE4_5.py
#Creating an empty list named grades.
grades = []

grades.append(75)
grades.append(82)
grades.append(58)  # Failing grade
grades.append(90)
grades.append(45)  # Failing grade

#Printing the current list.
print("Current list:", grades)

total = 0
for i in range(len(grades)):
    total += grades[i]

average = total / len(grades)

print("Average: {:.2f}".format(average))

#Using a loop
for grade in grades[:]:  # Create a copy of the list to avoid modifying while iterating
    if grade < 60:
        grades.remove(grade)

#Printing the updated list.
print("Updated list:", grades)

#Using list comprehension
grades = [grade for grade in grades if grade >= 60]

if len(grades) > 0:  # Check if there are grades left to avoid division by zero
    new_average = sum(grades) / len(grades)
    print("Updated average: {:.3f}".format(new_average))
else:
    print("No passing grades left.")
print()
print()


#Using input() to prompt and request a full name.
full_name = input("Enter the full name of your favorite US president:\n")

name_parts = full_name.split()

first_name = name_parts[0]
last_name = name_parts[-1]
print("First Name:", first_name.capitalize())
print("Last Name:", last_name.capitalize())


NOTE: HAVE TO EDIT THE NAMES











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



#PE6_7_A
myList = ['apple','banana','cherry']
print(myList[2])

#B
print(myList[-1:-4:-1])

#C 
word = 'sea'
word[0] = 'p' + word[1 :]
print(word)

#D
n = [1, "two", 'three', 4]
n = [str(i) for i in n] # converts all element to str
print(" ".join(n))
