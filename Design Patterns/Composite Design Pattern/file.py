from file_systen_component import FileSystemComponent

class File(FileSystemComponent):

    def __init__(self, name, size) -> None:
        self.name = name
        self.size = size

    def get_size(self) -> int:
        return self.size
    
    def display(self, indent = 0):
        print(' ' * indent + f"📃 {self.name}, Size: {self.size} bytes")
