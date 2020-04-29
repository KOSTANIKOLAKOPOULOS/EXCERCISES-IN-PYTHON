'''
++++++++++++++++Άσκηση 9.4++++++++++++++++++
Παγια χρέωση : 35 €
Παροχές:
Λεπτά ομιλίας 1000 sms 1000 MB 1000
Extra χρέωση:
0,0045€/ λεπτό ομιλίας
0.10€/sms
0.06€/ΜΒ
'''
#Έλεγχος ακρίβειας εισόδου - Check data input
def insertdata():
    while True:
        x = input ('>')
        try :
            a = int(x)
            break
        except:
            print('Λάθος εισαγωγή .Παρακαλώ δώστε αριθμό')
            continue
    return a

#Υπολογισμός επιπρόσθετης χρέωσης - extra charge calculation
def extra_calc(i):
    charge = 0
    print(f"Παρακαλώ πληκτρολόγησε την μηνιαία κατανάλωση \n Για  {i[0]}:")
    amount = insertdata()
    charged_amount = amount - i[1]
    if charged_amount >=0:
        charge+= charged_amount * i[2]
        print(f"Υπερβήκατε το όριο κατά {charged_amount} {i[0]} \nσυναιπώς υπάρχει επιπλεόν χρέωση {charge} €")
    else:
        print ("Δέν υπαρχει extra χρέωση.")
    return charge

#Main
print('\tΥπολογισμός μηνιαίας οφειλής\t')

#Data Values
extraCharge = 0
fixed = 35
chargeList = [('λεπτά ομιλίας',1000,0.0045),('sms',1000,0.10),('MB',1000,0.06)]

for i in chargeList:
    extraCharge+=extra_calc(i)

payment = extraCharge +fixed
print("Η συνολική οφειλή ειναι : {:.2f} €".format(payment))








input("Press enter to exit")
