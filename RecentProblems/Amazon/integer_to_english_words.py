"""
Integer To English Words
Convert a non-negative integer num to its English words representation.


Input: num = 123
Output: "One Hundred Twenty Three"

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Hints: Group by 3 digits, write helper that takes # less than 1000 and converts to chunk of words
Hints: Create many testcases for edge cases

Edge cases:
0 ->Zero
100 -> One + Hundred
11, 12. All teens

1000
i=3
i=4 = -1

"""

class Solution:
	def __init__(self):
		self.digs = {"0":
			{"0":"handle",
			"1":"One",
			"2":"Two",
			"3":"Three",
			"4":"Four",
			"5":"Five",
			"6":"Six",
			"7":"Seven",
			"8":"Eight",
			"9":"Nine",
			"10":"Ten",
			"11":"Eleven",
			"12":"Twelve",
			"13":"Thirteen",
			"14":"Fourteen",
			"15":"Fifteen",
			"16":"Sixteen",
			"17":"Seventeen",
			"18":"Eighteen",
			"19":"Nineteen"},
			"1":{
				"2":"Twen",
				"3":"Thir",
				"4":"For",
				"5":"Fif",
				"6":"Six",
				"7":"Seven",
				"8":"Eigh",
				"9":"Nine"
			},
			"3":{
				0:"",
				1:" Thousand",
				2:" Million",
				3:" Billion",
			}
		}


	def numberToWords(self, num: int) -> str:
		if not num:
			return "Zero"

		return_str = ""
		bill = num//10**9
		mill = (num-bill*10**9)//10**6
		thous = (num-bill*10**9-mill*10**6)//1000
		rest = num - bill*10**9 - mill *10**6 - thous*1000

		if bill:
			return_str+=self._sub_thou(str(bill)) + " Billion"
		if mill:
			return_str += " " if return_str else ""
			return_str+=self._sub_thou(str(mill))+" Million"
		if thous:
			return_str += " " if return_str else ""
			return_str+=self._sub_thou(str(thous))+ " Thousand"
		if rest:
			return_str += " " if return_str else ""
			return_str += self._sub_thou(str(rest))
		return return_str

	def _sub_thou(self, lil_num:str)->str:
		"""
		0-19, use a simple look-up
		20 - 99, use a prefix + digit
		100-999,use a prefix + two digit
		"""
		if lil_num=="000":
			return ""
		if len(lil_num)==1:
			return self.digs["0"][lil_num] if lil_num != "0" else "Zero"
		elif len(lil_num)==2:
			return self._two_digit(lil_num)
		else:

			return (self.digs["0"][lil_num[0]] +" Hundred" + self._two_digit(lil_num[1:])).rstrip()

	def _two_digit(self,two_dig:str)->str:
		if two_dig == "00" or two_dig=="000":
			return ""
		if int(two_dig) < 20:
			return self.digs["0"][two_dig]
		else:
			ones_col = " "+self.digs["0"][two_dig[1]] if two_dig[1] != "0" else ""
			return self.digs["1"][two_dig[0]]+"ty"+ones_col