%define major 6
%define libname %mklibname ice %{major}
%define develname %mklibname ice -d

Name:		libice
Summary:	X Inter Client Exchange Library
Version:	1.0.8
Release:	3
Group:		Development/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	ftp://xorg.freedesktop.org/pub/individual/lib/libICE-%{version}.tar.bz2

BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	x11-util-macros >= 1.0.1
BuildRequires:	x11-xtrans-devel >= 1.0.0

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
Conflicts:	libxorg-x11 < 7.0
Provides:	%{name} = %{version}

%description -n %{libname}
libice provides an interface to ICE, the Inter-Client Exchange protocol.
Motivated by issues arising from the need for X Window System clients to
share data with each other, the ICE protocol provides a generic framework for
building protocols on top of reliable, byte-stream transport connections. It
provides basic mechanisms for setting up and shutting down connections, for
performing authentication, for negotiating versions, and for reporting
errors.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}-%{release}
Provides:	libice-devel = %{version}-%{release}
Obsoletes:	%{_lib}ice6-devel < 1.0.8
Obsoletes:	%{_lib}ice-static-devel < 1.0.8
Conflicts:	libxorg-x11-devel < 7.0

%description -n %{develname}
Development files for %{name}

%prep
%setup -q -n libICE-%{version}

%build
%configure2_5x \
	--disable-static \
	--x-includes=%{_includedir}\
	--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std
mv %{buildroot}/%{_datadir}/doc/lib{ICE,ice}

%files -n %{libname}
%{_libdir}/libICE.so.%{major}*

%files -n %{develname}
%{_datadir}/doc/libice
%{_libdir}/libICE.so
%{_libdir}/pkgconfig/ice.pc
%{_includedir}/X11/ICE/ICEutil.h
%{_includedir}/X11/ICE/ICE.h
%{_includedir}/X11/ICE/ICEproto.h
%{_includedir}/X11/ICE/ICEconn.h
%{_includedir}/X11/ICE/ICElib.h
%{_includedir}/X11/ICE/ICEmsg.h

