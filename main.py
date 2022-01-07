the_file = open("file.txt","r") 

required_letters = [] 

key = input("Enter a word you want to use as the key: ")

content = the_file.read() 

modified_key = key*len(content) 

modified_key = list(modified_key) 

for i in range(len(content)): 
    
    required_letters.append(modified_key[i]) 
    
content = list(content) 
    
new_file = open("new_file.txt","w") 

decision = input("Press e to encrypt or d to decrypt: ") 

if decision == "e": 
    
    for i in range(len(content)): 
        
        encrypted_letter = ord(required_letters[i]) + ord(content[i]) 
        
        encrypted_letter = chr(encrypted_letter) 
        
        new_file.write(encrypted_letter) 
        
elif decision == "d": 
    
    for i in range(len(content)): 
        
        decrypted_letter = ord(content[i]) - ord(required_letters[i]) 
        
        if(decrypted_letter > 0 and decrypted_letter < 11141111): 
            decrypted_letter = chr(decrypted_letter) 
            new_file.write(decrypted_letter) 
        else:
            print("ValueError: chr() arg not in range(0x110000)")
            print("The Program Will End")
            print("Look at the Readme.txt file next time")
            break

            
the_file.close() 

new_file.close() 
    
    
    
    
    
    
    
    







