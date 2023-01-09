


class stack:
    def __init__(self):
        self.data = []
       
    
    def push(self, item): 
        self.data.append(item)

    def pop(self):
        return self.data.pop()
    
    def isEmpty(self):
        return len(self.data) == 0
    
    def peek(self):
        return self.data[len(self.data)-1] 
        
    def size(self):
        return len(self.data)



class queue:

    def __init__(self):
        self.data = []
       
    
    def enqueue(self, item): 
        self.data.insert(0,item)

    def dequeue(self):
        return self.data.pop()
    
    def isEmpty(self):
        return len(self.data) == 0
    
    def peek(self):
        return self.data[len(self.data)-1] 
        
    def size(self):
        return len(self.data)       

def isPalindrome(str):
    queueString = queue()
    stackString = stack()

    for letter in str: 
        queueString.enqueue(letter)
        stackString.push(letter)
    
    print(queueString.data)
    print(stackString.data)
    match = True
    index = 0
    for letter in str:
        if queueString.data[index] != stackString.data[index]:
            match = False 
        index += 1
    return match  



userInput = input('Choose a word:')
print(isPalindrome(userInput))

