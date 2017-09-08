#I am checking zip codes for Chicago area
listing='Anderson, Maren,60707\n'
listing+='Anderson, Marie,60707\n'
listing+='Hansen, Thor,60707\n'
listing+='Primo, Alex,60610\n'
file=open('newexample.txt','w')
file.write(listing)
file.close()
file=open('newexample.txt','r')
for line in file:
    print( line , end='')
file.close()
