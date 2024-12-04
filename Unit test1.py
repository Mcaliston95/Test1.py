salary = float(input("enter salary:"))
numdependents = int(input("number of dependents:"))

statetax = salary * .065
federaltax = salary * .28
dependentDeduction = .025 * salary * numdependents
totalwithholding = statetax + federaltax + dependentDeduction
takehomepay= salary - totalwithholding

print("statetax :$", statetax)
print("federaltax :$", federaltax)
print("dependents: $", numdependents)
print("takehomepay: $", takehomepay)