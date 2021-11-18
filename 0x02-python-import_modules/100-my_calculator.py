#!/usr/bin/python3
if __name__ == "__main__":
 from calculator_1 import add, sub, mul, div
import sys
m=len(sys.argv)-1
if m == 3:
  a=int(sys.argv[1])
  b=int(sys.argv[3])
  if sys.argv[2]=='+':
     print(a,"+", b, "=",add(a,b))
  elif sys.argv[2]=='-':
     print(a, "-", b ,"=",sub(a,b))
  elif sys.argv[2]=='*':
     print(a,"*" ,b ,"=",mul(a,b))
  elif sys.argv[2]=='/':
     print(a,"/", b,"=",div(a,b))
  else:
     print("Unknown operator. Available operators: +, -, *,/" )
     sys.exit(1)
else:
   print("Usage:./100-my_calculator.py <a> <operator> <b>()")
   sys.exit(1)
