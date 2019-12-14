#inspector lekas
lista=[]
while True:
    matrix = input("give the element of matrix")
    if matrix=="stop":
        break
    else:
        lista.append(matrix)
y = min(lista)
print("minimum",y)
print(lista.index(y))