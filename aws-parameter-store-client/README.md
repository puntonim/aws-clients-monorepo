**AWS Clients monorepo: AWS Parameter Store Client**
====================================================

Just a Python client for AWS Parameter Store.\
It is a wrapper around (and an interface to) boto3.


Usage
=====

---

See top docstrings in [aws_parameter_store_client.py](aws_parameter_store_client/aws_parameter_store_client.py).

Local dir install
-----------------
To install this client in a Poetry project, from a local dir, add this to `pyproject.toml`:
```toml
[project]
...
dependencies = [
    "aws-parameter-store-client @ ../aws-parameter-store-client"
    # "aws-parameter-store-client @ file:///Users/myuser/workspace/aws-clients-monorepo/aws-parameter-store-client"
]

[tool.poetry.dependencies]
# This section is required only when there are editable (develop = true) dependencies.
aws-parameter-store-client = {develop = true}
```

Github install
--------------
To install this client in a Poetry project, from Github, add this to `pyproject.toml`:
```toml
[project]
...
dependencies = [
    "aws-parameter-store-client @ git+https://github.com/puntonim/aws-clients-monorepo#subdirectory=aws-parameter-store-client",
]
```

Pip install
-----------
```sh
$ pip install "aws-parameter-store-client @ git+https://github.com/puntonim/aws-clients-monorepo#subdirectory=aws-parameter-store-client"
```


Development setup
=================

---

See [README.md](../README.md) in the root dir.
