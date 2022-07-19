# -*- coding: utf-8 -*-
# @File    : vos.py
"""
list some of dataclass
"""

from dataclasses import dataclass


def nested_dataclass(*args, **kwargs):
    """允许属性中有dataclasses类的装饰器"""

    def wrapper(cls):
        cls = dataclass(cls, **kwargs)
        original_init = cls.__init__

        def __init__(self, *args, **kwargs):
            for name, value in kwargs.items():
                field_type = cls.__annotations__.get(name, None)
                if is_dataclass(field_type) and isinstance(value, dict):
                    new_obj = field_type(**value)
                    kwargs[name] = new_obj
                if isinstance(value, list) and is_dataclass(field_type[0]):
                    res = []
                    for c in value:
                        new_obj = field_type[0](**c)
                        res.append(new_obj)
                    kwargs[name] = res
            original_init(self, *args, **kwargs)

        cls.__init__ = __init__
        return cls

    return wrapper(args[0]) if args else wrapper


@dataclass
class Demo:
    # 将没有标注类型的额外属性, 也可以用 对象.Attr 的形式调用
    @classmethod
    def from_kwargs(cls, **kwargs):
        # split the kwargs into native ones and new ones
        native_args, new_args = {}, {}
        for name, val in kwargs.items():
            if name in cls.__annotations__:
                native_args[name] = val
            else:
                new_args[name] = val

        # use the native ones to create the class ...
        ret = cls(**native_args)

        # ... and add the new ones by hand
        for new_name, new_val in new_args.items():
            setattr(ret, new_name, new_val)
        return ret
