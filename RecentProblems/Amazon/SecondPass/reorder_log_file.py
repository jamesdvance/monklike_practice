class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        def get_key(log:str)->tuple:
            id_, val = log.split(" ",maxsplit=1)
            return (0,val, id_) if val[0].isalpha() else (1,0)

        return sorted(logs, key=lambda x: get_key(x))
