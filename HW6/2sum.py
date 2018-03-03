stored = set()
for j in open('2sum.txt', 'r'):
    stored.add(int(j))

def twoSum(t):
    #searches through stored to see if there is a distint x, y that add to t
    for i in stored:
        k = t - i
        if k in stored and k != i:
            return True
    return False
    
def checkSums(a,b):
    count = 0
    for i in range(a, b + 1):
        if twoSum(i):
            count += 1
    print(a, ' to ', b, ' = ', count)
import time
start = time.time()
checkSums(9001, 10000)
end = time.time()
print(end - start)
