

'''
# Input==================
print('Menu:')
print('r: Regular')
print('s: Supervisor')
print('m: Manager')
employee_type=input()


print(employee_type)

print('Enter work day:')
day=input()

print('Enter work hours:')
hours=int(input())

print('employee_type:%s, day:%s, hours:%s' % ((employee_type, day, hours)))
# ======================
'''
(employee_type, day, hours) = ('s', 'mon', 12)

sal_dict = {
    'sun' : 30,
    'mon' : 30,
    'tue' : 30,
    'wed' : 30,
    'thu' : 30,
    'fri' : 42,
    'sat' : 42
}

coeff = {
    'r' : 1.0,
    's' : 1.2,
    'm' : 1.5
}

sal = hours*sal_dict[day]*coeff[employee_type]

print('employee_type:%s, day:%s, hours:%s' % ((employee_type, day, hours)))
print('The daily salary: %s' % sal)
