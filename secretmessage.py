alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = int(input ('enter your key : '))

newmessage = ' '
message = input('please enter the message : ')

for character in message :
    if character in alphabet:
        position =  alphabet . find(character)
        newpos = (position + key)%26
        newchar = alphabet[newpos]
        newmessage += newchar
    else:
        newmessage += character

print('your newmessage is : ',newmessage)    
