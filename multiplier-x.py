import time

def sumCalc():
    for tafel in range(1,11,1):
        print('---' + str(tafel) + '---')
        print(sum * tafel)
        time.sleep(0.5)

sum = int(input('Welke tafel wilt u zien? '))

sumCalc()