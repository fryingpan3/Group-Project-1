#decoding and encoding cypher (affine)
def Affine_En(String):
    EnString = []
    String = "abcd!"
    try:
        Akey = int(input())
        Bkey = int(input())
    except:
        print("NO LETTERS!")
        Affine()
    planetext = String
    numtext = []
    newnum = []
    alph = ["A","B","C","D","E","F","G","H","I","J","K","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    # convert to num
    for i in range (0, len(planetext)-1):
        for p in range (0,25):
            if alph[int(p)] == planetext[int(i)]:
                numtext.append(p)
    # apply cypher
    for i in range (0, len(numtext)):
        try:
            numtext[i] = Akey*numtext[i]+Bkey
        except:
            print("")
    # covert back to letters
    for i in range(0, len(numtext)):
        try:
            EnString.append(alph[numtext[i]])
        except:
            number = numtext[i] - 26
            EnString.append(alph[number])
    String = planetext
    print(EnString)
    return EnString
Affine()


            
        
    
