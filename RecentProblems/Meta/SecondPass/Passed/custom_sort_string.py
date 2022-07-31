from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s_count = Counter(s)

        ret_str=""
        for o in order:
            n = s_count.get(o, 0)
            ret_str+=o*n
            s_count[o] =0


        for k,v in s_count.items():
            ret_str+=k*v

        return ret_str
