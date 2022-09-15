# #tuple
Data1 = (7, False, "Apple", True, 7, 98.6)
len(Data1)
print(len(Data1))
print(Data1[3])
print(Data1.count(7))

# #set
Data2 = {"July", 4, 8, "Tango", 4.3, "Bingo"}
Data2.pop()
Data2.add("Alpha")
print(Data2)

#list
Data3 = ["A", 7, -1, 3.14, True, 7] 
Data3.reverse()
Data3[3] = "b"
Data3.pop(len(Data3)-1)
print(Data3)



#dictionary
Data4 = { 
    "name" : "Joe",
    "age" : 26,
    "active" : True, 
    "hourly_wage" : 14.75, 
    "hours_perWeek" : 40
    }
if Data4["hours_perWeek"] == 40: 
    print(Data4["hourly_wage"] * Data4["hours_perWeek"])

Data4["active"] = False
Data4.update({"address": "123_West_Main_Street"})

print(Data4)
