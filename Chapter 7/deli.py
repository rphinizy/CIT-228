sandwich_orders=["Pastrami","Pastrami","BLT","French Dip","Reuben","Turkey","Pastrami","Club","PB & J"]
finished_sandwiches=[]

for s in sandwich_orders:
    print("I have made a",s ,"sandwich")
    finished_sandwiches.append(s)
print("********************")
print("COMPLETED ORDERS:")
for f in finished_sandwiches:
    print("\t\t",f,"\n")
print("********************")
print()
print("---------------------------")
print("SORRY! We are out of:")
print("\t\tPASTRAMI\n")
print("---------------------------")

finished_sandwiches.clear()

while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

for s in sandwich_orders:
    print("I have made a",s ,"sandwich")
    finished_sandwiches.append(s)
print("--------------------------")
print("COMPLETED ORDERS:")
for f in finished_sandwiches:
    print("\t\t",f,"\n")
print("--------------------------")


