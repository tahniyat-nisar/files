file_2=open("bank list.txt","w")
banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
i=0
while i<len(banks_list):
    file_2.write(banks_list[i])
    file_2.write("\n")
    i+=1
print(file_2)