from typing import List
from pathlib import Path

class Parser():
    extensions: List[str] = []

    def valid_extension(self, extension):
        return extension in self.extensions

    def parse(path, source, dest):
        path: Path[]
        source: Path[]
        dest: Path[]
