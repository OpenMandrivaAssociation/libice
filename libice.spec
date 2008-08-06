%define libice %mklibname ice 6
Name: libice
Summary:  X Inter Client Exchange Library
Version: 1.0.4
Release: %mkrel 5
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

%package -n %{libice}
Summary:  X Inter Client Exchange Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libice}
libice provides an interface to ICE, the Inter-Client Exchange protocol.
Motivated by issues arising from the need for X Window System clients to
share data with each other, the ICE protocol provides a generic framework for
building protocols on top of reliable, byte-stream transport connections. It
provides basic mechanisms for setting up and shutting down connections, for
performing authentication, for negotiating versions, and for reporting
errors.

#-----------------------------------------------------------

%package -n %{libice}-devel
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libice} = %{version}
Requires: x11-proto-devel >= 1.0.0
Provides: libice-devel = %{version}-%{release}
Conflicts: libxorg-x11-devel < 7.0

%description -n %{libice}-devel
Development files for %{name}

%pre -n %{libice}-devel
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files -n %{libice}-devel
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

%package -n %{libice}-static-devel
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{libice}-devel = %{version}
Provides: libice-static-devel = %{version}-%{release}
Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{libice}-static-devel
Static development files for %{name}

%files -n %{libice}-static-devel
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

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -p /sbin/ldconfig
%endif

%files -n %{libice}
%defattr(-,root,root)
%{_libdir}/libICE.so.6
%{_libdir}/libICE.so.6.3.0
