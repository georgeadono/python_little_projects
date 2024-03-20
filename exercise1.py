#icsd16007, Antonopoulos Georgios

#Anoigoume to arxeio sa string
with open('words.txt', 'r') as file:
    data = file.read().replace('\n', '')
frequent_letter = ""
frequency = 0  
lfrequent_letter = ""
lfrequency = 100  
letters = []
  

  
# for apo gramma se gramma
for a in data:
      
    # ta kanoume ola peza kai svhnoume tuxwn komma h teleies 
    
    listl = a.lower().replace(',','').replace('.',''); 
   
      
    # ta vazoume se lista
    for w in listl:  
        letters.append(w);  


#GIA TO MAX  
for i in range(0, len(letters)):  
      
    
    count = 1;  
      
    # Metrame kathe gramma 
    for j in range(i+1, len(letters)):  
        if(letters[i] == letters[j]):  
            count = count + 1;  
  
    # An to count einai megalutero ap to frequency 
    if(count > frequency):  
        frequency = count;  
        frequent_letter = letters[i];  

#GIA TO MIN
for i in range(0, len(letters)):  
      
    
    lcount = 1;  
      
    # Metrame pali kathe gramma 
    for j in range(i+1, len(letters)):  
        if(letters[i] == letters[j]):  
            lcount = lcount + 1;  
  
    # An to lcount einai mikrotero ap to lfrequency kai den einai mhden
    #giati theloume na uparxei to gramma
    if(lcount < lfrequency and lcount != '0'):  
        lfrequency = lcount;  
        lfrequent_letter = letters[i]; 


  
print("Most frequent letter: " + frequent_letter +"," + str(frequency) + " times")
print("Least frequent letter: " + lfrequent_letter +"," + str(lfrequency) + " times")

file.close()