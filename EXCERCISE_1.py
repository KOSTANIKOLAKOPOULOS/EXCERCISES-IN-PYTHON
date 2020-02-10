#INSPECTOR LEKAS
lista = []
lista1 = []
lista2 = []
negative_numbers=[]
positive_numbers=[]
i,k = 0,0

while True:
    k+=1
    number=input("give the number or stop")
    if number=="stop":
        break
    else:
        lista.append(int(number))
    if k==5 :
        break    
y=sum(lista)/k 
print(y)       
for i in lista:
    if i<11:
        lista1.append(i)
    if  i<0:
        negative_numbers.append(i)
    if i>0:
         positive_numbers.append(i)
print(len(lista1))
for j in lista:
    if j<(y/2):
     lista2.append(j)
print(len(lista2))  
print(len(negative_numbers))
print(len(positive_numbers))