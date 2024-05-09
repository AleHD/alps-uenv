# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PyDacite(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://github.com/konradhalas/dacite"

    # Github link because source code is not available from PyPI.
    url = "https://github.com/konradhalas/dacite/archive/refs/tags/v1.8.1.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="github_user1")

    version("1.8.1", sha256="791ac3da85a040684a96df59e2320dc7b3cac000ff536e3f4b00fb3b67520b86")
    version("1.8.0", sha256="b52134bf47548d4c5ce92379662f88ce28237c5fe2b45ade4093231afa85ad08")
    version("1.7.0", sha256="2b33e37f9c167c9485e63d86c5964359487aa3f2f0a4773102378bb7fd35c0eb")

    # FIXME: Only add the python/pip/wheel dependencies if you need specific versions
    # or need to change the dependency type. Generic python/pip/wheel dependencies are
    # added implicity by the PythonPackage base class.
    # depends_on("python@2.X:2.Y,3.Z:", type=("build", "run"))
    # depends_on("py-pip@X.Y:", type="build")
    # depends_on("py-wheel@X.Y:", type="build")

    depends_on("py-setuptools", type="build")

    def config_settings(self, spec, prefix):
        # FIXME: Add configuration settings to be passed to the build backend
        # FIXME: If not needed, delete this function
        settings = {}
        return settings
