from nt import getcwd
import re

# t iterates from the max type number to 0
def classify(vector, t, n):
    
    count = [0]*len(vector)

    def cleanhtml(raw_html):
        cleanr = re.compile('< . , ""{}\/*?=><()>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
        cleantext = re.sub(cleanr, '', raw_html)
        return cleantext
    if t == 0:
        b = f'{getcwd()}\\tech{n}.html'
    elif t == 1:
        b = f'{getcwd()}\cars{n}.html'
    elif t == 2:
        b = f'{getcwd()}\Sport {n}.htm'
    
    print(f'FILE: {b}')
    f = open(b, "r", encoding='utf-8')
    
    for line in f:
        for word in line.split():
            word = cleanhtml(word)
            word = word.lower()
            #print(f'{word}\n')
            
            i = 0
            while (i < len(vector)): 
                if word == vector[i]:
                    count[i] = count[i] + 1

                i = i + 1

    i = 0
    total = [0,0,0]
    row = []
    o = open(f'output{t}.txt', 'a')
    i = 0
    o.write('\n')
    
    while(i < len(vector)):
       
        total[0] = total[0] +  count[i]
        row.append(count[i])

        i = i + 1
    if t == 0:
        o.write(f'Tech{n}'.ljust(12))
    elif t == 1:
        o.write(f'Cars{n}'.ljust(12))
    elif t == 2:
        o.write(f'Sports{n}'.ljust(12))
    
    for d in row:
        o.write(f'{d}'.ljust(12))
            
    o.close()   

    a = open("output0.txt", 'r')
    next(a)
    next(a)
    b = open("output1.txt", 'r')
    next(b)
    next(b)
    c = open("output2.txt", 'r')
    next(c)
    next(c)
    
    o = open("totaloutput.txt", 'w')
    o.write('\t')
    for i in vector:
        if len(i) < 4:
            o.write('\t')
        if len(i) > 7:
            o.write(f'\t{i} '.ljust(8))
        else:
            o.write(f'\t{i}\t'.ljust(6))
    o.write('\n')
    for line1 in a:
        o.write(line1)
    o.write('\n')
    for line2 in b:
        o.write(line2)
    o.write('\n')
    for line3 in c:
        o.write(line3)
    o.write('\n')       
    o.close()
    
def main(t, n):
    vector0 = ["iphone", "code", "internet", "phone", "network", "samsung", "computer", "device", "program", "digital"]
    vector1 = ["engine", "gas", "vehicle", "automobile", "drive", "car", "transportation", "road", "wheel", "tire"]
    vector2 = ["hockey", "football", "golf", "soccer", "basketball", "baseball", "play", "sport", "run", "kick"]
    vector = vector0 + vector1 + vector2

    j = 1
    
    o = open(f'output{t}.txt', 'w')
    i = 0
    o.write('\t')
    for d in vector:
        if len(d) < 4:
            o.write('\t')
        if len(d) > 7:
            o.write(f'\t{d} '.ljust(8))
        else:
            o.write(f'\t{d}\t'.ljust(6))
    o.write('\nVector'.ljust(13))
    while(i < len(vector)):
        o.write(f'{i}'.ljust(12))
        i = i + 1
    o.close()
    
    while j <= n:
        classify(vector, t, j)
        j = j + 1
    if t > 0:
        main(t-1, n);


n = int(input("How many documents in each category? "))
main(2, n)