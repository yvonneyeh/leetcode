# 1743. Restore the Array From Adjacent Pairs
# Medium
# You are given a 2D integer array adjacentPairs of size n - 1 where each adjacentPairs[i] = [ui, vi] indicates that the elements ui and vi are adjacent in nums.
# It is guaranteed that every adjacent pair of elements nums[i] and nums[i+1] will exist in adjacentPairs, either as [nums[i], nums[i+1]] or [nums[i+1], nums[i]]. The pairs can appear in any order.
# Return the original array nums. If there are multiple solutions, return any of them.

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        def dfs(u):
            result.append(u)
            seen.add(u)
            for v in graph[u]:
                if v not in seen:
                    dfs(v)

        graph = collections.defaultdict(list)

        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)

        for k, v in graph.items():
            if len(v) == 1:
                start = k
                break

        seen = set()
        result = []

        dfs(start)

        return result

# Runtime: 1284 ms, faster than 17.44% of Python3 online submissions for Restore the Array From Adjacent Pairs.
# Memory Usage: 182.6 MB, less than 7.44% of Python3 online submissions for Restore the Array From Adjacent Pairs.


class Solution1:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = {}
        for u, v in adjacentPairs:
            graph.setdefault(u, []).append(v)
            graph.setdefault(v, []).append(u)

        ans = []
        seen = set()
        stack = [next(x for x in graph if len(graph[x]) == 1)]
        while stack:
            n = stack.pop()
            ans.append(n)
            seen.add(n)
            for nn in graph[n]:
                if nn not in seen: stack.append(nn)
        return ans


# Runtime: 1128 ms, faster than 51.86% of Python3 online submissions for Restore the Array From Adjacent Pairs.
# Memory Usage: 63.1 MB, less than 66.05% of Python3 online submissions for Restore the Array From Adjacent Pairs.
