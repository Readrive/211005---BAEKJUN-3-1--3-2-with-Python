n = int(input())

for i in range(1, 10):
    x = n * i
    print(n, "*", i, "=", x)


T = int(input()) #몇 개의 식을 만들 것인지

for i in range(0, T):
    A, B = map(int, input().split())
    S = A + B
    print(S)