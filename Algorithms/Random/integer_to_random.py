
class Solution:

    def __init__(self):
        self.divisors = [1000,500, 100,  50, 10, 5, 1 ]
        self.numerals = ["M","D","C", "L","X", "V","I"]
        self.prefixes = {1:"I", 2:"X", 3: "C"}
        self.roman = ""

    def intToRoman(self, num):
        self.process_digit(num,0)
        return self.roman

    def process_digit(self, num:int, index:int)->int:

        if index == len(self.numerals):
            return 

        divisor = self.divisors[index]
        value = num // divisor
        str_num = str(num)
        first_digit = int(str_num[0])

        if (value > 0 ) :
            # Get max value
            if first_digit in (4,9):
                prefix = self.prefixes[len(str_num)]
                i = index

                self.roman += prefix + self.numerals[i-1]
                divisor = self.divisors[i-1] - (10**(len(str_num)-1))
                if divisor == 0:
                    return


            else:
                start = 1 if value < 4 else 5
                # loop_val = value
                loop_roman = ""
                step_size =1 

                for i in range(1, value+1, step_size): 
                    loop_roman += self.numerals[index]

                self.roman += loop_roman
                            
        num %= divisor
        if num ==0:
            return 

        return self.process_digit(num, index+1)