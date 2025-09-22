
#top-down(DP)
def climbStairs(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 1:
        return 1
    if n == 2:
        return 2

    memo[n] = climbStairs(n - 1, memo) + climbStairs(n - 2, memo)
    return memo[n]

print("First solution:")
print(climbStairs(5))  # 8

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Bottom-Up(DP)
def climbStair(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    a,b=1,2
    for i in range(3,n+1):
        a,b=b,a+b
    return b
print("Second solution:")
print(climbStair(5))


