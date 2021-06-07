#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : libvdpau
Version  : 1.4
Release  : 301
URL      : file:///aot/build/clearlinux/packages/libvdpau/libvdpau-v1.4.tar.gz
Source0  : file:///aot/build/clearlinux/packages/libvdpau/libvdpau-v1.4.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
BuildRequires : Z3-dev
BuildRequires : Z3-staticdev
BuildRequires : buildreq-meson
BuildRequires : doxygen
BuildRequires : findutils
BuildRequires : gcc
BuildRequires : gcc-abi
BuildRequires : gcc-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-doc
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libs-math
BuildRequires : gcc-libstdc++32
BuildRequires : gcc-libubsan
BuildRequires : gcc-locale
BuildRequires : glibc-dev
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : graphviz
BuildRequires : libX11-data
BuildRequires : libX11-dev
BuildRequires : libX11-lib
BuildRequires : libXScrnSaver
BuildRequires : libXScrnSaver-dev
BuildRequires : libXScrnSaver-lib
BuildRequires : libXau-dev
BuildRequires : libXau-lib
BuildRequires : libXcursor-dev
BuildRequires : libXcursor-lib
BuildRequires : libXdamage-dev
BuildRequires : libXdamage-lib
BuildRequires : libXdmcp-dev
BuildRequires : libXdmcp-lib
BuildRequires : libXext-dev
BuildRequires : libXext-lib
BuildRequires : libXfont2-dev
BuildRequires : libXft-dev
BuildRequires : libXft-lib
BuildRequires : libXi-dev
BuildRequires : libXi-lib
BuildRequires : libXrender-dev
BuildRequires : libXrender-lib
BuildRequires : libXtst-dev
BuildRequires : libXtst-lib
BuildRequires : libXxf86vm-dev
BuildRequires : libXxf86vm-lib
BuildRequires : libgcc1
BuildRequires : libstdc++
BuildRequires : libva
BuildRequires : libva-dev
BuildRequires : libva-intel-driver
BuildRequires : libva-intel-driver-dev
BuildRequires : libva-lib
BuildRequires : libva-vdpau-driver-chromium
BuildRequires : libva-vdpau-driver-chromium-dev
BuildRequires : libvdpau
BuildRequires : libvdpau-dev
BuildRequires : libxcb-dev
BuildRequires : libxcb-lib
BuildRequires : libxkbcommon
BuildRequires : libxkbcommon-dev
BuildRequires : libxml2-dev
BuildRequires : libxml2-staticdev
BuildRequires : libxslt-bin
BuildRequires : libxslt-dev
BuildRequires : libxslt-staticdev
BuildRequires : mesa
BuildRequires : mesa-dev
BuildRequires : mesa-lib
BuildRequires : ninja
BuildRequires : pkg-config
BuildRequires : pkgconfig(32dri2proto)
BuildRequires : pkgconfig(32x11)
BuildRequires : pkgconfig(32xext)
BuildRequires : pkgconfig(dri)
BuildRequires : pkgconfig(dri2proto)
BuildRequires : pkgconfig(dri3proto)
BuildRequires : pkgconfig(libva)
BuildRequires : pkgconfig(libva-drm)
BuildRequires : pkgconfig(libva-glx)
BuildRequires : pkgconfig(libva-wayland)
BuildRequires : pkgconfig(libva-x11)
BuildRequires : pkgconfig(vdpau)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xext)
BuildRequires : sed
BuildRequires : wayland
BuildRequires : wayland-dev
BuildRequires : weston
BuildRequires : wmctrl
BuildRequires : xauth
BuildRequires : xcb-proto
BuildRequires : xcb-proto-dev
BuildRequires : xcb-util-cursor-dev
BuildRequires : xcb-util-dev
BuildRequires : xcb-util-keysyms-dev
BuildRequires : xcb-util-renderutil-dev
BuildRequires : xcb-util-wm-dev
BuildRequires : xcb-util-xrm-dev
BuildRequires : xclip
BuildRequires : xdg-dbus-proxy
BuildRequires : xdg-desktop-portal
BuildRequires : xdg-desktop-portal-dev
BuildRequires : xdg-desktop-portal-gtk
BuildRequires : xdg-desktop-portal-kde
BuildRequires : xdg-user-dirs
BuildRequires : xdg-user-dirs-gtk
BuildRequires : xdg-utils
BuildRequires : xdotool
BuildRequires : xdpyinfo
BuildRequires : xf86-input-libinput
BuildRequires : xf86-video-amdgpu
BuildRequires : xf86-video-ati
BuildRequires : xf86-video-fbdev
BuildRequires : xf86-video-nouveau
BuildRequires : xf86-video-qxl
BuildRequires : xf86-video-vboxvideo
BuildRequires : xf86-video-vesa
BuildRequires : xf86-video-vmware
BuildRequires : xfontsel
BuildRequires : xhost
BuildRequires : xinit
BuildRequires : xinput
BuildRequires : xkbcomp
BuildRequires : xkeyboard-config
BuildRequires : xkill
BuildRequires : xmodmap
BuildRequires : xorg-server
BuildRequires : xorg-server-dev
BuildRequires : xorgproto
BuildRequires : xorgproto-dev
BuildRequires : xprop
BuildRequires : xrandr
BuildRequires : xrdb
BuildRequires : xrdp
BuildRequires : xrestop
BuildRequires : xscreensaver
BuildRequires : xsel
BuildRequires : xset
BuildRequires : xsetroot
BuildRequires : xvfb-run
BuildRequires : xwd
BuildRequires : xwininfo
BuildRequires : xz
BuildRequires : xz-dev
BuildRequires : xz-staticdev
BuildRequires : yaml-cpp
BuildRequires : yaml-cpp-dev
BuildRequires : zlib
BuildRequires : zlib-dev
BuildRequires : zlib-staticdev
BuildRequires : zstd-dev
BuildRequires : zstd-staticdev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Set-default-configuration-in-absence-of-config-file.patch
Patch2: 0001-Enable-static-build.patch

%description
No detailed description available

%prep
%setup -q -n libvdpau
cd %{_builddir}/libvdpau
%patch1 -p1
%patch2 -p1
pushd ..
cp -a libvdpau build32
popd

%build
## build_prepend content
#find . -type f -name '*.json' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#find . -type f -name '*.ninja' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
## build_prepend end
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1623081339
unset LD_AS_NEEDED
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags_pgo content
## pgo generate
export PGO_GEN="-fprofile-generate=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-update=atomic -fprofile-arcs -ftest-coverage --coverage -fprofile-partial-training"
export CFLAGS_GENERATE="-g -O3 -Wl,--as-needed --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now -Wl,-z,relro -Wl,-sort-common -fasynchronous-unwind-tables -pthread -static-libstdc++ -static-libgcc $PGO_GEN"
export FCFLAGS_GENERATE="-g -O3 -Wl,--as-needed --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now -Wl,-z,relro -Wl,-sort-common -fasynchronous-unwind-tables $PGO_GEN"
export FFLAGS_GENERATE="-g -O3 -Wl,--as-needed --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now -Wl,-z,relro -Wl,-sort-common -fasynchronous-unwind-tables $PGO_GEN"
export CXXFLAGS_GENERATE="-g -O3 -Wl,--as-needed --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -fvisibility-inlines-hidden -pipe -ffat-lto-objects -flto=16 -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now -Wl,-z,relro -Wl,-sort-common -fasynchronous-unwind-tables $PGO_GEN"
export LDFLAGS_GENERATE="-g -O3 -Wl,--as-needed --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now -Wl,-z,relro -Wl,-sort-common -fasynchronous-unwind-tables -pthread -static-libstdc++ -static-libgcc -lpthread $PGO_GEN"
## pgo use
## -ffat-lto-objects -fno-PIE -fno-PIE -m64 -no-pie -fPIC -Wl,-z,max-page-size=0x1000 -fvisibility=hidden -flto-partition=none
## gcc: -feliminate-unused-debug-types -fipa-pta -flto=16 -Wno-error -Wp,-D_REENTRANT -fno-common -funroll-loops
export PGO_USE="-fprofile-use=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-correction -fprofile-partial-training"
export CFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export FCFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export FFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export CXXFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export LDFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -lpthread $PGO_USE"
#
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
#
export MAKEFLAGS=%{?_smp_mflags}
#
%global _lto_cflags 1
#global _lto_cflags %{nil}
%global _disable_maintainer_mode 1
#%global _disable_maintainer_mode %{nil}
#
export CCACHE_DISABLE=true
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
#export CCACHE_SLOPPINESS=modules,include_file_mtime,include_file_ctime,time_macros,pch_defines,file_stat_matches,clang_index_store,system_headers,locale
#export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
#export CCACHE_LOGFILE=/var/tmp/ccache/cache.debug
#export CCACHE_DEBUG=true
#export CCACHE_NODIRECT=true
#
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/nvidia/lib64:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/dri:/usr/lib64/haswell:/usr/lib64:/usr/lib:/usr/share"
#
export LIBRARY_PATH="$LIBRARY_PATH:/usr/nvidia/lib64:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/dri:/usr/lib64/haswell:/usr/lib64:/usr/lib:/usr/share"
#
export PATH="$PATH:/usr/local/cuda/bin:/usr/nvidia/bin:/usr/bin/haswell:/usr/bin:/usr/sbin"
#
export CPATH="$CPATH:/usr/local/cuda/include"
#
export DISPLAY=:0
export __GL_ALLOW_UNOFFICIAL_PROTOCOL=1
export __GL_SYNC_TO_VBLANK=0
export __GL_SYNC_DISPLAY_DEVICE=DFP-1
export VDPAU_NVIDIA_SYNC_DISPLAY_DEVICE=DFP-1
export LANG=en_US.UTF-8
export XDG_CONFIG_DIRS=/usr/share/xdg:/etc/xdg
export XDG_SEAT=seat0
export XDG_SESSION_TYPE=tty
export XDG_CURRENT_DESKTOP=KDE
export XDG_SESSION_CLASS=user
export XDG_VTNR=1
export XDG_SESSION_ID=1
export XDG_RUNTIME_DIR=/run/user/1000
export XDG_DATA_DIRS=/usr/local/share:/usr/share
export KDE_SESSION_VERSION=5
export KDE_SESSION_UID=1000
export KDE_FULL_SESSION=true
export KDE_APPLICATIONS_AS_SCOPE=1
export VDPAU_DRIVER=nvidia
export LIBVA_DRIVER_NAME=vdpau
export LIBVA_DRIVERS_PATH=/usr/lib64/dri
export GTK_RC_FILES=/etc/gtk/gtkrc
export FONTCONFIG_PATH=/usr/share/defaults/fonts
## altflags_pgo end
export CFLAGS="${CFLAGS_GENERATE}"
export CXXFLAGS="${CXXFLAGS_GENERATE}"
export FFLAGS="${FFLAGS_GENERATE}"
export FCFLAGS="${FCFLAGS_GENERATE}"
export LDFLAGS="${LDFLAGS_GENERATE}"
meson --libdir=lib64 --prefix=/usr --buildtype=release -Ddefault_library=both  -Ddefault_library=both \
-Ddocumentation=false \
-Ddri2=auto builddir
## make_prepend content
#find . -type f -name '*.json' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#find . -type f -name '*.ninja' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
## make_prepend end
ninja --verbose %{?_smp_mflags} -v -C builddir

export DISPLAY=:0
export __GL_ALLOW_UNOFFICIAL_PROTOCOL=1
export __GL_SYNC_TO_VBLANK=0
export __GL_SYNC_DISPLAY_DEVICE=DFP-1
export VDPAU_NVIDIA_SYNC_DISPLAY_DEVICE=DFP-1
export LANG=en_US.UTF-8
export XDG_CONFIG_DIRS=/usr/share/xdg:/etc/xdg
export XDG_SEAT=seat0
export XDG_SESSION_TYPE=tty
export XDG_CURRENT_DESKTOP=KDE
export XDG_SESSION_CLASS=user
export XDG_VTNR=1
export XDG_SESSION_ID=1
export XDG_RUNTIME_DIR=/run/user/1000
export XDG_DATA_DIRS=/usr/local/share:/usr/share
export KDE_SESSION_VERSION=5
export KDE_SESSION_UID=1000
export KDE_FULL_SESSION=true
export KDE_APPLICATIONS_AS_SCOPE=1
export VDPAU_DRIVER=nvidia
export LIBVA_DRIVER_NAME=vdpau
export LIBVA_DRIVERS_PATH=/usr/lib64/dri
export GTK_RC_FILES=/etc/gtk/gtkrc
export FONTCONFIG_PATH=/usr/share/defaults/fonts
meson test --verbose --num-processes 16 -C builddir || :
exit 1
find builddir/ -type f,l -not -name '*.gcno' -not -name 'statuspgo*' -delete -print  || :
export CFLAGS="${CFLAGS_USE}"
export CXXFLAGS="${CXXFLAGS_USE}"
export FFLAGS="${FFLAGS_USE}"
export FCFLAGS="${FCFLAGS_USE}"
export LDFLAGS="${LDFLAGS_USE}"
meson --libdir=lib64 --prefix=/usr --buildtype=release -Ddefault_library=both -Ddefault_library=both \
-Ddocumentation=false \
-Ddri2=auto  builddir
## make_prepend content
#find . -type f -name '*.json' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#find . -type f -name '*.ninja' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
## make_prepend end
ninja --verbose %{?_smp_mflags} -v -C builddir
pushd ../build32/
export CFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -pipe -fPIC -m32 -mstackrealign -march=native -mtune=native"
export CXXFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -fvisibility-inlines-hidden -pipe -fPIC -m32 -mstackrealign -march=native -mtune=native"
export LDFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -pipe -fPIC -m32 -mstackrealign -march=native -mtune=native"
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
unset LD_LIBRARY_PATH
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
meson --libdir=lib32 --prefix=/usr --buildtype=release -Ddefault_library=both   builddir
ninja --verbose %{?_smp_mflags} -v -C builddir
popd

%check
export LANG=C.UTF-8
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
meson test -C builddir || :
cd ../build32;
meson test -C builddir || : || :

%install
pushd ../build32/
DESTDIR=%{buildroot} ninja -C builddir install
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)
