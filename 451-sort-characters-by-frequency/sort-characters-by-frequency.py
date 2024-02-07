class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        op = ""
        for i in sorted(count.items(), key=lambda item: item[1], reverse=True):
            op += i[0] * i[1]
        return op
        