class Solution:
    def simplifyPath(self, path: str) -> str:
        chars = path.split('/')
        new_dirs = []
        for char in chars:
            if char == '':
                continue
            elif char == '.':
                continue
            elif char == '..':
                if len(new_dirs) > 0:
                    new_dirs.pop()
            else:
                new_dirs.append(char)
        ans = ['']
        ans += new_dirs
        return '/'.join(ans) if len(ans) > 1 else '/'