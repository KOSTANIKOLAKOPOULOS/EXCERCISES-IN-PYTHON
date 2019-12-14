#INSPECTOR LEKAS
lista = []
lista1 = []
lista2 = []
negative_numbers=[]
positive_numbers=[]
i,k = 0,0
'''
def add():
    k=0
    sum=0
    for j in lista:
        sum=int(j)+sum
        k+=1
        addition=sum/k
    return addition
print(add()) '''
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