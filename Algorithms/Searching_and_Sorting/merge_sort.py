class Sorter():

	def mergeSort(self, array:list)->list:
		if len(array) == 1:
			return array 

		middleIdx = len(array)//2
		leftarr = array[:middleIdx]
		rightarr = array[middleIdx:]
		return self.mergeSortedArrays(mergeSort(rightarr), mergeSort(leftarr))


	def mergeSortedArrays(self, arr1:list, arr2:list)->list:
		sortedArray = [None] * (len(rightarr)+len(leftarr))
		k = i = j = 0
		while i < len(leftarr) and j < len(rightarr):
			if leftarr[i] <= rightarr[j]:
				sortedArray[k] = leftarr[i]
				i+=1
			else:
				sortedArray[k] = rightarr[j]
				j+=1 

			k+=1 

		# Address leftover left

		# sortedArray = sortedArray[:k]+leftarr[i:] # seems like should work
		while i < len(leftarr):
			sortedArray[k] = leftarr[i]
			i+=1
			k+=1

		while j < len(rightarr):
			sortedArray[k] = rightarr[j]
			j+=1
			k+=1

		return sortedArray