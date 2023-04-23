import glob
import importlib
from typing import TypeVar, Generic, List

T = TypeVar('T')


class ClassLoader(Generic[T]):
    def __init__(self, path):
        self.path = path
        self.module_paths = glob.glob(path + '/*.py')

    def load(self) -> List[T]:
        for module_path in self.module_paths:
            module_name = module_path.split('/')[-1].split('.')[0]

            module = importlib.import_module(f'path.to.folder.{module_name}')
            classes = [getattr(module, cls) for cls in dir(module) if isinstance(getattr(module, cls), type)]

            return [instance for instance in classes]
