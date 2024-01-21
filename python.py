def saisir():
    ch1="Gaza"
    ch2="Palestine"
    ch=input("saisir un commentaire:")
    while not (ch!="" and ch.isdigit()==False and ch[len(ch)-1]=="!" and (ch.find(ch1)!=-1 or ch.find(ch2)!=-1)) :
        ch=input("saisir un commentaire:")
    return ch
        
def remplacer(ch):
    ch1="Palestine"
    ch2="Gaza"
    K=""
    if (ch.find(ch1)==-1):
        x=ch.find(ch2)
        if ch.find(ch1)!=-1:
            for i in range (x,x+len(ch1)):
                K=K+ch[i]+"*"
            L=ch.replace(ch[x,x+len(ch1)]-1,K)
        #else: 
            #for i in range (x,x+len(ch2)):
                #K=K+ch[i]+"*"
            #ch=ch.replace(ch[x,x+len(ch2)-1],K)
    print(L)


ch=saisir()
remplacer(ch)
