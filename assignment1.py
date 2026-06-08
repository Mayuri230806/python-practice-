#Create a string variable with your name and perform the following 
# operations: 
# o Print the first character 
# o Print the last character 
# o Print the length of the string 
# o Convert the string to uppercase 
# o Convert the string to lowercase 
# o Reverse the string using slicing 


name="mayuri"
print("the first character of string :-",name[0])  #Print the first character
print("the last character of string ",name[-1])    #print the last character


name="mayuri"
print("the length of string is :-",len(name))    #length of string


name="mayuri"
upper_case=name.upper()
print("the upper case of string is :-",upper_case) # upper case


name="MAYURI"
lower_case=name.lower()
print("the lower case of string is:-",lower_case)   #lower case


name="mayuri"
print(name[::-1])    #reverse using slicing 




# Write a Python program to perform string slicing on a given string: 
# o Print the first four characters 
# o Print characters from index 2 to 5 
# o Print the complete string in reverse order



name="mayuri"
print("the first four character are:-",name[:4])   #perform string slicing on a given string

print("the char at index  2 to 5 ",name[2:6])  #Print characters from index 2 to 5 

print(name[::-1])    # print string in reverse order



# Create a list containing numbers and perform the following operations: 
# o Add an element using append() 
# o Insert an element at a specific position 
# o Remove an element using remove() 
# o Delete the last element using pop() 
# o Reverse the list 
# o Sort the list
# o Find the length of the list 
# o Count the occurrence of an element 




lst=[1,2,3,4,7,9]
lst.append(5)
print(lst)      # Add an element using append() 


lst=[1,2,3,4,7,9]
lst.insert(3,8)
print(lst)  # Insert an element at a specific position


lst=[1,2,3,4,7,9]
lst.remove(3)
print(lst)    #Remove an element using remove()


lst=[1,2,3,4,7,9]
lst.pop(5)
print(lst)  #Delete the last element using pop() 


lst=[1,2,3,4,7,9]
lst.sort()
print(lst)   #Sort the list



lst=[1,2,3,4,7,9]
lst.reverse()
print(lst)      # Reverse the list 


lst=[1,2,3,4,7,9]
print("the length of lst:-",lst)     #length of list


lst=[1,2,3,4,7,9] 
print(lst.count(4))          #count of list
   



#  Create a tuple containing 5 subjects. Perform the following operations: 
# o Print the first element 
# o Print the last element 
# o Print the length of the tuple 
# o Print elements using slicing 
# o Find the maximum, minimum, and sum of numerical tuple elements




subject=("math","science","physics","chem","english")   

print("the first element of subject:-",subject[0])    #Print the first element
print("the first element of subject:-",subject[-1])     # Print the last element
print("the len of subject",len(subject))                 #Print the length of the tuple
print("the slicing is :-",subject[1:4])                   # Print elements using slicing 


print("Maximum:", max(subject))   
print("Minimum:", min(subject))   #print min max element in subject name dict


numbers = (10, 20, 30, 40, 50)

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))     # maximum, minimum, and sum of numerical tuple elements
print("Sum:", sum(numbers))


# Write a Python program to demonstrate tuple packing and unpacking. Create 
# a tuple of four values and assign them to four separate variables. 



student = ("Mayuri", 19, "B.Tech", "CS")   

print("Packed Tuple:", student)      # Tuple Packing


name, age, course, branch = student

print("Name:", name)    # Tuple Unpacking
print("Age:", age)
print("Course:", course)
print("Branch:", branch)





# Perform the following operations: 
# o Print all keys 
# o Print all values 
# o Print all items 
# o Update the Address 
# o Add a new key called "Branch" 



dict={   "Name":"mayuri", 
          "Age" :"19",
          "Course" :"btech",
          "Address" : "jaipur"
     } 

print("the key of dict is:-",dict.keys())     # Print all keys 
print("the key of dict is:-",dict.values())   #Print all values
print("the key of dict is:-",dict.items())     #Print all item
dict.update({"Address": "Kanota"})             #Update the Address 
print("Updated dictionary:", dict)

dict["Branch"] = "Computer Science"              #Add a new key called "Branch" 
print(dict)





# Print the value 5 using indexing. 



lst=[1, 2, 3, 4, [2, 5], 7]
print("The required element is:", lst[4][1])



# Create a dictionary and demonstrate the use of: 
# o get() 
# o keys() 
# o values() 
# o items() 




employee={ "name":"shyam",
            "age":"24",
            "salary":"20000",
            "department":"finance",
            "address":"ajmer"
}

print(employee.get("name"))    #use of get() it is use to find the value of key 
print(employee.keys())         #print all the keys which is in the employee
print(employee.values())        #print all the values which is in employee
print(employee.items())           #prit all item which is in employee




# Create a copy of a list using copy() and print both the original and copied lists.


num = [10, 20, 30, 40, 50]
copied_list = num.copy()

print("Original List:", num)     # Original List
print("Copied List:", copied_list)    #copied list



#  Write a Python program to demonstrate type casting: 
# o Take two numbers as input from the user 
# o Convert them to integers 
# o Print their multiplication




num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

num1 = int(num1)
num2 = int(num2)

print("Multiplication =", num1 * num2)



#  Write a Python program to take a number as input from the user and: 
# o Add 10 using the += operator 
# o Print the updated value 


num = int(input("Enter a number: "))
num += 20
print("Updated value =", num)



