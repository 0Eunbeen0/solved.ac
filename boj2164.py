import sys
import collections
n=int(sys.stdin.readline())
card=collections.deque([i for i in range(n+1)])
card.remove(card[0])
while(n>1):
    card.append(card[1])
    card.remove(card[0])
    card.remove(card[0])
    n-=1
print(card[0])