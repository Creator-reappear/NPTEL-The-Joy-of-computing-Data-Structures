 L=int(input())

def prime(L):
    if (L<=1):
        print("False")
    else:
        if(L==2):
            print("True")
        else: 
            if(L%2==0):
                print("False")
            else:
                if(L%2!=0):
                    print("True")

prime(L)
