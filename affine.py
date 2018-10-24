#decoding and encoding cypher (affine)
def Affine_En(Key1Input, Key2Input, plainText):
    EnString = []
    Akey = Key2Input
    Bkey = Key1Input
    planetext = plainText
    numtext = []
    newnum = []
    alph = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    # convert to num
    for i in range (0, len(planetext)):
        for p in range (0,27):
            print(planetext[int(i)], p)
            if p == 26:
                numtext.append(planetext[int(i)])
                print("planetext")
                
            elif alph[int(p)] == planetext[int(i)]:
                numtext.append(p)
                break
            
    print(numtext)
    # apply cypher
    for i in range (0, len(numtext)):
        try:
            numtext[i] = (Akey*numtext[i]+Bkey) % 26
        except:
            print("except cypher")
    # covert back to letters
    for i in range(0, len(numtext)):
        try:
            EnString.append(alph[numtext[i]])
        except:
            try:
                number = numtext[i] - 26
                EnString.append(alph[number])
            except:
                EnString.append(numtext[i])
                
    String = planetext
    "".join(EnString)
    print(EnString)
    return EnString

            
        
    
