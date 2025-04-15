Python Package Template
=======================

This [cookiecutter](https://github.com/cookiecutter/cookiecutter)-based project template is designed
to rapidly generate new Python packages. In just a few seconds, you’ll receive a fully set-up python 
package following modern development approaches.

This template can serve as a foundational template for various types of projects.

Features:

- A modern toolchain that complies with the latest PEPs.
- Includes fully functional code snippets for your application.
- Configured pytest with examples of how to test asynchronous code.
- Makefile for basic package management operations.
- Enables linting, testing, building, and deploying with a single command.
- A fully functional boilerplate for a CLI application.
- Continuous integration configuration for GitHub Actions.

## Getting Started

1. Install `cookiecutter` and `uv`.
2. Generate a new python project.

```bash
$ pip install uv cookiecutter # You can use brew instead of pip
$ cookiecutter https://github.com/akopdev/template-python-package
```

Cookiecutter will prompt you for information regarding your package.

```
name (my_package): my_package
description (A short description of the package.): Awesome package.
author_name (Akop Kesheshyan): Akop Kesheshyan
author_email (devnull@akop.dev): devnull@akop.dev
github_username (akopdev): akopdev
version (0.1.0): 0.0.1
```

As a result, you’ll receive a fully functional package. 
```
my_package
├── src
│   └── my_package
│       ├── __init__.py
│       ├── cli.py
│       ├── my_package.py
│       ├── py.typed
│       └── settings.py
├── tests
│   ├── conftest.py
│   └── test_my_package.py
├── .gitignore
├── LICENSE
├── Makefile
├── pyproject.toml
└── README.md
```

Refer to the `make help` for a list of supported actions.
