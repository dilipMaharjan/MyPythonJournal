# Variables 
height=4.10 #height is a variable that holds actual value of height of a person.
weight=120
height_in_inches=4*12+10
bmi=(weight/height_in_inches**2) * 703 # height is converted to inches 
print(bmi)
print(type(bmi)) #givies the data type of the stored value, it prints float meaning it a real number(integer or fractional number representation)

print(2+4) #prints 6
print('ab'+'cd') # prints abcd

# Different data type = different behavior

## Python data types
'''
float - real numbers
int - integers
str - string , text
bool - True, False
'''

# Lists 
names=['John', ' Mathew', 'Mark']
print(names)
#sublist 
persons=[['John','23',5.5],['Mark','33',5.9]] # list can hold other lists
print(persons)

# Accessing List
print(names[0]) #list indexes starts from 0 
print(persons[0][0]) 
print(persons[0][1]) 

#Slicing 
numbers=[0,3,4,5,6,7,8,9,2,3,4,5,6,7,8]
print(numbers[3:5]) #print the values in the index 3 to 5  , inclusive lower index and exclusive upper index i.e value for 3 index is included while value for 5th index is excluded 
