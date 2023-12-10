class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        stack = []
        current = 1  # Start from the first element in the stream

        for num in target:
            while current < num:
                stack.append("Push")
                stack.append("Pop")
                current += 1

            stack.append("Push")
            current += 1

        return stack