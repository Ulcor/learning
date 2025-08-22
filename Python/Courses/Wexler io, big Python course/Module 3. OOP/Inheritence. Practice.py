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
        if not self.is_opened:
            return f"Ошибка. Файл {str(self)} уже закрыт"
        else:
            self.is_opened = False

    def read(self):
        if self.is_opened:
            return self.filename
        else:
            return f"Ошибка чтения. Файл {str(self)} закрыт"


class VideoFile(File):
    def __init__(self, path, filename, extension="png", length="0:00"):
        super().__init__(path, filename, extension)
        self.length = length

# parent class method summon # 1
    def read(self):
        res = super().read()
        if res == self.filename:  # if success
            return f"Показываем {self.filename}"
        return res  # un-success

# parent class method summon # 2
#     def get_read_error(self):  # Этот метод определяем в классе File
#        return f"Ошибка чтения. Файл {str(self)} закрыт"
#
#     def read(self):
#         if not self.is_opened:
#             return self.get_read_error()
#         return f"Показываем {self.filename}"


file1 = File(path="/Users", filename="test")
file2 = File(path="/Users/Docs", filename="test_1", extension="jpeg")

print(file1)
file1.open()
print(file1.is_opened)
file1.open()
print(file1.is_opened)
file1.close()
print(file1.is_opened)

video_file = VideoFile('top_movies', 'XXX10', 'mkv', '97:00')

