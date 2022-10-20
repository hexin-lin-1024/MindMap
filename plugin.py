import os
import inspect
import imp

def load_plugins(path):
    plugins = {}
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            if name == "main.py":
                module = imp.load_source("", os.path.join(root, name))
                plugins[os.path.basename(root)] = {k.__name__ : k for k in [module.__getattribute__(j) for j in module.__dir__()] if inspect.isclass(k)}
    return plugins

print(load_plugins("./plugins"))