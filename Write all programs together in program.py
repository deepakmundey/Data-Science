#Develop by : 	Mr. Gajendra Sharma 
#WhatsApp   : 	9810301034
#Book Name  :	PlayWithPython (DotPyEdu) >> www.amazon.in
#Email	    :	pgt.csip.gajendra@gmail.com
#Address    :	Ghaziabad (UP)
#Program    :	Write all programs together in program
import glob
files=glob.glob("*.py")
print(files)
i=0
s=""
for file in files:
    f=open(file,"r")
    s1=f.read()
    s=s+"#*************"+file+"****************\n"+s1+"\n"
    i=i+1
f1=open("Allinone.py","w")
f1.write(s)
f1.close()
f.close()
print("DONE")
