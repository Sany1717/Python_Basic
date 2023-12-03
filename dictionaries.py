StudentInfo = {
    "Rubama":{
        "Name":"Rubama Chowdhury",
        "Lcation":"Chadpur",
        "Study":"Computer Science & Engineer",
        "id":20230000000034,
        "Number":"01406573702"
    },

        "Sany": {
            "Name": "Mahmudur Rahman Sany",
            "Location": "Kishoregonj",
            "study": "Computer Science & Engineer",
            "id": 2022000000027,
            "Number": "01317970640"
    },

          "Year":1928



}
print(StudentInfo)
print(StudentInfo["Rubama"])
print(StudentInfo["Rubama"]["Number"])
#Accesing Items
print(StudentInfo["Year"])
#use get() method
print(StudentInfo.get("Sany"))
#Keys () Method
print(StudentInfo.keys())
#Get Values
print(StudentInfo.values())

#Change Dictionary Items
StudentInfo["Year"]=2005
print(StudentInfo["Year"])
#Update() metheod
StudentInfo.update({"Sany":'Sany is a Naughty Boy'})
print(StudentInfo["Sany"])

#pop () method removes
StudentInfo.pop("Rubama")
print(StudentInfo)
#popitem () method...<- last item dirac delet
StudentInfo.popitem()
print(StudentInfo)
#del() method
del StudentInfo["Sany"]
print(StudentInfo)
#clear() method
StudentInfo.clear()
print(StudentInfo)

#Loop
studentInfo = {
    "Rubama":{
        "Name":"Rubama Chowdhury",
        "Lcation":"Chadpur",
        "Study":"Computer Science & Engineer",
        "id":20230000000034,
        "Number":"01406573702"
    },

        "Sany": {
            "Name": "Mahmudur Rahman Sany",
            "Location": "Kishoregonj",
            "study": "Computer Science & Engineer",
            "id": 2022000000027,
            "Number": "01317970640"
    },

          "Year":1928
}
for x in studentInfo:
    print(x)
for a in studentInfo.values():
    print(a)
for b in studentInfo.keys():
    print(b)
for item in studentInfo.items():
    print(item)

#copy dictionary
student ={
    "sum1":20,
    "sum2":30,
    "sum3":50
}
print(student)
print(student.copy())
print(dict(student))