pkgname = "lean"
pkgver = "4.33.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DUSE_MIMALLOC=OFF",
    "-DINSTALL_CADICAL=OFF",
    "-DINSTALL_LEANTAR=OFF",
]
make_cmd = "make"
make_dir = "build/release"
hostmakedepends = ["bash", "gmake", "cmake", "cadical", "pkgconf", "leantar"]
makedepends = ["gmp-devel", "libuv-devel", "openssl3-devel", "llvm-devel"]
pkgdesc = "Lean programming language and theorem prover"
license = "Apache-2.0"
url = "https://lean-lang.org"
source = (
    f"https://github.com/leanprover/lean4/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "348d0839049a7cbb72b5e82196670e4ded6e1f8ec4610cd6c5188b2754a1f24c"


@subpackage("lean-devel-static")
def _(self):
    return ["usr/lib/lean/*.a"]


@subpackage("lean-devel")
def _(self):
    return self.default_devel()
