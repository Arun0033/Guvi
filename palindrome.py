l=str(input())
if(len(l)<=1000):
   rev=l[::-1]
   if(l == rev):
      print("yes")
   else:
       print("no")
