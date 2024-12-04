salary = float(input("please enter the your salary:"))
numdependents = int(input("enter number of numdependents:"))

statetax = salary * .065
federaltax = salary *.28
dependentDeduction = .025 * salary * numdependents
totalwithholding = statetax + federaltax + dependentDeduction
takehomepay = salary + totalwithholding

print("statetax :$", statetax)
print("federaltax :$", federaltax)
print("dependents: $", numdependents)
print("salary:$", salary)
print("take-homepy:$",takehomepay)
