v,c=input().split()
if (v=='P' and c=='R') or (v=='S' and c=='P') or (v=='R' and c=='S'):
    print("Vignesh")
elif(v=='R' and c=='P') or (v=='P' and c=='S') or (v=='S' and c=='R'):
    print("Charan")
else:
    print("NULL")
