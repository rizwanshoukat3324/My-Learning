#every name in the list is called index 
students=["Rizwan","Shoukat","Imran","Shaban"]
print(students[2])
print(students[0])
print(students[1])


for student in students:
    print(student)

#where len is an function use for knowing about the lengthand i+1 is use for giving serial no to index
for i in range (len(students)):
    print(i+1, students)

#where below is dictionary 
stodent={'Name':'Rizwan',
         'Name':'Imran',
         'Name':'Shaban',
         'Name':'Ramzan'}

print(stodent['Name'])


for student in stodent:
    print(student, stodent[student])


#where below is the dictionary with multiple Entries like Name City and Profesion
#where 'NOne' function is represnt officially the absence of a value
studant=[
    {'Name':'Rizwan','City':'Lahore','Profession':'AI Engineer'},
    {'Name':'Imran','City':'Islamabad',"Profession":'Mechanical Engineer'},
    {'Name':'Shaban','City':'Karachi','Profession':'Punjab Police'},
    {'Name':'Ramzan','City':'Jehlum','Profession':None}
]


for student in studant:
    print(student["Name"], student["Profession"], student["City"], sep=", ")


