from file_systen_component import FileSystemComponent

class Directory(FileSystemComponent):

    def __init__(self, name) -> None:
        self.name = name
        self.components: list[FileSystemComponent] = []

    def get_size(self) -> int:
        total_size = sum(component.get_size() for component in self.components)
        return total_size

    def add_component(self, component: FileSystemComponent):
        self.components.append(component)

    def display(self, indent = 0):
         print(' ' * indent + f"📂 {self.name}")
         for component in self.components:
             component.display(indent + 3)