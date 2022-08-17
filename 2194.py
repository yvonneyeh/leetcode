# 2194. Cells in a Range on an Excel Sheet
class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        a, b = map(str, s.split(":"))
        result = []
        r = range(ord(a[0]), ord(b[0])+1)
        for i in r:
            for j in range(int(a[-1]), int(b[-1])+1):
                result.append(chr(i)+str(j))
        return result
