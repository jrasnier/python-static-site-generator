from pathlib import Path

class Site:
    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path):
        directory = self.dest / relative_to(self.source)
        self.directory.mkdir(parent=True, exist_ok=True)

    def build():
        self.dest.mkdir(parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if Path.is_dir():
                self.create_dir(path)
