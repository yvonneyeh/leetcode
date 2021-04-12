# 1672. Richest Customer Wealth

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:

# loop through range of accounts, length
# find sum of all nested list values to find wealth of person
# if total wealth is more than max wealth => update max

        max_wealth = 0
        for i in range(len(accounts)):
            total_wealth = sum(accounts[i])
            max_wealth = max(max_wealth, total_wealth)
        return max_wealth
