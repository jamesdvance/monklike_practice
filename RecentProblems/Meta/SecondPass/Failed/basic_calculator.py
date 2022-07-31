"""
# " 3+5 / 2 "
# res =0
res = 0
cur_num =0
last_num =0
cur_num=3
res = 0
last_num = 3
cur_num=0
op=+
res = 3
last_num = 5
op="/"

"""
class Solution:
    def calculate(self, s: str) -> int:
        if len(s)==0:
            return 0
        cur_num, last_num, res = 0,0,0
        op = "+"
        s=s.rstrip()
        for i,c in enumerate(s):
            if c ==" ":
                continue
            elif c.is_digit():
                cur_num=cur_num*10+int(c)
            elif not c.is_digit() or i ==len(s)-1:
                if op in ["+","-"]:
                    res+=last_num 
                    last_num = -cur_num if op=="-" else cur_num
                elif op =="*":
                    last_num*=cur_num
                elif op=="/":
                    last_num = int(last_num/cur_num)
                op=char
                cur_num =0

        res+=last_num   
        return res
