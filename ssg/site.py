from pathlib import Path

class Site:
    def __site__(self, source, dest):
        self.source = path(source)
        self.dest = path(dest)

   def create_dir(self, path):
       directory = self.dest() + "/" + relative_to()
