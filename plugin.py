import os
import inspect
import imp

plugins = {}

for root, dirs, files in os.walk("./plugins", topdown=False):
    for name in files:
        if name == "main.py":
            module = imp.load_source("", os.path.join(root, name))
            plugins[os.path.basename(root)] = [k for k in [module.__getattribute__(j) for j in module.__dir__()] if inspect.isclass(k)]

imp.load_source
imp.load_module

for i in plugins.keys():
    print(i)
    for j in plugins[i]:
        j()