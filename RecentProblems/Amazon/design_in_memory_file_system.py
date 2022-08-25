"""
Design a data structure that simulates an in-memory file system.

Implement the FileSystem class:

FileSystem() Initializes the object of the system.
List<String> ls(String path)
If path is a file path, returns a list that only contains this file's name.
If path is a directory path, returns the list of file and directory names in this directory.
The answer should in lexicographic order.
void mkdir(String path) Makes a new directory according to the given path. 
The given directory path does not exist. If the middle directories in the path do not exist, you should create them as well.
void addContentToFile(String filePath, String content)
If filePath does not exist, creates that file containing given content.
If filePath already exists, appends the given content to original content.
String readContentFromFile(String filePath) Returns the content in the file at filePath.



"""

"""
Sol 1. OOP - A node object which can serve as either file or folder
* Exposes staticmethods to update a given instance of a class, but not itself
"""

class Node():
	def __init__(self, name, nodeType):
		""" Initialize Children as a dictionary 
		Objects of type 'dir' have a children dictionary, all others have a string 'content'
		"""
		self.name = name
		self.type = nodeType
		self.children=None
		self.content = None
		if self.type='dir':
			self.children={}
		else:
			self.content = ''

	def updateFileTypeToDir(self):
		"Change Attributes from Content to Children"
		self.type='dir'
		self.children={}
		self.content = None 

	def updateFileTypeToFile(self):
		"Change Attributes From Children to Content"
		self.type='file'
		self.children=None
		self.content=''

	@staticmethod
	def traverseNode(root, path):
		""" 
		:1 Traverses to final file in path, starting at root
		:2 Creates a list of all child-folders or file names which are children of file
		:3 Returns list sorted 
		"""

		path=path.split("/")
		if path[0]=="":
			path.pop(0)

		resultList = []
		for p in path:
			root = root.children[p]
		if root.type=='dir':
			for child in root.children:
				resultList.append(child)
			else:
				resultList.append(root.name)
		resultList.sort()
		return resultList

	@staticmethod
	def makedir(root,path):
		"""
		Traverses each folder in a directory path
		:1 Iterates over each folder in the path
		:2 Updates root to the child that has the particular name in the path
		:3 Returns the final dir object in that path
		"""
		path=path.split("/")
		for p in path:
			if p in root.children:
				root=root.children[p]
			else: # Start building
				child=Node(p,"dir")
				root.children[p] = child 
				root = root.children[p]

		return root 

	@staticmethod
	def addContentToFile(root,path content):
		"""
		:1 Converts object to File if Dir
		:2 Ads a string to content
		"""
		file=Node.makedir(root, path)
		if file.type=='dir':
			file.updateFileTypeToFile()
		file.content+=content 

	@staticmethod
	def readContentFromFile(root, path):
		"""
		:1 Gets / makes the path
		:2 Returns the content of the final Node object
		"""	
		file=Node.makedir(root,path)
		return file.content

class FileSystem:

    def __init__(self):
    	self.root = Node("","dir")

    def ls(self, path: str) -> List[str]:
    	return Node.traverseNode(self.root, path[1:])        

    def mkdir(self, path: str) -> None: 
    	Node.makedir(self.root, path[1:])  

    def addContentToFile(self, filePath: str, content: str) -> None:
        Node.addContentToFile(self.root, filePath[1:],content)

    def readContentFromFile(self, filePath: str) -> str:
        return Node.readContentFromFile(self.root, filePath[1:])


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)


"""
Sol 2. OOP - A node object which can serve as either file or folder
* Exposes staticmethods to update a given instance of a class, but not itself
"""
class MemObject():
	
	def __init__(self, abs_path:str):
		self.abs_path = abs_path 

	def get_object_name(self, abs_path):
		last_slash = abs_path.rindex("/") # find last instance of "/"
		return abs_path[last_slash+1:]

	def __repr__(self)->str:
		return f"MemObject({self.abs_path})"

class File(MemObject):
	def __init__(self, abs_path):
		super().__init__(abs_path)
		self.content=""

	def append_content(self,content):
		self.content+=content 

class Folder(MemObject):
	def __init__(self):
		super.__init__(abs_path)
		self.files: list[File] = []
		self._file_name_to_index={}
		self.folders: list[Folder] = []
		self._folder_name_to_index = {}
		self.items: list[FSObject] = [] 

	def create_dir(self, abs_path):
		new_dir = Folder(abs_path)
		self.folders.append(new_dir)
		self._folder_name_to_index[new_dir.name] = len(self.folders)-1 

	def 

class FileSystem:

    def __init__(self):

    def ls(self, path: str) -> List[str]:    

    def mkdir(self, path: str) -> None:

    def addContentToFile(self, filePath: str, content: str) -> None:

    def readContentFromFile(self, filePath: str) -> str: