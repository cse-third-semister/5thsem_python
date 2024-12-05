import random

def roll_dice(): return random.randint(1, 6) + random.randint(1, 6)

wins, losses = {}, {}
for _ in range(1_000_000):
    roll, point = 1, roll_dice()
    while True:
        if roll == 1 and point in {7, 11} or roll > 1 and roll_dice() == point:
            wins[roll] = wins.get(roll, 0) + 1
            break
        elif roll == 1 and point in {2, 3, 12} or roll > 1 and roll_dice() == 7:
            losses[roll] = losses.get(roll, 0) + 1
            break
        roll += 1

total_games = sum(wins.values()) + sum(losses.values())
win_pct = sum(wins.values()) / total_games * 100
loss_pct = sum(losses.values()) / total_games * 100
resolved = {r: wins.get(r, 0) + losses.get(r, 0) for r in range(1, max(wins.keys() | losses.keys()) + 1)}
cumulative = 0

print(f"Games won: {win_pct:.2f}%, Games lost: {loss_pct:.2f}%")
for r, count in resolved.items():
    pct = count / total_games * 100
    cumulative += pct
    print(f"Roll {r}: {pct:.2f}% resolved, cumulative: {cumulative:.2f}%")





# Games won: 51.21%, Games lost: 48.79%
# Roll 1: 33.36% resolved, cumulative: 33.36%
# Roll 2: 17.55% resolved, cumulative: 50.91%
# Roll 3: 12.83% resolved, cumulative: 63.74%
# Roll 4: 9.52% resolved, cumulative: 73.26% 
# Roll 5: 7.00% resolved, cumulative: 80.26% 
# Roll 6: 5.14% resolved, cumulative: 85.40%    
# Roll 7: 3.82% resolved, cumulative: 89.22%    
# Roll 8: 2.80% resolved, cumulative: 92.03%    
# Roll 9: 2.07% resolved, cumulative: 94.09%    
# Roll 10: 1.53% resolved, cumulative: 95.62%   
# Roll 11: 1.14% resolved, cumulative: 96.76%   
# Roll 12: 0.83% resolved, cumulative: 97.59%   
# Roll 13: 0.62% resolved, cumulative: 98.21%   
# Roll 14: 0.46% resolved, cumulative: 98.67%   
# Roll 15: 0.34% resolved, cumulative: 99.02%   
# Roll 16: 0.25% resolved, cumulative: 99.27%   
# Roll 17: 0.19% resolved, cumulative: 99.46%   
# Roll 18: 0.14% resolved, cumulative: 99.60%   
# Roll 19: 0.10% resolved, cumulative: 99.71%   
# Roll 20: 0.08% resolved, cumulative: 99.79%   
# Roll 21: 0.05% resolved, cumulative: 99.84%   
# Roll 22: 0.04% resolved, cumulative: 99.88%   
# Roll 23: 0.03% resolved, cumulative: 99.91%   
# Roll 24: 0.02% resolved, cumulative: 99.93%   
# Roll 25: 0.02% resolved, cumulative: 99.95%   
# Roll 26: 0.01% resolved, cumulative: 99.96%   
# Roll 27: 0.01% resolved, cumulative: 99.97%   
# Roll 28: 0.01% resolved, cumulative: 99.98%   
# Roll 29: 0.01% resolved, cumulative: 99.98%   
# Roll 30: 0.00% resolved, cumulative: 99.99%   
# Roll 31: 0.00% resolved, cumulative: 99.99%   
# Roll 32: 0.00% resolved, cumulative: 99.99%   
# Roll 33: 0.00% resolved, cumulative: 99.99%   
# Roll 34: 0.00% resolved, cumulative: 100.00%  
# Roll 35: 0.00% resolved, cumulative: 100.00%  
# Roll 36: 0.00% resolved, cumulative: 100.00%  
# Roll 37: 0.00% resolved, cumulative: 100.00%  
# Roll 38: 0.00% resolved, cumulative: 100.00%  
# Roll 39: 0.00% resolved, cumulative: 100.00%  
# Roll 40: 0.00% resolved, cumulative: 100.00%  
# Roll 41: 0.00% resolved, cumulative: 100.00%  
# Roll 42: 0.00% resolved, cumulative: 100.00%  
# Roll 43: 0.00% resolved, cumulative: 100.00%  
# Roll 44: 0.00% resolved, cumulative: 100.00%  
# Roll 45: 0.00% resolved, cumulative: 100.00%  
# Roll 47: 0.00% resolved, cumulative: 100.00%
# Roll 48: 0.00% resolved, cumulative: 100.00%
# Roll 47: 0.00% resolved, cumulative: 100.00%
# Roll 48: 0.00% resolved, cumulative: 100.00%
# Roll 47: 0.00% resolved, cumulative: 100.00%
# Roll 47: 0.00% resolved, cumulative: 100.00%
# Roll 47: 0.00% resolved, cumulative: 100.00%
# Roll 47: 0.00% resolved, cumulative: 100.00%
# Roll 47: 0.00% resolved, cumulative: 100.00%
# Roll 48: 0.00% resolved, cumulative: 100.00%
# Roll 50: 0.00% resolved, cumulative: 100.00%
# Roll 51: 0.00% resolved, cumulative: 100.00%
# Roll 52: 0.00% resolved, cumulative: 100.00%
# Roll 53: 0.00% resolved, cumulative: 100.00%