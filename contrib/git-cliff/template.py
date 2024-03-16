pkgname = "git-cliff"
pkgver = "2.1.2"
pkgrel = 1
build_style = "cargo"
make_check_args = [
    "--",
    "--skip=repo::test::git_log",
    "--skip=repo::test::git_tags",
    "--skip=repo::test::git_upstream_remote",
]
hostmakedepends = ["cargo", "pkgconf"]
makedepends = ["libgit2-devel"]
pkgdesc = "Changelog generator for conventional commits"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "Apache-2.0 OR MIT"
url = "https://github.com/orhun/git-cliff"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "1c321b180b071ccfa8986931576fc02ca4dbc75dff035e4c663c2cfb8ecd4683"
# generates manpages/completions with host bins
options = ["!cross"]


def post_build(self):
    self.do(
        f"target/{self.profile().triplet}/release/git-cliff-mangen",
        env={"OUT_DIR": "."},
    )
    self.do(
        f"target/{self.profile().triplet}/release/git-cliff-completions",
        env={"OUT_DIR": "."},
    )


def do_install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/git-cliff")
    self.install_man("git-cliff.1")
    self.install_completion("git-cliff.bash", "bash")
    self.install_completion("git-cliff.fish", "fish")
    self.install_completion("_git-cliff", "zsh")
    self.install_license("LICENSE-MIT")
