#Dictionary 
# info = {
#     "name" : "jayraj",
#     "age" : 20,
#     "subject" : ["math","state","DSA"],
#     "topic" : ("dic", "set")
    
# }
# print(info)
# print(info["name"])
# info["name"] = "jay" 
# info["surname"] = "girase"
# print(info)

# null_dic = {}       #also print null values and after adding the values 
# null_dic["name"] = "jayraj"
# print(null_dic)
# print(info["surname"])  #when not accesit value show the error


  #Nested Dictionary
Student = {
    "name" : "jayraj",
    "subjects" : {
        "math" : 98,
        "DSA" : 95,
        "PDS-1" : 99
    }
}
print(Student)
print(Student["subjects"])
print(Student["subjects"]["DSA"])