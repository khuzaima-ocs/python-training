from contextlib import contextmanager

@contextmanager
def filestream(path, mode):
    file = open(path, mode)
    yield file
    file.close()

with filestream("context_manager.txt", "w") as f:
    f.write("Hello, I am writing this inside ")
    print(f.closed)

print(f.closed)