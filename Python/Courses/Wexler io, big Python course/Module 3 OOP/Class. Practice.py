class File:
    def __init__(self, path, filename, extension="png"):
        self.path = path
        self.filename = filename
        self.extension = extension

    def __str__(self):  # returns a formatted path
        return f"{self.path}/{self.filename}.{self.extension}"



file1 = File(path="/Users", filename="test")
file2 = File(path="/Users/Docs", filename="test_1", extension="jpeg")

print(file1)
