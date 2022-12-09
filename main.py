s = input("Введыть довільне слово --> ")
f = open('Text.txt', 'r', encoding='utf-8')
for i in range(5):
    d=f.readline().split()
    for k in d :
        if s in k:
            for y in d:
                print(y, end=' ')
            print('\n')