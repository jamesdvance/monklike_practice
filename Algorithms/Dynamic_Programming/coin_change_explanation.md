# Coin Change

## Bottom-up Dynamic Programming Solution

### Intuition: 
The optimal # of coins can be found by first finding the optimal # to make each amount
less than amount. This way you can build up to a proven-optimal solution

### Data Structures
Double-nested loop for bottom-up dp
Array of size 'amount'

### Steps
1. Intialize array of size 'amount' + 1. We do this because we need to also have a spot for 0 and 1 - amount
2. Set the first value (for 0) to 0 becaue that's how many coins needed
3. Iterate from 1 to amount (inclusive of amount). In each iteration, iterate over each coin
4. For each amount and coin pair, set the array at [amount] to equal the min of its current value and 1 + dp[amount-coin]
ONLY DO THIS IF amount-coin >= 0 

