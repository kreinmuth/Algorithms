

#How it works, the algorithm searchs through a list one by one to find a matching variable


def linearsearch(string_list, x):
   for i in range(len(string_list)): #Loops through the list from 0 t the max list length, put reveresed in front range to go in opposite order, can use all range functions to change how it searches
      if string_list[i] == x:
         return i #Returns the location of the matching variable
   return -1# This is the value the function will return tht can be used to compare it
string_list = ['t','u','t','o','r','i','a','l']
x = 'a'

object = linearsearch(string_list,x) #Converting the function into an object to then compare if it found a match or not.

if object == -1:
   print("Element not found in List")
else:
   print("element found at index " + str(linearsearch(string_list, x)))

#Test


