'''Assignment No: 3
To accept students five courses marks and compute his/her result.
Student is passing if he/she scores marks equal to and above 40 in each course.
If student scores aggregate greater than 75%, then the grade is distinction.
If aggregate is 60>= and <75 then the grade if first division.
If aggregate is 50>= and <60, then the grade is second division.
If aggregate is 40>= and <50, then the grade is third division.
'''

class Student:    # creation of class

 def __init__(self):  #  __init__() function to assign values to object properties
  self.marks = []
  self.passed = True

 def input(self):   # input function is defined using the def keyword. 
          #Self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
  try:
   for i in range(5):
    mark = float(input("Marks: "))
    self.marks.append(mark)
    if mark < 40:
     self.passed = False
  except:
   print("Enter marks in digits.")

 def grade(self):   #grade function is defined
  if self.passed:
   average = sum(self.marks)/5
   print("Average=",average )
   if average>=75 and average<100:
    print("Distinction")
   elif average >= 60 and average<75:
    print("First Division")
   elif average >= 50 and average<60:
    print("Second Division")
   else: 
    print("Third Division")
  else:
   print("Failed")

if __name__ == '__main__':
 student = Student()
 student.input()   # function calling
 student.grade()
