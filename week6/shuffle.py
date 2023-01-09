import random



list = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]

# li
def shuffle (list):
  for i in range(len(list) -1, 0, -1):
    #print(i)
    j = random.randint(0, i + 1)
   # print(j)
    list[i],list [j]= list [j],list[i]
    return list
shuffle(list)
    
print(list)
shuffle(list)
    
print(list)
shuffle(list)
    
print(list)
shuffle(list)
    
print(list)
    
print(list)
