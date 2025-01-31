ccn= input("Enter your credit card number: ")

ccn= ccn.replace("-", "")
ccn= ccn.replace(" ", "")

odd_sum = 0
even_sum = 0

for x in ccn[::2]:
    odd_sum+=int(x)

for x in ccn[::-2]:

    if int(x)*2>=10:
       even_sum+= ((int(x)*2)%10)+1
    else:
        even_sum += int(x) * 2

total= odd_sum+even_sum

if total%10==0:
    print("Valid")
else:
    print("Invalid")

