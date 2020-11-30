#(1)List down all the error types and check all the errors using a python program for all errors
    #DIVISION BY ZERO ERROR
try:
  print(100/0)
except ZeroDivisionError:
  print("division by zero error")

   # KEY ERROR
  try:
    d1={'a':'1','b':'2'}
    d1['c']
  except KeyError:
    print("key not found")

    #MODULE NOT FOUND ERROR
    try:
      import mod5
    except ModuleNotFoundError:
      print("module not found")

    #SYNTAX ERROR
    a,b=1,2
    print(a b)

  #(2) calculator
def calc():
         try:
           num1=int(input("enter the first number"))
           num2=int(input("enter the second number"))
           c=input("enter the operation: +,-,*,/")
           if c=='+':
             print(" num1 + num2 is:",num1+num2)
           elif c=='-':
            print(" num1 - num2 is:",num1-num2)
           elif c=='*':
            print(" num1 * num2 is:",num1*num2)
           elif c=='/':
             try:
              print(" num1 / num2 is:",num1/num2)
             except ZeroDivisionError:
               print("division by zero error")
         except ValueError:
           print("enter valid input")
calc()



#(3)print one message if the try block raises a NameError and another for other errors
try:
  print(name)
except NameError:
  print("Name is not defined")
except:
  print("other error has occured")




#(5)input inside the try catch block
try:
  num=int(input("enter the number"))
  print(num)
except:
  print("An exception occurred")
