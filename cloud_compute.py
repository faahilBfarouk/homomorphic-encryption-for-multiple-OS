cipher=0
e=2 ##exponent value stored in database 

#attempt at file input for Review 3


with open('/media/sf_Shared_Docs/output.txt','r+') as f:
    data=int(f.read())
    cipher=data

cipher_comp=cipher**e

print("Data Recieved By Cloud: ", cipher)
print("Data computed And Send: ",cipher_comp)
out=open('/media/sf_Shared_Docs/result.txt','w')
out.write(str(cipher_comp))
out.close()
