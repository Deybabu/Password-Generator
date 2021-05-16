import string
import random

if __name__ == '__main__':
    s1=string.ascii_lowercase
    #print(s1)
    s2=string.ascii_uppercase
    s3=string.ascii_letters
    s4=string.digits
    sub=input("For what you need password?\n")
    plen=int(input("Enter password length for "+sub+":-"))
    s=[]
    s.extend(s1)
    s.extend(s2)
    s.extend(s3)
    s.extend(s4)
    print("Your password is:-")
    p="".join(random.sample(s,plen))
    file=open('password','a+')
    file.write("\n"+sub+":-"+p)
    file.close()
