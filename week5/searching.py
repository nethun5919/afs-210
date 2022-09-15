from msilib import MSIMODIFY_DELETE


num_list = [
    7, 20, 26, 31, 40, 51, 55, 63, 74, 81
    ] 

target_list= [
    "Alpha", "Beta", "Delta", "Epsilon", "Gamma", "Theta", "Zeta"
    ]   
 
 #          param 1, param2
def search(num_list, target):
    # variable num1
    left=0
    # variable num2
    right= len(num_list) -1    
    while left <= right:
        middle = round((left + right)/2)
        if num_list[middle] == target:
            return True
        elif target < num_list[middle]:
            right = middle -1
        else:
            left = middle +1

    if left > right:
        return False    

    print(num_list)

  
    
    # if statment that checks if the first paremeter[middle] > the secnd paremeter
        # make second variable = middle -1
    # else:
        #make first = middle +1

# if first variable is > last variable
    # return False 
#print(call function by functionName(list1,13)) 
     
print(search(num_list, 31)) 
print(search(num_list, 77))
print(search(target_list,"Delta" )) 
