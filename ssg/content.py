import re
from yaml import load
from yaml import FullLoader
from collections.abc import Mapping

class Content(Mapping):
    __delimiter = r"^(?:-|\+){3}\s*$"
    __regex  = re.compile(__delimiter, re.MULTILINE)

    @classmethod
    def load(self, cls, string):
        cls.__regex = split(string, 2)
        _ = cls.__regex
        fm = cls.__regex
        content = cls.__regex

        self.load(fm)
        return cls(metadata, content)


