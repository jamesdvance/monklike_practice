"""
DO THIS
"""
from enum import Enum 

class CarSize(Enum):
	BIG = 1 
	MEDIUM = 2
	SMALL = 3

class ParkingSystem:

	def __init__(self, big:int, medium:int, small:int):
		self.d = {}
		self.d[CarSize.BIG] = big
		self.d[CarSize.MEDIUM]= medium
		self.d[CarSize.SMALL]=small 

	def addCar(self, carType:int)->bool:
		if self.d[CarSize(carType)]:
			self.d[CarSize(carType)]-=1
			return True 
		return False




"""
DON'T DO THIS!
"""

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self._1 = big 
        self._2 = medium
        self._3 = small

    def addCar(self, carType: int) -> bool:
        cap = getattr(self,"_"+str(carType))
        if cap >0:
            setattr(self,"_"+str(carType), cap-1)
            return True 
        else:
            return False
            