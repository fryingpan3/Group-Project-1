#STEP BY STEP PROOF OF TRANSPOSITIONCYPHER USING ABCDEFGHI and KEY =
from time import sleep
string = "abcdefghi"
def Transposition_Cypher(string):
  #TAKES KEY INPUT WITH VALIDATION  
  while True: 
     try: 
         key = 3
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
  print("EXPLANATION OF TRANSPOSITION CODE: Input is 'abcdefghi' and the code is 3")
  sleep(3)
  print("\nHere the input gets split into an array, the string is written into a list, as soon as the list reaches a length equal to the key,\nthe list is appended to the Cypher Array, the temporary list is then cleared and this repeats until all letters are withheld in the Cypher Array")
  sleep(10)  
  while count < len(String_List):
    if tempcount < key:
        temp.append(string[count])
        count += 1
        tempcount += 1
        print("Temp List:", temp)
        sleep(1)
    else:
        Cypher_Array.append(temp)
        temp = []
        tempcount = 0
        print("Added to Cypher Array. Current Contents: ", Cypher_Array)
        sleep(2)
        
  #TESTS FOR OVERFLOW OF CHARACTERS TO BE ADDED TO ARRAY
  print("\nHere is the current contents of the Cypher Array:",Cypher_Array)
  sleep(4)
  print("\nTo add the final temp list at the end of the string,\nthis code fills the temp list with spaces until it is equal to the length of the key. Once this is true, temp is added to the Cypher Array")
  sleep(5)
  if len(temp) < key:
      while len(temp) < key:
          temp.append(" ")
      Cypher_Array.append(temp)
  elif len(temp) == key:
    Cypher_Array.append(temp)

  print("\nHere is the final contents of temp: ",temp, "\nHere is the final Cypher Array: ",Cypher_Array)  
  sleep(8)
  #INDEXING SET UP FOR LIST THAT HOLDS SEQUENCE OF ENCRYPTED CHARACTERS
  x = 0
  y = 0
  z = ""
  new = []
  #FORMS LIST OF ENCRYPTED CHARACTERS
  print("\nHere the first character of each mini list in the Cypher Array gets added to a new list,\nthen the second characters in the list get added etc. This forms a list of letters in the sequence of the encrypted code")
  sleep(8)
  while y < key:
    while x < len(Cypher_Array):
      new.append(Cypher_Array[x][y])
      print("Encrypted List:", new)
      sleep(1)
      x += 1
    x = 0
    y += 1

  print("\nFinal Encrypted List:", new)
  sleep(3)
  print("\nNow the encrypted list is converted into a single string")
  Encrypted = z.join(new) #FORMS FINAL CODE
  sleep(2)
  print("\nThe Encrypted string is:", Encrypted)
  #print(Cypher_Array) OUTPUTS STRING STORED IN ARRAY
  #print(new) OUTPUTS LIST OF ENCRYPTED STRING

  

Transposition_Cypher(string)
