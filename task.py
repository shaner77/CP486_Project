from nt import getcwd
import re
def classify():
    vector1 = ["iphone", "apple", "coding", "internet", "software", "amazon", "samsung", "hack", "internet", "computer", "google", "bitcoin"]
    count1 = [0]*len(vector1)
    
    vector2 = ["engine", "gas", "vehicle", "drive", "clutch", "transmission", "suv", "van", "car", "truck", "road", "racecar"]
    count2 = [0]*len(vector2)
    
    vector3 = ["hockey", "football", "golf", "soccer", "basketball", "tennis", "ball", "run", "kick", "baseball", "play", "swim", "sport"]
    count3 = [0]*len(vector3)


    def cleanhtml(raw_html):
        cleanr = re.compile('< . , ""{}\/*?=><()>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
        cleantext = re.sub(cleanr, '', raw_html)
        return cleantext
    
    b = f'{getcwd()}\sports1.html'
    #b = f'{getcwd()}\sports2.html'
    #b = f'{getcwd()}\cars1.html'
    #b = f'{getcwd()}\cars2.html'
    #b = f'{getcwd()}\\tech1.html'                #be aware of the character that follows  \  if n, t, etc use \\
    #b = f'{getcwd()}\\tech2.html'
    
    print(b)
    f = open(b, "r", encoding='utf-8')
    
    for line in f:
        for word in line.split():
            word = cleanhtml(word)
            word = word.lower()
            print(f'{word}\n')
            
            i = 0
            while (i < len(vector1)): 
                if word == vector1[i]:
                    count1[i] = count1[i] + 1
                elif word == vector2[i]:
                    count2[i] = count2[i] + 1
                elif word == vector3[i]:
                    count3[i] = count3[i] + 1
                i = i + 1
    i = 0
    total1=0
    while(i < len(vector1)):
        print(f'{vector1[i]}: {count1[i]}   ')
        total1 = total1 + count1[i]
        i = i + 1
    
    i = 0
    total2=0
    print("\n")
    while(i < len(vector2)):
        print(f'{vector2[i]}: {count2[i]}   ')
        total2 = total2 + count2[i]
        i = i + 1
    
    i = 0
    total3=0
    print("\n")
    while(i < len(vector3)):
        print(f'{vector3[i]}: {count3[i]}   ')
        total3 = total3 + count3[i]
        i = i + 1   
        
    if total1 > total2 and total1 > total3:
        print("\n Technology!!")
    elif total2 > total1 and total2 > total3:
        print("\n Cars!!")
    elif total3 > total2 and total3 > total1:
        print("\n Sports!!")
    else:
        print("mixed")
        

classify()
