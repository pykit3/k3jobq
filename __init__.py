"""
k3jobq is a manager to create concurrent tasks.
It processes a series of inputs with functions concurrently and
return once all threads are done::

    def add1(args):
        return args + 1

    def printarg(args):
        print(args)

    k3jobq.run([0, 1, 2], [add1, printarg])
    # > 1
    # > 2
    # > 3
"""

from .jobq import (
    EmptyRst,
    Finish,
    JobManager,
    JobWorkerError,
    JobWorkerNotFound,
    run,
    stat,
)
from .works import (
    limit_job_speed,
)

__all__ = [
    "EmptyRst",
    "Finish",
    "JobManager",
    "JobWorkerError",
    "JobWorkerNotFound",
    "limit_job_speed",
    "run",
    "stat",
]


def __getattr__(name: str) -> str:
    # importlib.metadata takes about 20 ms to import, so it is loaded only
    # when __version__ is read
    if name != "__version__":
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

    from importlib.metadata import version

    return version("k3jobq")
