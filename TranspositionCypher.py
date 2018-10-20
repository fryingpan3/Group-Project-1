string = input("ENTER STRING: ")
def Transposition_Cipher(string):
  #TAKES KEY INPUT WITH VALIDATION  
  while True: 
     try: 
         key = int(input("ENTER KEY: ")) 
         break 
     except ValueError: 
         print("INVALID INPUT")

  #LIST COMPREHENSION FORMATTING
  String_List = list(string) 
  Cypher_Array = []
  temp = [] #HOLDS LETTERS TO THE LENGTH OF THE KEY BEFORE INSERTION INTO ARRAY
  count = 0 #CORRESPONDS TO LETTER TO BE INSERTED INTO LIST
  tempcount = 0 #CORRESPONDS TO LENGTH OF LIST

  #CREATES TRANSPOSED ARRAY
  while count < len(String_List):
    if tempcount < key:
        temp.append(string[count])
        count += 1
        tempcount += 1
    else:
        Cypher_Array.append(temp)
        temp = []
        tempcount = 0
        
  #TESTS FOR OVERFLOW OF CHARACTERS TO BE ADDED TO ARRAY 
  if len(temp) < key:
      while len(temp) < key:
          temp.append(" ")
      Cypher_Array.append(temp)
  elif len(temp) == key:
    Cypher_Array.append(temp)

  #INDEXING SET UP FOR LIST THAT HOLDS SEQUENCE OF ENCRYPTED CHARACTERS
  x = 0
  y = 0
  z = ""
  new = []
  #FORMS LIST OF ENCRYPTED CHARACTERS
  while y < key:
    while x < len(Cypher_Array):
      new.append(Cypher_Array[x][y]) 
      x += 1
    x = 0
    y += 1

   
  Encrypted = z.join(new) #FORMS FINAL CODE  
  #print(Cypher_Array) OUTPUTS STRING STORED IN ARRAY
  #print(new) OUTPUTS LIST OF ENCRYPTED STRING
  print(Encrypted)#FINAL OUTPUT
  

Transposition_Cipher(string)



    
