# Copyright (c) 2025, GSI Helmholtzzentrum für Schwerionenforschung GmbH
# LV_binary_files is distributed under the terms of the [GPL-3.0-only] https://spdx.org/licenses/GPL-3.0-only.html license.

import sys

# check python version: if below 3.8 use a different import syntax of will fail
if sys.version_info >= (3, 8):
    from importlib.metadata import PackageNotFoundError, version
else:
    from importlib_metadata import PackageNotFoundError, version

try:
    __version__ = version('LV_binary_files')
except PackageNotFoundError:  # pragma: no cover
    __version__ = 'unknown'
finally:
    del version, PackageNotFoundError
