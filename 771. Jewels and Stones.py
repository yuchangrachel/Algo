"""
    Question:count how many char in jewels in stones. case sensitive
"""
def numJewelsInStones(self, jewels: str, stones: str) -> int:
    return sum(1 if stone in jewels else 0 for stone in stones)