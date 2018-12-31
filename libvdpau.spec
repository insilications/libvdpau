#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libvdpau
Version  : 1.1.1
Release  : 4
URL      : https://gitlab.freedesktop.org/vdpau/libvdpau/uploads/5635163f040f2eea59b66d0181cf664b/libvdpau-1.1.1.tar.bz2
Source0  : https://gitlab.freedesktop.org/vdpau/libvdpau/uploads/5635163f040f2eea59b66d0181cf664b/libvdpau-1.1.1.tar.bz2
Summary  : The Video Decode and Presentation API for UNIX
Group    : Development/Tools
License  : MIT
Requires: libvdpau-lib = %{version}-%{release}
Requires: libvdpau-license = %{version}-%{release}
BuildRequires : doxygen
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : graphviz
BuildRequires : pkg-config
BuildRequires : pkgconfig(32dri2proto)
BuildRequires : pkgconfig(32x11)
BuildRequires : pkgconfig(32xext)
BuildRequires : pkgconfig(dri2proto)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xext)
Patch1: 0001-Set-default-configuration-in-absence-of-config-file.patch
Patch2: 0001-mesa_dri2-Add-missing-include-of-config.h-to-define-.patch
Patch3: 0002-util.h-Make-getenv_wrapper-static-inline.patch
Patch4: 0003-Fix-doc-error-on-displayable-surface-types.patch
Patch5: 0004-Add-new-frame-and-field-mode-chroma-types.-Add-VdpDe.patch
Patch6: 0005-Fix-typos-from-commit-53eeb07f68d483fee86ad872884aee.patch

%description


%package dev
Summary: dev components for the libvdpau package.
Group: Development
Requires: libvdpau-lib = %{version}-%{release}
Provides: libvdpau-devel = %{version}-%{release}

%description dev
dev components for the libvdpau package.


%package dev32
Summary: dev32 components for the libvdpau package.
Group: Default
Requires: libvdpau-lib32 = %{version}-%{release}
Requires: libvdpau-dev = %{version}-%{release}

%description dev32
dev32 components for the libvdpau package.


%package doc
Summary: doc components for the libvdpau package.
Group: Documentation

%description doc
doc components for the libvdpau package.


%package lib
Summary: lib components for the libvdpau package.
Group: Libraries
Requires: libvdpau-license = %{version}-%{release}

%description lib
lib components for the libvdpau package.


%package lib32
Summary: lib32 components for the libvdpau package.
Group: Default
Requires: libvdpau-license = %{version}-%{release}

%description lib32
lib32 components for the libvdpau package.


%package license
Summary: license components for the libvdpau package.
Group: Default

%description license
license components for the libvdpau package.


%prep
%setup -q -n libvdpau-1.1.1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
pushd ..
cp -a libvdpau-1.1.1 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1546252167
%configure --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="$ASFLAGS --32"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check
cd ../build32;
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1546252167
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libvdpau
cp COPYING %{buildroot}/usr/share/package-licenses/libvdpau/COPYING
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/vdpau/vdpau.h
/usr/include/vdpau/vdpau_x11.h
/usr/lib64/libvdpau.so
/usr/lib64/pkgconfig/vdpau.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libvdpau.so
/usr/lib32/pkgconfig/32vdpau.pc
/usr/lib32/pkgconfig/vdpau.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/libvdpau/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libvdpau.so.1
/usr/lib64/libvdpau.so.1.0.0
/usr/lib64/vdpau/libvdpau_trace.so
/usr/lib64/vdpau/libvdpau_trace.so.1
/usr/lib64/vdpau/libvdpau_trace.so.1.0.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libvdpau.so.1
/usr/lib32/libvdpau.so.1.0.0
/usr/lib32/vdpau/libvdpau_trace.so
/usr/lib32/vdpau/libvdpau_trace.so.1
/usr/lib32/vdpau/libvdpau_trace.so.1.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libvdpau/COPYING
