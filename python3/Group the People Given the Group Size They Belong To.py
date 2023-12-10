class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = {}
        result = []

        # Iterate through the groupSizes array
        for i, size in enumerate(groupSizes):
            if size not in groups:
                groups[size] = []  # Create a new group if it doesn't exist
            groups[size].append(i)  # Add person i to the group

            # If the group is full, add it to the result and reset it
            if len(groups[size]) == size:
                result.append(groups[size])
                groups[size] = []

        return result