  #Sign your name:________________

'''
 1. Make the following program work.
   '''  
     print("This program takes three numbers and returns the sum.")
     total = 0

     for i in range(3):
         x = input("Enter a number: ")
         total = total + i
     print("The total is:", x)
  


'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive.
'''
    print("This program prints the even numbers from 2 to 100,inclusive")
    for i in range(2,102,2):
        print(i , end =" ")
    print()





'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop.
''' 
no = 10
while(no>=0):
  print(no,end = " ")
  no-=1
print('Blast off!')






'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive).
'''
import random 
no = random.randrange(0, 10)
print(no,end = " ")
while(no<10):
  no = random.randrange(no+1, 11)
  print(no,end = " ")
  




'''
  5. Write a Python program that will:
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.   
'''
list = list(map(int,input("\nEnter 7 numbers : ").strip().split()))[:7]
print("Sum of numbers is ",sum(list))
z=0
n=0
p =0 
for num in list:
    if num ==0:
      z+=1
    elif num >  0:
      p+=1
    else :
      n+=1
print("count of entries equal to zero =",z)
print("count of negative entries = ",p)
print("count of negative entries = ",n)
