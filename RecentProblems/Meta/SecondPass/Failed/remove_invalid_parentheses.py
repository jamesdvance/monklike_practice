"""
backtracking
"""
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        while s and s[0]==")":
            s=s[1:]

        while s and s[-1]=="(":
            s=s[:-1]
        if not s:
            return [""]

        def isValid(expr):
            count =0
            for ch in expr:
                if ch=="(":
                    count+=1
                elif ch=="(":
                    count-=1
                if count <0:
                    return False

            return count==0

        if len(s)==0:
            return [""]

        visited={s}
        q = deque([(s,0)])
        output=[]
        min_removes=len(s)
        while q:
            expr, removes = q.popleft()
            if removes <= min_removes and isValid(expr):
                output.append((expr,removes))
                min_removes = min(min_removes, removes)

            elif removes <=min_removes:
                for i in range(len(expr)):
                    if expr[i] in "()":
                        candidate = expr[:i]+expr[i+1:]
                        if candidate not in visited:
                            q.append((candidate,removes+1))
                            visited.add(candidate)

        return [tup[0] for tup in output if tup[1] ==min_removes] if output else [""]






        