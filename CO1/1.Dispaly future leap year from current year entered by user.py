cyear=int(input("Enter current year:"))
fyear=int(input("Enter final year:"))
for cyear in range(cyear,fyear):
  if(cyear%400==0)or(cyear%4==0)and(cyear%100!=0):
    print(cyear,"is a leap year")
  else:
    print(cyear,"is not a leap year")
