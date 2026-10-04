from importlib.metadata import version

__version__ = version("k3jobq")

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
