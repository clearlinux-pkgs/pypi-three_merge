#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-three_merge
Version  : 0.1.1
Release  : 22
URL      : https://files.pythonhosted.org/packages/4d/d1/86f4a088f2ebdc3ff1a9cb653aab91e588a8d0930b41c2e066e6a2920ae7/three-merge-0.1.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/4d/d1/86f4a088f2ebdc3ff1a9cb653aab91e588a8d0930b41c2e066e6a2920ae7/three-merge-0.1.1.tar.gz
Summary  : Simple library for merging two strings with respect to a base one
Group    : Development/Tools
License  : MIT
Requires: pypi-three_merge-license = %{version}-%{release}
Requires: pypi-three_merge-python = %{version}-%{release}
Requires: pypi-three_merge-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(diff_match_patch)

%description
# three-merge
[![Project License - MIT](https://img.shields.io/pypi/l/three-merge.svg)](https://raw.githubusercontent.com/spyder-ide/three-merge/master/LICENSE)
[![pypi version](https://img.shields.io/pypi/v/three-merge.svg)](https://pypi.org/project/three-merge/)
[![conda version](https://img.shields.io/conda/vn/conda-forge/three-merge.svg)](https://www.anaconda.com/download/)
[![download count](https://img.shields.io/conda/dn/conda-forge/three-merge.svg)](https://www.anaconda.com/download/)
[![Downloads](https://pepy.tech/badge/three-merge)](https://pepy.tech/project/three-merge)
[![PyPI status](https://img.shields.io/pypi/status/three-merge.svg)](https://github.com/spyder-ide/three-merge)
![Linux tests](https://github.com/spyder-ide/three-merge/workflows/Linux%20tests/badge.svg)
![MacOS tests](https://github.com/spyder-ide/three-merge/workflows/MacOS%20tests/badge.svg)
![Windows tests](https://github.com/spyder-ide/three-merge/workflows/Windows%20tests/badge.svg)

%package license
Summary: license components for the pypi-three_merge package.
Group: Default

%description license
license components for the pypi-three_merge package.


%package python
Summary: python components for the pypi-three_merge package.
Group: Default
Requires: pypi-three_merge-python3 = %{version}-%{release}

%description python
python components for the pypi-three_merge package.


%package python3
Summary: python3 components for the pypi-three_merge package.
Group: Default
Requires: python3-core
Provides: pypi(three_merge)
Requires: pypi(diff_match_patch)

%description python3
python3 components for the pypi-three_merge package.


%prep
%setup -q -n three-merge-0.1.1
cd %{_builddir}/three-merge-0.1.1
pushd ..
cp -a three-merge-0.1.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656368627
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-three_merge
cp %{_builddir}/three-merge-0.1.1/LICENSE %{buildroot}/usr/share/package-licenses/pypi-three_merge/3b8430679131d39161725b9b41dd652aeb125d39
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-three_merge/3b8430679131d39161725b9b41dd652aeb125d39

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
