import glob
import importlib
import os
from typing import TypeVar, Generic, List

T = TypeVar('T')


# TODO : Fazer funcionar algum dia

class ClassLoader(Generic[T]):
    def __init__(self, path):
        self.path = path
        self.module_paths = glob.glob(path + '/*.py')

    def load(self) -> List[T]:
        for module_path in self.module_paths:
            module_name = module_path.replace('\\', '/').replace('/', os.sep).split(os.sep)[-1].split('.')[0]

            module = importlib.import_module(module_name)
            classes = [getattr(module, cls) for cls in dir(module) if isinstance(getattr(module, cls), type)]

            return [instance for instance in classes]
