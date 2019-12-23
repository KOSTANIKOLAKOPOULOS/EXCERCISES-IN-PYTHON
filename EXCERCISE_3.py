#inspector lekas
lista=[]
while True:
    name = input("give elements")
    if name=="stop":
        break
    else:
    	lista.append(name)
print(lista)    	    
y=max(lista)
print(y)
lista.remove(y)
x=max(lista)
print(x) 
print(lista)       