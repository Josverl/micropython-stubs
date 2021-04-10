import sys
import warnings

import importlib


_import_hook = None
_import_exts = []


class ImphookFileLoader(importlib._bootstrap_external.FileLoader):

    def create_module(self, spec):
        global _import_hook
        #print("create_module", spec)
        basename = spec.origin.rsplit(".", 1)[0]
        m = _import_hook(spec.name, basename)
        return m

    def exec_module(self, mod):
        # Module is fully populated in create_module
        pass


def setimphook(hook, exts):
    global _import_hook
    old_hook = _import_hook
    _import_hook = hook
    _import_exts.extend(exts)

    for i, el in enumerate(sys.path_hooks):
        if not isinstance(el, type):
            # Assume it's a type wrapped in a closure,
            # as is the case for FileFinder.
            el = type(el("."))
        if el is importlib._bootstrap_external.FileFinder:
            sys.path_hooks.pop(i)
            insert_pos = i
            break
    else:
        warnings.warn("Could not find existing FileFinder to replace, installing ours as the first to use")
        insert_pos = 0

    # Mirrors what's done by importlib._bootstrap_external._install(importlib._bootstrap)
    loaders = [(ImphookFileLoader, _import_exts)] + importlib._bootstrap_external._get_supported_file_loaders()
    # path_hook closure captures supported_loaders in itself, all instances
    # of FileFinder class will be created with it.
    sys.path_hooks.insert(insert_pos, importlib._bootstrap_external.FileFinder.path_hook(*loaders))
    sys.path_importer_cache.clear()
    return old_hook


sys.setimphook = setimphook
