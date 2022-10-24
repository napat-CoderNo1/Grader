def maximumWealth(accounts):
    for i in range(len(accounts)):
        accounts[i] = sum(accounts[i])
    return max(accounts)

print(maximumWealth([[2,8,7],[7,1,3],[1,9,5]]))
