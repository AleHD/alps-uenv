# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyFlashAttn(PythonPackage):
    """
    This package provides the official implementation of FlashAttention.
    """

    pypi = "flash-attn/flash_attn-2.5.4.tar.gz"

    maintainers("aurianer")

    license("BSD")

    version("2.5.8", sha256="2e5b2bcff6d5cff40d494af91ecd1eb3c5b4520a6ce7a0a8b1f9c1ed129fb402")
    version("2.5.7", sha256="7c079aef4e77c4e9a71a3cd88662362e0fe82f658db0b2dbff6f279de2a387a8")
    version("2.5.5", sha256="751cee17711d006fe7341cdd78584af86a6239afcfe43b9ed11c84db93126267")
    version("2.5.4", sha256="d83bb427b517b07e9db655f6e5166eb2607dccf4d6ca3229e3a3528c206b0175")

    depends_on("py-setuptools", type="build")

    with default_args(type=("build", "run")):
        depends_on("py-torch+cuda")
        depends_on("py-ninja")
        depends_on("py-einops")
        depends_on("py-packaging")

    depends_on("py-psutil", type="build")
    depends_on("py-pybind11", type="build")

    depends_on("python@3.7:", type=("build", "run"))
