class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            # Check for collisions while moving to the right
            while stack and asteroid < 0 and stack[-1] > 0:
                if stack[-1] == abs(asteroid):
                    stack.pop()
                    break
                elif stack[-1] < abs(asteroid):
                    stack.pop()
                else:
                    break
            else:
                # No collision, add the asteroid to the stack
                stack.append(asteroid)

        return stack