a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

c = min(a,b)
ls = []
#print(c)

for i in range (1 , c+1):
    if a%i == 0 and b%i == 0:
        #print(i)
        ls.append(i)


d = max(ls)

print(f"The highest common divisor for {a} and {b} is {d}")    