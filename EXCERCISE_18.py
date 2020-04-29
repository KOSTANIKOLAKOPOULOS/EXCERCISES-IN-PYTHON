# inspector lekas
minutes = float(input("how many minutes you spoke"))
sms = int(input("how many sms"))
data = float(input("how much data"))
if minutes>1000:
	money_minutes = (minutes-1000)*0.0045
else:
	money_minutes = 0

if sms>1000:
    money_sms = (sms-1000)*0.1
else:
	money_sms = 0
if data>1000:
	money_data = (data-1000)*0.06
else:
	money_data = 0

total = 35+money_minutes+money_sms+money_data
print(" the total is {}".format(total))