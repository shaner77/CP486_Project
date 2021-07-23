from nt import getcwd
def classify():
    vector1 = ["iphone", "apple", "ios"]
    count = [0, 0, 0]
    b = f'{getcwd()}\iphone1.txt'
    print(b)
    f = open(b, "r")
    for line in f:
        for word in line.split():
            #word by word
            word = word.lower()
            print(f'{word}\n')
            i = 0
            while (i < 3): 
                #vector.indexof("word")
                if word == vector1[i]:
                    count[i] = count[i] + 1
                i = i + 1
    print(f'IPhone: {count[0]} \nApple: {count[1]} \nIOS: {count[2]}')
classify()