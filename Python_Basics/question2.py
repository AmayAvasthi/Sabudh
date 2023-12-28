import string
a = string.ascii_lowercase
alphabets = list(a)
#print(alphabets)
code = input("Enter your code: ")
skip = int(input("Enter the skip: "))
result=[]
ls = []
for i in code:
    #print(alphabets.index(i))
    ls.append(alphabets.index(i))

#print(ls)


ls = [*map(lambda x: x - skip, ls)]
#print(ls)

for i in ls:
    #print(alphabets[i])
    result.append(alphabets[i])
    
print(result)