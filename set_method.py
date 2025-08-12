#Set Method
# collection = set()
# collection.add(1)
# collection.add(2)
# collection.add(2)
# collection.add(3)
# collection.add("jayraj")     #add the new element

# collection.remove(2)         #remove the element
# collection.clear()           #clear the all 
# print(collection)

#pop
collection = {"name","jayraj","surat",20}
print(collection.pop())
print(collection.pop())    #remove the rendome element 


#union and intersection
set1 = {1,2,3}
set2 = {2,3,4}

print(set1.union(set2))          #show the all values but not repeted {1,2,3,4}
print(set1.intersection(set2))   #show only combaine values {2,3}