import os

class Solution:
  def simplifyPath(self, path: str) -> str:
    stack = []

    # Split path into segments and process each segment
    for segment in path.split('/'):
      if segment in ('', '.'):
        # Skip empty or current directory segments
        continue
      if segment == '..':
        # If the segment is a parent directory, pop the last directory from the stack
        if stack:
          stack.pop()
      else:
        # Otherwise, add the segment to the stack
        stack.append(segment)

    # Join the remaining directory segments with '/'
    simplified_path = '/' + '/'.join(stack)

    # Use os.path to simplify the path further
    return os.path.abspath(simplified_path)