import builtins


_original_build_class = builtins.__build_class__


def _british_build_class(func, name, *bases, **kwargs):
    cls = _original_build_class(func, name, *bases, **kwargs)

    namespace = cls.__dict__

    if "__innit__" in namespace and "__init__" not in namespace:
        cls.__init__ = namespace["__innit__"]

    elif "__init__" in namespace and "__innit__" not in namespace:
        cls.__innit__ = namespace["__init__"]

    return cls


def install():
    if getattr(builtins.__build_class__, "__pythinnit__", False):
        return

    _british_build_class.__pythinnit__ = True
    builtins.__build_class__ = _british_build_class
