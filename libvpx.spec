#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libvpx
Version  : 1.7.0
Release  : 8
URL      : https://github.com/webmproject/libvpx/archive/v1.7.0.tar.gz
Source0  : https://github.com/webmproject/libvpx/archive/v1.7.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause HPND
Requires: libvpx-bin
Requires: libvpx-lib
BuildRequires : nasm
BuildRequires : yasm
Patch1: build.patch

%description
Welcome to the WebM VP8/VP9 Codec SDK!
COMPILING THE APPLICATIONS/LIBRARIES:
The build system used is similar to autotools. Building generally consists of
"configuring" with your desired build options, then using GNU make to build
the application.

%package bin
Summary: bin components for the libvpx package.
Group: Binaries

%description bin
bin components for the libvpx package.


%package dev
Summary: dev components for the libvpx package.
Group: Development
Requires: libvpx-lib
Requires: libvpx-bin
Provides: libvpx-devel

%description dev
dev components for the libvpx package.


%package lib
Summary: lib components for the libvpx package.
Group: Libraries

%description lib
lib components for the libvpx package.


%prep
%setup -q -n libvpx-1.7.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1517070904
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%configure --disable-static || : ; ./configure --prefix=/usr --libdir=/usr/lib64 --target=x86_64-linux-gnu --enable-static --enable-libs --enable-vp8 --enable-vp9 --enable-runtime-cpu-detect --enable-shared --enable-webm-io
make  %{?_smp_mflags} V=1 AS_FLAGS="-a AMD64"

%install
export SOURCE_DATE_EPOCH=1517070904
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/vpxdec
/usr/bin/vpxenc

%files dev
%defattr(-,root,root,-)
/usr/include/vpx/vp8.h
/usr/include/vpx/vp8cx.h
/usr/include/vpx/vp8dx.h
/usr/include/vpx/vpx_codec.h
/usr/include/vpx/vpx_decoder.h
/usr/include/vpx/vpx_encoder.h
/usr/include/vpx/vpx_frame_buffer.h
/usr/include/vpx/vpx_image.h
/usr/include/vpx/vpx_integer.h
/usr/lib64/libvpx.so
/usr/lib64/pkgconfig/vpx.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libvpx.so.5
/usr/lib64/libvpx.so.5.0
/usr/lib64/libvpx.so.5.0.0
