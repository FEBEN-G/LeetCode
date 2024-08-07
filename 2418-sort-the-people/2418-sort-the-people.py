class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        return [p[0] for p in sorted(zip(names, heights), key=lambda person: -person[1])]