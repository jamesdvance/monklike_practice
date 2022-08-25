class Solution:
    def tribonacci(self, n: int) -> int:
        """
        The Tribonacci sequence Tn is defined as follows: 

        T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

        Given n, return the value of Tn.

        Base Cases:
        T0 = 0 
        0 <= n <= 37
        """
        if n ==0:
            return 0
        elif n <3:
            return 1

        trib_list = [0,1,1]

        for i in range(3, n+1):

            trib_list.append(trib_list[i-1]+trib_list[i-2]+trib_list[i-3])

        return trib_list[n]
