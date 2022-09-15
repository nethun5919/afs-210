class HashTable:
    def __init__(self) -> None:
        self.size = 10
        self.slots = [None] * self.size #key
        self.data = [None] * self.size  # value
   
    def hashFunction(self,key):
      #Insert your hashing function code
       #key modulus table_size

      key % self.size
         # multi = 1
         # hv = 0
         # for ch in str(key):
         #    hv += multi * ord(ch)
         #    multi += 1
         #    return key % self.size

    def rehash(self,key):
        # Insert your secondary hashing function codye
     # key div table_size
     pass
     def put(self,key,data):
        # Insert your code here to store key and data 
         hv = self.hashFunction(key) 
         if self.slots [hv]== None:
            self.slots[hv] = key
            self.data [hv] = data
         else:
            if self.slots[hv] == key: #update
               self.data[hv] = data
            else: #collision
               hv = self.rehash(key)
               if self.slots[hv] == None:
                  self.slots[hv] = key
                  self.data[hv] = data
               else:
                  print("unresolved collision")


        
        

    def get(self,key):
        # Insert your code here to get data by key
    
     def __getitem__ (self,key):
        return self.get(key)
    
     def __setitem__ (self,key,data):
        self.put(key,data)
H = HashTable()
H[69] = 'A'
H[66] = 'B'
H[89] = 'G'
# Store remaining input data
print(H.slots)
print(H.data)

# print the value for key 52