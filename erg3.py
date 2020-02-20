#python 3.6.8
d={}
i=0
#asking if there is a product
while True:
    answer=input("Do you have a product?")
    if (answer=="yes"):
        #asking for product details
        name=input("Give product name\t")
        price=input("give price\t")
        tax=input("give tax\t")
        #putting product details given in a dictionary item (i)
        d[i]={"product_name":name,"product_price":int(price),"product_tax":int(tax)}
        i=i+1
    else:
        break

sum=0
#calculating sum
for i in d:
    sum=sum+d[i]["product_price"]+(d[i]["product_price"]*d[i]["product_tax"]/100)

if sum!=0:
    print("The sum is:")
    print(sum)
print("end of transaction")