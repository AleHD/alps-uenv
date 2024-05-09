from spack.package import *


class PyPyarrowHotfix(PythonPackage):
    homepage = "https://github.com/pitrou/pyarrow-hotfix"
    pypi = "pyarrow-hotfix/pyarrow_hotfix-0.6.tar.gz"

    version("0.6", sha256="79d3e030f7ff890d408a100ac16d6f00b14d44a502d7897cd9fc3e3a534e9945")

    depends_on("py-setuptools", type="build")
    depends_on("py-hatchling", type="build")
    depends_on("py-pyarrow", type="build")
