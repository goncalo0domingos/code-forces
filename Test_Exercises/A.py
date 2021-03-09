def solve(n,k): 
    number_set = list(range((k+1) // 2,k)) + list(range(k+1,n+1))
    print(len(number_set))
    print(" ".join(map(str, number_set)))

def anti_knapsack():
    for _ in range(int(input())):
            n,k = input().split()
            solve(int(n),int(k))

anti_knapsack()


