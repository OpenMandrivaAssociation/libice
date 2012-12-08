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

%changelog
* Tue Mar 06 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1.0.8-1
+ Revision: 782302
- 1.0.8

* Tue Dec 27 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.0.7-4
+ Revision: 745625
- one last clean up
- rebuild
- disabled static build
- removed .la files
- cleaned up spec
- employed major macro

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.7-3
+ Revision: 662377
- mass rebuild

* Fri Feb 18 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.0.7-2
+ Revision: 638484
- dropped major from devel and static pkgs
- added proper provides and obsoletes

* Wed Oct 20 2010 Thierry Vignaud <tv@mandriva.org> 1.0.7-1mdv2011.0
+ Revision: 586888
- adjust file list
- new release

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.6-2mdv2010.1
+ Revision: 520867
- rebuilt for 2010.1

* Mon Aug 31 2009 Thierry Vignaud <tv@mandriva.org> 1.0.6-1mdv2010.0
+ Revision: 422874
- new release

* Sat Jan 10 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.5-1mdv2009.1
+ Revision: 328129
- update to new version 1.0.5

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 1.0.4-5mdv2009.0
+ Revision: 264806
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Jun 02 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.4-4mdv2009.0
+ Revision: 214369
- Rebuild to match changes in xtrans.
- Revert build requires.

* Mon Jan 14 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.4-3mdv2008.1
+ Revision: 151454
- Update BuildRequires and rebuild.

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Aug 21 2007 Thierry Vignaud <tv@mandriva.org> 1.0.4-1mdv2008.0
+ Revision: 68269
- new release


* Fri Feb 16 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.0.3-1mdv2007.0
+ Revision: 121707
- new release

  + Gustavo Pichorim Boiko <boiko@mandriva.com>
    - rebuild to fix cooker uploading
    - X11R7.1
    - increment release
    - fixed more dependencies
    - Adding X.org 7.0 to the repository

  + Andreas Hasenack <andreas@mandriva.com>
    - renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

