file_f=open("f.txt","r")
file_g=open("g.txt","w")
file_h=open("h.txt","w")

for s in file_f.readlines():
    if int(s) % 2 ==0:
        print(s, file=file_g)
    else:
        print(s, file=file_h)

file_f.close()
file_g.close()
file_h.close()