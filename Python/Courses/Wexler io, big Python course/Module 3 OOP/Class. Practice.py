class File:
    def __init__(self, path, filename, extension="png"):
        self.path = path
        self.filename = filename
        self.extension = extension
        self.is_opened = False

    def __str__(self):  # returns a formatted path
        return f"{self.path}/{self.filename}.{self.extension}"

    def open(self):
        if self.is_opened:
            return f"Ошибка. Файл {self.__str__()} уже открыт"  # does not actually work, but the idea is solid
        else:
            self.is_opened = True

    def close(self):
        if self.is_opened == False:
            return f"Ошибка. Файл {str(self)} уже закрыт"
        else:
            self.is_opened = False


file1 = File(path="/Users", filename="test")
file2 = File(path="/Users/Docs", filename="test_1", extension="jpeg")

print(file1)
file1.open()
print(file1.is_opened)
file1.open()
print(file1.is_opened)
file1.close()
print(file1.is_opened)

