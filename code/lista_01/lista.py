from random import choice
coins = ['orzeł', 'reszka']


class Coin:
    
    def __init__(self, denomination) -> None:
        self.side = "orzeł"
        self.denomination = denomination

    def __str__(self) -> str:
        return f'Moneta: {self.side}, nominał: {self.denomination}'
    
    def throw(self):
        self.side = choice(['orzeł', 'reszka'])
        

coin = Coin(1)
# print(coin)
m1 = Coin(1)
m2 = Coin(2)
m5 = Coin(5)


# for i in range(15):
#     m5.throw()
#     print(f"{i+1}: {m5.side}")
    

def single_game(coins):
    s = 0
    while True:
        for m in coins:
            m.throw()
            if m.side == "orzeł":
                s += m.denomination
        if s == 20:
            return True
        elif s > 20:
            return False
        else:
            continue
        

n = 1000
wins = 0
for _ in range(n):
    wins += single_game([m1, m2, m5]) 
    
    
print(f'Wygrane: {wins}, przegrane: {n-wins}')   
        
