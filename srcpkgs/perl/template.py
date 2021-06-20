pkgname = "perl"
version = "5.32.1"
revision = 2
_perl_cross_version = "1.3.5"
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = ["gmake", "less"]
makedepends = ["zlib-devel", "bzip2-devel"]
depends = ["less"]
checkdepends = ["iana-etc", "perl-AnyEvent", "perl-Test-Pod", "procps-ng"]
short_desc = "Practical Extraction and Report Language"
maintainer = "Leah Neukirchen <leah@vuxu.org>"
license = "Artistic-1.0-Perl, GPL-1.0-or-later"
homepage = "https://www.perl.org"
distfiles = [
    f"https://www.cpan.org/src/5.0/perl-{version}.tar.gz",
    f"https://github.com/arsv/perl-cross/releases/download/{_perl_cross_version}/perl-cross-{_perl_cross_version}.tar.gz"
]
checksum = [
    "03b693901cd8ae807231b1787798cf1f2e0b8a56218d07b7da44f784a7caeb2c",
    "91c66f6b2b99fccfd4fee14660b677380b0c98f9456359e91449798c2ad2ef25"
]

# Before updating this package to a new major version, run ${FILESDIR}/provides.pl
# against ${wrksrc} to find the list of built in packages.

provides = [
    "perl-Archive-Tar-2.36_1",
    "perl-Attribute-Handlers-1.01_1",
    "perl-AutoLoader-5.74_1",
    "perl-CPAN-2.27_1",
    "perl-CPAN-Meta-2.150010_1",
    "perl-CPAN-Meta-Requirements-2.140_1",
    "perl-CPAN-Meta-YAML-0.018_1",
    "perl-Carp-1.50_1",
    "perl-Compress-Raw-Bzip2-2.093_1",
    "perl-Compress-Raw-Zlib-2.093_1",
    "perl-Config-Perl-V-0.32_1",
    "perl-Data-Dumper-2.174.01_1",
    "perl-Devel-PPPort-3.57_1",
    "perl-Devel-SelfStubber-1.06_1",
    "perl-Digest-1.17.01_1",
    "perl-Digest-MD5-2.55.01_1",
    "perl-Digest-SHA-6.02_1",
    "perl-Dumpvalue-1.21_1",
    "perl-Encode-3.06_1",
    "perl-Env-1.04_1",
    "perl-Exporter-5.74_1",
    "perl-ExtUtils-CBuilder-0.280234_1",
    "perl-ExtUtils-Constant-0.25_1",
    "perl-ExtUtils-Install-2.14_1",
    "perl-ExtUtils-MakeMaker-7.44_1",
    "perl-ExtUtils-Manifest-1.72_1",
    "perl-ExtUtils-ParseXS-3.40_1",
    "perl-File-Fetch-0.56_1",
    "perl-File-Path-2.16_1",
    "perl-File-Temp-0.2309_1",
    "perl-Filter-Simple-0.96_1",
    "perl-Filter-Util-Call-1.59_1",
    "perl-FindBin-1.51_1",
    "perl-Getopt-Long-2.51_1",
    "perl-HTTP-Tiny-0.076_1",
    "perl-I18N-Collate-1.02_1",
    "perl-I18N-LangTags-0.44_1",
    "perl-IO-1.43_1",
    "perl-IO-Compress-2.093_1",
    "perl-IO-Socket-IP-0.39_1",
    "perl-IO-Zlib-1.10_1",
    "perl-IPC-Cmd-1.04_1",
    "perl-IPC-SysV-2.07_1",
    "perl-JSON-PP-4.04_1",
    "perl-Locale-Maketext-1.29_1",
    "perl-Locale-Maketext-Simple-0.21.01_1",
    "perl-MIME-Base64-3.15_1",
    "perl-Math-BigInt-1.999818_1",
    "perl-Math-BigInt-FastCalc-0.5009_1",
    "perl-Math-BigRat-0.2614_1",
    "perl-Math-Complex-1.59.01_1",
    "perl-Memoize-1.03.01_1",
    "perl-Module-CoreList-5.20210123_1",
    "perl-Module-Load-0.34_1",
    "perl-Module-Load-Conditional-0.70_1",
    "perl-Module-Loaded-0.08_1",
    "perl-Module-Metadata-1.000037_1",
    "perl-NEXT-0.67.01_1",
    "perl-Net-Ping-2.72_1",
    "perl-Params-Check-0.38_1",
    "perl-PathTools-3.78_1",
    "perl-Perl-OSType-1.010_1",
    "perl-PerlIO-via-QuotedPrint-0.08_1",
    "perl-Pod-Checker-1.73_1",
    "perl-Pod-Escapes-1.07_1",
    "perl-Pod-Perldoc-3.2801_1",
    "perl-Pod-Simple-3.40_1",
    "perl-Pod-Usage-1.69_1",
    "perl-Safe-2.41.01_1",
    "perl-Scalar-List-Utils-1.55_1",
    "perl-Search-Dict-1.07_1",
    "perl-SelfLoader-1.26_1",
    "perl-Socket-2.029_1",
    "perl-Storable-3.21_1",
    "perl-Sys-Syslog-0.36_1",
    "perl-Term-ANSIColor-5.01_1",
    "perl-Term-Cap-1.17_1",
    "perl-Term-Complete-1.403_1",
    "perl-Term-ReadLine-1.17_1",
    "perl-Test-1.31_1",
    "perl-Test-Harness-3.42_1",
    "perl-Test-Simple-1.302175_1",
    "perl-Text-Abbrev-1.02_1",
    "perl-Text-Balanced-2.03_1",
    "perl-Text-ParseWords-3.30_1",
    "perl-Text-Tabs-2013.0523_1",
    "perl-Thread-Queue-3.14_1",
    "perl-Thread-Semaphore-2.13_1",
    "perl-Tie-File-1.06_1",
    "perl-Tie-RefHash-1.39_1",
    "perl-Time-HiRes-1.9764_1",
    "perl-Time-Local-1.28_1",
    "perl-Time-Piece-1.3401_1",
    "perl-Unicode-Collate-1.27_1",
    "perl-Unicode-Normalize-1.27_1",
    "perl-Win32-0.53_1",
    "perl-Win32API-File-0.1203.01_1",
    "perl-XSLoader-0.30_1",
    "perl-autodie-2.32_1",
    "perl-autouse-1.11_1",
    "perl-base-2.27_1",
    "perl-bignum-0.51_1",
    "perl-constant-1.33_1",
    "perl-encoding-warnings-0.13_1",
    "perl-experimental-0.020_1",
    "perl-if-0.0608_1",
    "perl-lib-0.65_1",
    "perl-libnet-3.11_1",
    "perl-parent-0.238_1",
    "perl-perlfaq-5.20200523_1",
    "perl-podlators-5.008_1",
    "perl-threads-2.25_1",
    "perl-threads-shared-1.61_1",
    "perl-version-0.9924_1",
]

def post_extract(self):
    import shutil

    pcpath = self.abs_wrksrc / ".." / f"perl-cross-{_perl_cross_version}"

    for f in pcpath.iterdir():
        if f.name == "utils":
            shutil.move(f / "Makefile", self.abs_wrksrc / "utils")
            f.rmdir()
            continue
        shutil.move(f, self.abs_wrksrc)

    pcpath.rmdir()

def init_configure(self):
    import shutil

    from cbuild.util import make

    self.make = make.Make(self)

    self.LDFLAGS.append("-Wl,-z,stack-size=2097152")
    self.LDFLAGS.append("-pthread")

    self.env["HOSTCFLAGS"] = "-D_GNU_SOURCE"

    self.CFLAGS.append("-DNO_POSIX_2008_LOCALE")
    self.CFLAGS.append("-D_GNU_SOURCE")

    self.tools["LD"] = self.tools["CC"]

    # to prevent perl buildsystem from invoking bmake
    if not self.bootstrapping or shutil.which("gmake"):
        self.env["MAKE"] = "gmake"

def do_configure(self):
    cargs = [
        "--prefix=/usr",
        "-Dusethreads", "-Duseshrplib", "-Dusesoname", "-Dusevendorprefix",
        "-Dprefix=/usr", "-Dvendorprefix=/usr",
        "-Dprivlib=/usr/share/perl5/core_perl",
        "-Darchlib=/usr/lib/perl5/core_perl",
        "-Dsitelib=/usr/share/perl5/site_perl",
        "-Dsitearch=/usr/lib/perl5/site_perl",
        "-Dvendorlib=/usr/share/perl5/vendor_perl",
        "-Dvendorarch=/usr/lib/perl5/vendor_perl",
        "-Dscriptdir=/usr/bin", "-Dvendorscript=/usr/bin",
        "-Dinc_version_list=none", "-Dman1ext=1p", "-Dman3ext=3p",
        "-Dman1dir=/usr/share/man/man1",
        "-Dman3dir=/usr/share/man/man3",
        "-Dd_sockaddr_in6=define",
    ]

    if self.cross_build:
        cargs.append("--target=" + self.cross_triplet)

    cargs.append("-Dcccdlflags=-fPIC")
    cargs.append("-Doptimize=-Wall " + " ".join(self.CFLAGS))
    cargs.append("-Dccflags=" + " ".join(self.CFLAGS))
    cargs.append("-Dlddlflags=-shared " + " ".join(self.LDFLAGS))
    cargs.append("-Dldflags=" + " ".join(self.LDFLAGS))
    cargs.append("-Dperl_static_inline=static __inline__")
    cargs.append("-Dd_static_inline")

    self.do(self.chroot_wrksrc / "configure", cargs, build = True)

def do_check(self):
    from cbuild.util import make

    self.env["TEST_JOBS"] = str(make.jobs())

    self.make.invoke("test")

def post_install(self):
    for f in (self.destdir / "usr/share").rglob("*"):
        if f.is_file() and not f.is_symlink():
            f.chmod(0o644)

    for f in (self.destdir / "usr/lib").rglob("*"):
        if f.is_file() and not f.is_symlink():
            f.chmod(0o644)

    self.install_link("perl", "usr/bin/perl" + version)

    # remove all pod files except those under
    # /usr/share/perl5/core_perl/pod/ (FS#16488)
    for f in (self.destdir / "usr/share/perl5/core_perl").glob("*.pod"):
        f.unlink()

    for d in (self.destdir / "usr/share/perl5/core_perl").iterdir():
        if not d.is_dir() or d.name == "pod":
            continue
        for f in d.rglob("*.pod"):
            f.unlink()

    for f in (self.destdir / "usr/lib").rglob("*.pod"):
        f.unlink()

    for f in self.destdir.rglob(".packlist"):
        f.unlink()

    import re
    import os

    cfpath = self.destdir / "usr/lib/perl5/core_perl/Config_heavy.pl"
    with open(cfpath) as ifile:
        with open(self.abs_wrksrc / "Config_heavy.pl.new", "w") as ofile:
            for ln in ifile:
                ln = re.sub("-specs=.*hardened-ld", "", ln)
                ln = re.sub("-specs=.*hardened-cc1", "", ln)
                ofile.write(ln)

    cfpath.unlink()
    os.rename(self.abs_wrksrc / "Config_heavy.pl.new", cfpath)
    cfpath.chmod(0o644)
