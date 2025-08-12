#Dictionary Mrthod
Student = {
    "name" : "jayraj",
    "subjects" : {
        "math" : 98,
        "DSA" : 95,
        "PDS-1" : 99
    }
}

print(Student)
print(Student.keys())         #show all the keys
print(Student.values())       #show all the values
print(list(Student.items()))  #show all the items also convert into list 
# print(Student["name2"])     #show the error when you write not used key name
print(Student.get("name2"))   #show the none 
Student.update({"city" : "surat","name" : "jay"})  #when you write new key is added and write same key on the dic so its update the values you write
print(Student)