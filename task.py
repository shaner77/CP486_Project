from nt import getcwd
def classify():
    vector1 = ["iphone", "apple", "ios", "android", "pc", "mac", "computer", "television", "technology"]
    count = [0]*len(vector1)
    b = f'{getcwd()}\iphone1.txt'
    print(b)
    f = open(b, "r")
    for line in f:
        for word in line.split():
            #word by word
            word = word.lower()
            print(f'{word}\n')
            i = 0
            while (i < len(vector1)): 
                #vector.indexof("word")
                if word == vector1[i]:
                    count[i] = count[i] + 1
                i = i + 1
    i = 0
    while(i < len(vector1)):
        print(f'{vector1[i]}: {count[i]}   ')
        i = i + 1
classify()
