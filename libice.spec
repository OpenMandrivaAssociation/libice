%define major 6
%define libname %mklibname ice %{major}
%define devname %mklibname ice -d
# libICE is used by wine and steam -- need a 32-bit
# compat package
%ifarch %{x86_64}
%bcond_without compat32
%else
%bcond_with compat32
%endif
%if %{with compat32}
%define lib32name libice%{major}
%define dev32name libice-devel
%endif

Name:		libice
Summary:	X Inter Client Exchange Library
Version:	1.1.0
Release:	1
Group:		Development/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libICE-%{version}.tar.xz
BuildRequires:	pkgconfig(xproto)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xtrans)
BuildRequires:	pkgconfig(libbsd)
%if %{with compat32}
BuildRequires:	devel(libbsd)
%endif

%description
libice provides an interface to ICE, the Inter-Client Exchange protocol.
Motivated by issues arising from the need for X Window System clients to
share data with each other, the ICE protocol provides a generic framework for
building protocols on top of reliable, byte-stream transport connections. It
provides basic mechanisms for setting up and shutting down connections, for
performing authentication, for negotiating versions, and for reporting
errors.

%package -n %{libname}
Summary:	X Inter Client Exchange Library
Group:		Development/X11
Provides:	%{name} = %{version}

%description -n %{libname}
libice provides an interface to ICE, the Inter-Client Exchange protocol.
Motivated by issues arising from the need for X Window System clients to
share data with each other, the ICE protocol provides a generic framework for
building protocols on top of reliable, byte-stream transport connections. It
provides basic mechanisms for setting up and shutting down connections, for
performing authentication, for negotiating versions, and for reporting
errors.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%{_lib}ice6-devel < 1.0.8
Obsoletes:	%{_lib}ice-static-devel < 1.0.8

%description -n %{devname}
Development files for %{name}.

%if %{with compat32}
%package -n %{lib32name}
Summary:	X Inter Client Exchange Library (32-bit)
Group:		Development/X11
Provides:	%{name} = %{version}

%description -n %{lib32name}
libice provides an interface to ICE, the Inter-Client Exchange protocol.
Motivated by issues arising from the need for X Window System clients to
share data with each other, the ICE protocol provides a generic framework for
building protocols on top of reliable, byte-stream transport connections. It
provides basic mechanisms for setting up and shutting down connections, for
performing authentication, for negotiating versions, and for reporting
errors.

%package -n %{dev32name}
Summary:	Development files for %{name} (32-bit)
Group:		Development/X11
Requires:	%{lib32name} = %{EVRD}
Requires:	%{devname} = %{EVRD}

%description -n %{dev32name}
Development files for %{name}.
%endif

%prep
%autosetup -n libICE-%{version} -p1
export CONFIGURE_TOP="`pwd`"

%if %{with compat32}
mkdir build32
cd build32
%configure32
cd ..
%endif
mkdir build
cd build
%configure

%build
%if %{with compat32}
%make_build -C build32
%endif
%make_build -C build

%install
%if %{with compat32}
%make_install -C build32
%endif
%make_install -C build
mv %{buildroot}/%{_datadir}/doc/lib{ICE,ice}

%files -n %{libname}
%{_libdir}/libICE.so.%{major}*

%files -n %{devname}
%{_datadir}/doc/libice
%{_libdir}/libICE.so
%{_libdir}/pkgconfig/ice.pc
%{_includedir}/X11/ICE/ICEutil.h
%{_includedir}/X11/ICE/ICE.h
%{_includedir}/X11/ICE/ICEproto.h
%{_includedir}/X11/ICE/ICEconn.h
%{_includedir}/X11/ICE/ICElib.h
%{_includedir}/X11/ICE/ICEmsg.h

%if %{with compat32}
%files -n %{lib32name}
%{_prefix}/lib/libICE.so.%{major}*

%files -n %{dev32name}
%{_prefix}/lib/libICE.so
%{_prefix}/lib/pkgconfig/*.pc
%endif
