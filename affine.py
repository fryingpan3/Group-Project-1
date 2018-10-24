#decoding and encoding cypher (affine)
def Affine_En(planetext, Akey, Bkey):
    EnString = []
    numtext = []
    newnum = []
    alph = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","M","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    # convert to num
    for i in range (0, len(planetext)):
        for p in range (0,27):
            if p == 26:
                numtext.append(planetext[int(i)])
            elif alph[int(p)] == planetext[int(i)]:
                numtext.append(p)
                break
    # apply cypher
    for i in range (0, len(numtext)):
        try:
            numtext[i] = (Bkey*numtext[i]+Akey) % 26
        except:
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
Affine_En(plainText, Key1Input, Key2Input)
