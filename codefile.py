#I am checking zip codes for Chicago area
listing='Anderson, Maren,60707\n'
listing+='Rogers, Marie,60707\n'
listing+='Hansen, Thor,60707\n'
listing+='Primo, Alex,60610\n'
listing+='Roberts, Walter,60610\n'
listing+='Olsen, Harry,60635\n'
file=open('newexample.txt','w')
file.write(listing)
file.close()
file=open('newexample.txt','r')
for line in file:
    fields=line.split(",")
    Lname = fields[0]
    Fname = fields[1]
    zip = fields[2]
    #print the data for review
    print(Lname + "," + Fname + " " + zip)
file.close()
