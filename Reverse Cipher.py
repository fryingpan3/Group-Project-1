"""THIS IS FUNCTION REVERSES THE USERS INPUT PHRASE OR WORD"""
def reverse_cipher(user_choice): #DEFINES THE FUNCTION
    user_list = [] #CREATES A LIST TO FLIP THE INPUT
    for i in user_choice: #GOES THROUGH EACH ITEM IN THE INPUT
        user_list.insert(0,i) #ADDS IT BACK TO THE LIST
    return(''.join(user_list)) #RETURNS TO THE MAIN PROGRAM
        
        



