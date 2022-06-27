from functools import reduce
patient_dobs=['21-02-1981', '03-02-2006', '12-01-1950']
curr_yr=2022

def get_yob(dob):
    return int(dob.split('-')[2])

patient_yobs=list(map(get_yob,patient_dobs))
print(patient_yobs)

def get_age(yob):
    return curr_yr-yob

patient_ages=list(map(get_age,patient_yobs))
print(patient_ages)

def isadult(age):
    return age>=18


status=list(filter(isadult,patient_ages))

print(status)


average_age= reduce(lambda age1,age2: age1+age2,patient_ages)/len(patient_ages)
print(average_age)