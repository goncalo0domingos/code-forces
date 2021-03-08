def solve(n,k):
    number_set = [i for i in range(1,n+1)]
    number_set.pop(k-1)
    count = 0
    for i in range(0,k-1):
        a = number_set[i]
        if a:
            for j in range(k-2-i,0,-1):
                b = number_set[j]
                if b and (a != b):
                    if (a + b) == k:
                        number_set[i] = None
                        count += 1
                        break
                    elif (a + b) < k: break

    print((n-1-count))
    for i in number_set:
        if i:
            print(i,end=' ')
    print()

def anti_knapsack():
    for i in range(0,int(input())):
        try:
            n,k = input().split()
            solve(int(n),int(k))
        except:
            return
anti_knapsack()
