def Affine_De(String):
    alph = ["a","b","c","d","e","f","g","h","i","j","k","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    try:
        print("A key?, it must be a prime")
        Akey = int(input())
        print("B key, it can be anythin")
        Bkey = int(input())
    except:
    # covert into numbers
    for i in range (0, len(planetext)-1):
        for p in range (0,25):
            if alph[int(p)] == planetext[int(i)]:
                numtext.append(p)
    # undo keys
    for i in range (0, len(numtext)):
    try:
        numtext[i] = Akey/(numtext[i]-Bkey)
    except:
        print("")
    # convert back to letters
    for i in range(0, len(numtext)):
        try:
            EnString.append(alph[numtext[i]])
        except:
            number = numtext[i] - 26
            EnString.append(alph[number])
    String = planetext
    print(EnString)
    return EnString
