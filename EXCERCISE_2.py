#inspector lekas
k,lista=0,[]
while True:
    matrix = input("give the element of matrix")
    if matrix=="stop":
        break
    else:
        lista.append(matrix)
y = min(lista)
print("minimum",y)
print(lista.index(y))

for i in lista:
    
    while lista.count(i)>1:
        k+=1
        lista.remove(i)
        print(lista.index(y)+k)
