#reversing the stringg without using slice
s='syam'
rev="".join(reversed(s))
print(rev)
#2nd way using 2 pointers + list
r="surya"
revv=list(r)
l,r=0,len(revv)-1
while(l<r):
    revv[l],revv[r]=revv[r],revv[l]
    l+=1
    r-=1
revv="".join(revv)
print(revv)