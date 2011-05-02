%define libname %mklibname ice 6
%define develname %mklibname ice -d
%define staticname %mklibname ice -d -s

Name: libice
Summary:  X Inter Client Exchange Library
Version: 1.0.7
Release: %mkrel 3
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libICE-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: x11-xtrans-devel >= 1.0.0

%description
libice provides an interface to ICE, the Inter-Client Exchange protocol.
Motivated by issues arising from the need for X Window System clients to
share data with each other, the ICE protocol provides a generic framework for
building protocols on top of reliable, byte-stream transport connections. It
provides basic mechanisms for setting up and shutting down connections, for
performing authentication, for negotiating versions, and for reporting
errors.

#-----------------------------------------------------------

%package -n %{libname}
Summary:  X Inter Client Exchange Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libname}
libice provides an interface to ICE, the Inter-Client Exchange protocol.
Motivated by issues arising from the need for X Window System clients to
share data with each other, the ICE protocol provides a generic framework for
building protocols on top of reliable, byte-stream transport connections. It
provides basic mechanisms for setting up and shutting down connections, for
performing authentication, for negotiating versions, and for reporting
errors.

#-----------------------------------------------------------

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libname} = %{version}-%{release}
Requires: x11-proto-devel >= 1.0.0
Provides: libice-devel = %{version}-%{release}
Provides: libice6-devel = %{version}-%{release}
Obsoletes: %{mklibname ice 6}-devel
Conflicts: libxorg-x11-devel < 7.0

%description -n %{develname}
Development files for %{name}

%pre -n %{develname}
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/libICE.so
%{_libdir}/libICE.la
%{_libdir}/pkgconfig/ice.pc
%{_includedir}/X11/ICE/ICEutil.h
%{_includedir}/X11/ICE/ICE.h
%{_includedir}/X11/ICE/ICEproto.h
%{_includedir}/X11/ICE/ICEconn.h
%{_includedir}/X11/ICE/ICElib.h
%{_includedir}/X11/ICE/ICEmsg.h

#-----------------------------------------------------------

%package -n %{staticname}
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{develname} = %{version}-%{release}
Provides: libice-static-devel = %{version}-%{release}
Provides: libice6-static-devel = %{version}-%{release}
Obsoletes: %{mklibname ice 6}-static-devel
Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{staticname}
Static development files for %{name}

%files -n %{staticname}
%defattr(-,root,root)
%{_libdir}/libICE.a

#-----------------------------------------------------------

%prep
%setup -q -n libICE-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std
mv %{buildroot}/%_datadir/doc/lib{ICE,ice}

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libICE.so.6
%{_libdir}/libICE.so.6.3.0
%{_datadir}/doc/libice
