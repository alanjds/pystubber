pystubber
=========

What differs from `mypy stubgen`?

As mypy's `stubgen -m random` generates the following for the `random` module: 

```python
class Random(_random.Random):
    VERSION: int = ...
    gauss_next: Any = ...
    def __init__(self, x: Optional[Any] = ...) -> None: ...
    def seed(self, a: Optional[Any] = ..., version: int = ...) -> None: ...
    def getstate(self): ...
    def setstate(self, state: Any) -> None: ...
    def __reduce__(self): ...
    def randrange(self, start: Any, stop: Optional[Any] = ..., step: int = ..., _int: Any = ...): ...
    def randint(self, a: Any, b: Any): ...
    def choice(self, seq: Any): ...
...
```

`pystubber random` instead generates:

```py
#!/usr/bin/env python  # [module random]
"""
Random variable generators.
...
"""
__all__ = ['Random', 'seed', 'random', 'uniform', 'randint', 'choice', 'sample', 'randrange', 'shuffle', 'normalvariate', 'lognormvariate', 'expovariate', 'vonmisesvariate', 'gammavariate', 'triangular', 'gauss', 'betavariate', 'paretovariate', 'weibullvariate', 'getstate', ...]

class Random(_random.Random):
    def __getstate__(self):
        """
        # Issue 17489: Since __reduce__ was defined to fix #759889 this is no
        # longer called; we leave it here because it has been here since random was
        # rewritten back in 2001 and why risk breaking something.
        """
        raise NotImplementedError()

    def __init__(self, x=None):
        """
        Initialize an instance.

        Optional argument x controls seeding, as for Random.seed().
        """
        raise NotImplementedError()

    def __reduce__(self):
        """
        helper for pickle
        """
        raise NotImplementedError()
...
```
