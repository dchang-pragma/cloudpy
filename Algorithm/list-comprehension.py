S = [x**2 for x in range(10)] # x^2 = x**2
print(S)
V = [2**i for i in range(13)]
print(V)
M = [x for x in S if x%2==0]
print(M)
M2 = [x**2 for x in range(10) if x%2==0]
print(M2)