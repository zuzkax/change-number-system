def na_czworkowy(x):
    if len(x)% 2 != 0:
        x = '0' + x

    wynik=''
    for i in range(0,len(x),2):
        cyfra_czworkowa = 2 * int(x[i]) + int(x[i+1])
        wynik += str(cyfra_czworkowa)
    return wynik

def na_osemkowy(x):
    while len(x)%3 != 0:
        x = '0' + x

    wynik=''
    for i in range(0,len(x),3):
        cyfra_osemkowa = 4 * int(x[i]) + 2 * int(x[i+1]) + int(x[i+2])
        wynik += str(cyfra_osemkowa)
    return wynik

def na_szesnastkowy(x):
    while len(x)%4 != 0:
        x = '0' + x

    wynik=''
    for i in range(0,len(x),4):
        cyfra_szesnastkowa = 8 * int(x[i]) + 4 * int(x[i+1]) + 2*int(x[i+2]) + int(x[i+3])
        if cyfra_szesnastkowa > 9:
            odpowiedniki=['A','B','C','D','E','F']
            y = int(cyfra_szesnastkowa) - 10
            cyfra_szesnastkowa = odpowiedniki[y]
        wynik += str(cyfra_szesnastkowa)
        
    return wynik
 
    
x = str(10101010101110111)

print(na_czworkowy(x),na_osemkowy(x),na_szesnastkowy(x), sep=';')
