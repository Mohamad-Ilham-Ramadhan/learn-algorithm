'''
    (2D Dynamic Programming) leetcode: 309. Best Time to Buy and Sell Stock with Cooldown


    You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day.

    Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

        - After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).

    Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

    

    Example 1:
        Input: prices = [1,2,3,0,2]
        Output: 3
        Explanation: transactions = [buy, sell, cooldown, buy, sell]

    Example 2:
        Input: prices = [1]
        Output: 0
    

    Constraints:
        - 1 <= prices.length <= 5000
        - 0 <= prices[i] <= 1000
'''

def maxProfit(prices):
    '''
        p12 = [2,1,3,10,9,10,0,7,9,1] # 18
        [maxPrice's index, maxProfit]
        p [0,0] pad
        1 [9,0]
        9 [8,0]
        7 [8, max(2+0, 0 ) 2]
        0 [8, max((7+0), (9+0)) 9] if maxPrice'Index > i-1, consider it
        10 [5, 9]
        9 [5, max((1+2), 9) 9]
        10 [3, 9]
        3 [3, 16]
        1 [3, max(16, (2+9), (9+9)), 18]
        2 [3, max(18, (1+9), (8+9)), 18] here I confuse how to buy 2 and sale to 3 algo
    '''
    prices.append(0) # max number, so it won't generate any profit
    prices.append(0) # max number, so it won't generate any profit
    prices.append(0) # max number, so it won't generate any profit
    dp = [[len(prices)-4, 0] for i in range(len(prices))] # [maxPrice'index, maxProfit]
    for i in range(len(prices)-4, -1, -1):
        p = prices[i]
        if p >= prices[dp[i+1][0]]: # update maxPrice 
            dp[i][0], dp[i][1] = i, dp[i+1][1]
            continue 
        print('i', i)
        sellNext = 0
        j = i+1
        while p > prices[j] and j < (len(prices) - 3):
            j += 1
        sellNext = (prices[j] - p) + dp[j+2][1]
        sellMax = ((prices[dp[i+1][0]] - p) + dp[dp[i+1][0]+2][1])
        profit = max(dp[i+1][1], sellMax, sellNext )
        print('profit', profit, 'sellNext', sellNext, 'sellMax', sellMax)
        dp[i][0] = dp[i+1][0]
        dp[i][1] = profit

    print('dp', dp)
    
    return dp[0][1]

'''
    fail1 = [91,71,43,1,61,24,78,18,57,81,82,73,49,61,42,37,46,84,95,82] # expected 194, output: 169
    [0,0]
    [0,0]
    [0,0]
    [19,0]

    dp [[18, 169], [18, 169], [18, 169], [18, 169], [18, 148], [18, 148], [18, 109], [18, 109], [18, 94], [18, 71], [18, 70], [18, 70], [18, 70], [18, 58], [18, 58], [18, 58], [18, 49], [18, 11], [18, 9], [0, 9], [0, 0], [0, 0], [0, 0]]

'''
fail1 = [91,71,43,1,61,24,78,18,57,81,82,73,49,61,42,37,46,84,95,82] # expected 194

p1 = [1,2,3,0,2] # 3
p2 = [1] # 0
p3 = [7,9,1,5,9,5,9,2,9,7,3,9,0,3,1] # 21
print('RESULT :', maxProfit(fail1))
'''
    1 [0,0]
    3 [0,0]
    0 [3,3]
    9 [3,3]
    3 [6,6]
    7 [6,6]   < to greater than it (9)
    9 [6,6]
    2 [7,13]
    9 [13,13]
    5 [4,10]
    9 [0,13]
    5 [4, 17]
    1 [8, 21]
    9 [21,21]
    7 [21,21]

'''
p4 = [1,2,3,4] # 3
p5 = [1,2,3,4,5,6] # 5
'''
    6
    [5->6] = 1
    4->5 or 4->6
    [4->6] = 2
    3
'''
p6 = [1,2,3,4,5,6,7,8,9,10] # 9
p7 = [10,5,2,1,7,3,5,4,1,9] # 14
'''
    9
    [1->9] = 8
    [4->9] = 5
    [5->9] = 4
    [3->5 - 1->9] = 10
    [7->9] = 2
    [1->7->9] = 8
    [2->7->9] = 7
'''
p8 = [1,7,3,5,0,2,2,5,0,2] # 11
'''
    2
    0->2 = 2
    5
    2->5 = 3
    2->5 = 3
    0
'''
p9 = [0,2,3,4,5,6,7,8,9,10,20] # 20
'''
    20
    10 -> 20 = 10
    9 -> 20 = 11
'''
p10 = [1,2,3,4,5,1,2,3,4,5] # 7
'''
    update until there is bigger number
    5
    4
    3
    2 => 5
    1 => 5
    5 => 5
    4
    3
    2
    1
'''
p11 = [5,1,2,3,4,5] # 4
p12 = [2,1,3,10,9,10,0,7,9,1] # 18
'''
    [maxPrice's index, maxProfit]
    p [0,0] pad
    1 [9,0]
    9 [8,0]
    7 [8, max(2+0, 0 ) 2]
    0 [8, max((7+0), (9+0)) 9] if maxPrice'Index > i-1, consider it
    10 [5, 9]
    9 [5, max((1+2), 9) 9]
    10 [3, 9]
    3 [3, 16]
    1 [3, max(16, (2+9), (9+9)), 18]
    2 [3, max(18, (1+9), (8+9)), 18] here I confuse how to buy 2 and sale to 3 algo
'''
p13 = [2,1,1,3,1,10,9,10,0,7,9,1] # 18

# print('RESULT :', maxProfit([2,1,1,3,1,10,9,10,0,7,9,1]))