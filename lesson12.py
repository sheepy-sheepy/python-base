class FileOpener:
    def __init__(self, file_path: str, mode: str, encoding: str):
        self.file_path = file_path
        self.mode = mode
        self.encoding = encoding

    def __enter__(self):
        self.file = open(self.file_path, self.mode, encoding=self.encoding)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        print(f"Ошибка внутри with: {exc_type}, текст: {exc_val}")
        return True


with FileOpener("data.txt", "r", "utf-8") as file:
    print(file.read())
    print(10 / 0)
