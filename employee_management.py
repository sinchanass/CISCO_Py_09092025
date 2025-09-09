employees=[]
employee=('Banu',22,50000,True)
employees.append(employee)

employee=('Mahesh',46,40000.50,True)
employees.append(employee)

employee=('Vaishnavi',22,50000.75,True)
employees.append(employee)

print('after add all employees:',employees)
I=0
search='Vaishnavi'
index=-1
for emp in employees:
    if emp[0]==search:
        index = I
        break
    I+=1
if index==-1:
    print('Employee not found')
else:
    search_employee=employees[index]
    print(search_employee)
    salary=float(input('Salary:'))
    employee=(search_employee[0],search_employee[1],salary,search_employee[3])
    employees[index]=employee
print('after search and update:',employees)

employee=('David',50,200.75,True)
employees.append(employee)
print('after add Dravid:',employees)
employees.pop()
print('after delete Dravid:',employees)

position=1
employees.pop(position)
print('after delete Mahesh:',employees)
