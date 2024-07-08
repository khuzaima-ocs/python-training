from abc import ABCMeta, abstractmethod

class FileSystemComponent(metaclass = ABCMeta):

    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def get_size(self) -> int:
        pass

    @abstractmethod
    def display(self) -> None:
        pass


class File(FileSystemComponent):

    def __init__(self, name, size) -> None:
        self.name = name
        self.size = size

    def get_size(self) -> int:
        return self.size
    
    def display(self, indent = 0):
        print(' ' * indent + f"📃 {self.name}, Size: {self.size} bytes")


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

    
d1 = Directory("Python Training")
d2 = Directory("Codes")
d3 = Directory("Todo")
d4 = Directory("eShop")
d5 = Directory("Design Patterns")

f1 = File("filter.py", 120)
f2 = File("sockets.py", 80)
f3 = File("app.py", 300)
f4 = File("index.py", 256)
f5 = File("Singleton.py", 72)
f6 = File("Proxy.py", 80)

d1.add_component(d2)
d1.add_component(d3)
d1.add_component(d4)

d2.add_component(d5)
d2.add_component(f1)
d2.add_component(f2)

d3.add_component(f3)
d4.add_component(f4)

d5.add_component(f5)
d5.add_component(f6)

d1.display()

print()
print(f'Size of Folder {d1.name} : {d1.get_size()} bytes')
print(f'Size of Folder {d2.name} : {d2.get_size()} bytes')