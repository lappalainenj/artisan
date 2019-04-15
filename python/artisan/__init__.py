''' A build system for explainable science '''

from ._artifacts import Artifact, ArrayFile, EncodedFile
from ._configurable import Configurable
from ._global_conf import Conf, ConfStack, conf_stack
from ._http import serve

__all__ = [
    'Configurable', 'Artifact',
    'ArrayFile', 'EncodedFile',
    'Conf', 'ConfStack', 'conf_stack',
    'serve'
]

#-- `__module__` rebinding ----------------------------------------------------

for sym in __all__:
    obj = globals()[sym]
    if hasattr(obj, '__module__'):
        obj.__module__ = __name__

#-- Wonky alias docstring definitions -----------------------------------------

ArrayFile = ArrayFile; 'An alias for `h5py.Dataset`' # type: ignore
EncodedFile = EncodedFile; 'An alias for `pathlib.Path`' # type: ignore