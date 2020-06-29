def main():
    ask = True
    n = 0
    while(ask):
        s = input("Change owed:\n")
        try: 
            n = float(s)
            if n > 0 and n < 9:
                ask = False
        except ValueError:
            print("parse error")
                
    
    calculateCoins(n)

def calculateCoins(n):
    print(n)
    cents = round(n * 100)
    numCoins = 0
    while (cents - 25 > -1):
        cents -= 25
        numCoins += 1
    while (cents - 10 > -1):
        cents -= 10
        numCoins += 1
    while (cents - 5 > -1):
        cents -= 5
        numCoins += 1
    while (cents - 1 > -1):
        cents -= 1
        numCoins += 1
        
    print(f"Number of coins: {numCoins}")
 



   
main()
