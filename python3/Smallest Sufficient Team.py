from typing import List

class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        # Create a mapping of skills to their indices
        skills = {skill: i for i, skill in enumerate(req_skills)}
        n = len(req_skills)

        # Create a bitmask for each person indicating their skills
        p = [0] * len(people)
        for i, x in enumerate(people):
            for r in x:
                p[i] |= 1 << skills.get(r, 0)

        # Initialize the dynamic programming arrays
        f = [float('inf')] * (1 << n)  # Minimum team size for each skill combination
        g = [(-1, -1)] * (1 << n)  # Track the previous state and person index for each skill combination
        f[0] = 0  # Base case: no skills required, team size is 0

        # Dynamic programming to find the optimal team
        for i, x in enumerate(p):
            for j in range((1 << n) - 1):
                if f[j | x] > f[j] + 1:
                    f[j | x] = f[j] + 1
                    g[j | x] = (j, i)

        # Trace back the optimal team from the final state
        res = []
        j = (1 << n) - 1
        while j > 0:
            res.append(g[j][1])
            j = g[j][0]

        return res