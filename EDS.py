1.2.1 Pass or Fail
n=int(input())
marks=list(map(int,input().split()))
agg=(sum(marks)/n)*100
if all(mark>40 for mark in marks):
agg=sum(marks)/n
print(f"Aggregate Percentage: {agg:.2f}")
if agg>=75:
print("Grade: Distinction")
elif (agg>=60 and agg<75):
print("Grade: First Division")
elif (agg>=50 and agg<60):
print("Grade: Second Second")
elif (agg>=40 and agg<50):
print("Grade: Thrid Division")
else:
print("Fail")
1.2.2 Fibonacci series using Recursive Fuction.
def fib(n):
if n<=1:
return n
else:
return fib(n-1)+fib(n-2)
n=int(input("Enter terms for Fibonacci series: "))
for i in range (n):
print(fib(i),end=" ")
1.2.3 Pattern 1.
n=int(input())
i=0
j=0
for i in range(n):
for j in range(i+1):
print("* ",end='')
print()
1.2.4 Pattern 2 .
n=int(input())
i=0
j=0
for i in range(1,n+1):
for j in range(1,i+1):
print(j,"",end='')
print()
