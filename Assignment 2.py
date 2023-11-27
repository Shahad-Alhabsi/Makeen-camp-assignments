"""
Shahad AlHabsi
Assignment2: Lists

1) Given the definition 
Values = [0, 0, 0, 0, 0, 0, 0]
Write statements to put the integer 10 into the elements of list values with the lowest 
and the highest valid index.
"""
Values = [0, 0, 0, 0, 0, 0, 0]
Values[0] =  10 # 0 is always the lowes index value
Values[len(Values)-1] = 10 # the last value is the length of the list -1
print(Values)



"""
2) Reverse the following list without using the reverse() function:
[6, 3, 8, 1, 7]
"""
# This could be solve in many ways
# Using a loop:
List = [6, 3, 8, 1, 7]
reversed_list = []
for i in range(len(List)-1, -1,-1):
    reversed_list.append(List[i])   
print(reversed_list)

# using slicing
print(List[::-1])


"""
3) If you have the following list as an input:
[‘red’, ‘yellow’, ‘pink’, ‘black’]
And the following list is the output of it:
[‘red’, ‘purple’, ‘yellow’, ’Black’, ‘green’]
Find how we got the output.
"""
List = ['red', 'yellow', 'pink', 'black']
List.insert(1,'purple') #insert 'purp'e in the index of 'yellow' --> index 1
List.remove('pink') # remove the element 'pink'
List[3] = 'Black' #change the element 'black' be adding 'Black' in its index
List.append('green') #append 'green' at the end
print(List)



"""
4) fruits = [‘orange’, ‘apple’, ‘pear’, ‘banana’, ‘kiwi’, ‘apple’, ‘banana’]
fruits.count(“apple”)
fruits.count(“strawberry”)
fruits.index(“banana”)
fruits.index(“banana”, 4)
fruits.reverse()
fruits.append(“grape”)
fruits.sort()
fruits.pop()
"""
# output: fruits list --> ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange']

# count() and index() functions do not change anything in the lidt
# reverse() function reverses the list --> ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
# after appending "grape" --> ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
# after sorting with sort() in alphabetical order  --> ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
# pop() pops out the last element in the list ('peer') ---> ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange']



"""
5) input: [23, 54, 76, 12, 90]
output: 23 | 54 | 76 | 12 | 90
"""
inp = [23, 54, 76, 12, 90]
out = ""
for i in inp:
    out += str(str(i)+" | ")
print(out[:len(out)-2]) # -2 becaouse we don't want the "|" and the spaces at the end



"""
6) write a loop that counts how many elements in a list is equal to zero.
"""
def countZero(lst):
    count = 0
    for i in lst:
        if i == 0:
            count += 1
    return count

try:
    elements = input("Enter numbers to form a list: ")
    List = [float(i) for i in elements.split()]
    print("In the list there are ",countZero(List), " elements equal to zero")
except:
    print("Invalisd input")



"""
7) Write the output of the following:
d = “a*hj”
list(d)
"""
# the output ---> ['a', '*', 'h', 'j']
# because the function list() is going to save each element of the string as en element in a list



"""
8) What is the output of the following:
b= [‘p’, ‘r’, ‘a’, ‘c’, ‘t’, ‘i’, ‘c’, ‘e’]
for i in b:
 print(i, end=”?”)
"""
# the output --> p?r?a?c?t?i?c?e?
# because the loop is printing each element followed by "?" without scape and in the same line



"""
9) If you have the following:
b = “Hello World”
a = list(b)
print(a)
print(len(a))
print(a[1:11])
print(a[-2,-5,-1])
print(a[::2])
print(a[:4])
print(a[4:])
"""
b = "Hello World"
a = list(b)
# print(a)  a list of the characters of the string b --> ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
# print(len(a))  --> 11 elements
# print(a[1:11])  --> without the first element (a[0]) --> ['e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
# # print(a[-2,-5,-1]) -->  Error: we shoud use the ":" for slicing not ","
# print(a[::2]) -->  jump 2 places in the list (print one and leave one)--> ['H', 'l', 'o', 'W', 'r', 'd']
# print(a[:4])  --> fron index 0 to 3 (first 4 elements) --> ['H', 'e', 'l', 'l']
# print(a[4:]) --> from the element in index 4 to the end of the list --> ['o', ' ', 'W', 'o', 'r', 'l', 'd']


"""
10) Write a Python program to find the list of words that are longer than n from a given 
list of words.
Hint: take n from user
"""
def check_words(lst, n):
        out_list = []
        for i in lst:
            if len(i) > n:
                out_list.append(i)
        return out_list
        

try:
    n = int(input("Enter n: "))
    words = input("Enter words separated by a aspace to form a list ")
    list_of_words = [i for i in words.split()]
    print("list of words that are longer than ", n, " --> ",check_words(list_of_words, n))
except:
    print("Invalid input")
    
         
         
