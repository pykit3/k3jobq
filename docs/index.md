# k3jobq

[![Action-CI](https://github.com/pykit3/k3jobq/actions/workflows/python-package.yml/badge.svg)](https://github.com/pykit3/k3jobq/actions/workflows/python-package.yml)
[![Documentation Status](https://readthedocs.org/projects/k3jobq/badge/?version=stable)](https://k3jobq.readthedocs.io/en/stable/?badge=stable)
[![Package](https://img.shields.io/pypi/pyversions/k3jobq)](https://pypi.org/project/k3jobq)

Concurrent job queue manager with multi-threading support. Process a series of inputs with worker functions concurrently.

k3jobq is a component of [pykit3](https://github.com/pykit3) project: a python3 toolkit set.

## Installation

```bash
pip install k3jobq
```

## Quick Start

```python
import k3jobq

def add1(args):
    return args + 1

def printarg(args):
    print(args)

# Process inputs through worker pipeline
k3jobq.run([0, 1, 2], [add1, printarg])
# Output:
# 1
# 2
# 3

# Use multiple threads for a worker
k3jobq.run(range(100), [add1, (printarg, 4)])  # 4 threads for printarg

# Keep results in order
k3jobq.run(range(10), [add1, printarg], keep_order=True)
```

## API Reference

::: k3jobq

## License

The MIT License (MIT) - Copyright (c) 2015 Zhang Yanpo (张炎泼)
