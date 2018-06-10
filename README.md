# LV_binary_files

![GPLv3-only License](https://img.shields.io/badge/License-GPLv3--only_License-lightgray)  ![Planning](https://img.shields.io/badge/Status-Planning-blue)

## Table of Contents

- [Short hatch explanation](#short-hatch-explanation)
- [License](#license)

## Short hatch explanation

**Please exchange this short explanation with your own documentation.**

Unfortunately there are some issues with hatch on GSI windows machines. Therefore, it has to be used under WSL (Windows Subsystem for Linux).

0. Search for `WSL` or `Ubuntu` in the GSI software center and install the found `Ubuntu 20.04`.

*All the following commands ar to be executed in the WSL environment.*

1. Install hatch with `pip install hatch`, where the assumption is made, that python is installed already.
2. Modify the `.bashrc` to add `.local` to the PATH variable. Afterwards restart the shell for the changes to function.
3. You are done and should be able to use hatch. Try `hatch --version`.

The following commands are supported by this project template:
- `hatch run test:cov`: This runs the tests for the project and also reports on the test coverage.
- `hatch run lint:all`: This runs the linter telling where the code style can be / should be improved.
- `hatch run lint:fix`: This applies any automatic fixes, which are possible to do for the code.
- `hatch build`: Build the package into a .wheel and .tar.gz file.
- `hatch run docs:generate` and `hatch run docs:build`: These commands run one after the other build the documentation for the project from the docstrings in the code.
- `hatch run docs:serve`: This serves the documentation on a local webserver (http://localhost:8000).

All these commands are also included in the `run.sh` file, which executes the hatch commands in order to perform the tests, linting, building and documentation generation.


## License

LV_binary_files is distributed under the terms of the [GPL-3.0-only](https://spdx.org/licenses/GPL-3.0-only.html) license.
