%define glibmm_version 2.24.0
%define atk_version 1.12

%define api_version 1.6
%define major 1
%define libname %mklibname %{name} %{api_version} %{major}
%define libnamedev %mklibname -d %{name} %{api_version}
%define gtkmmapi 2.4
%define gtkmmlibname %mklibname gtkmm %{gtkmmapi} %{major}
%define gtkmmlibnamedev %mklibname -d gtkmm %{gtkmmapi}


Name:		atkmm
Summary:	C++ interface for accessibility library Atk
Version:	2.22.6
Release:	2
#gw lib is LGPL, tool is GPL
License:	LGPLv2+ and GPLv2+
Group:		System/Libraries
URL:		http://gtkmm.sourceforge.net/
Source:		http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
BuildRequires:	glibmm2.4-devel >= %{glibmm_version}
BuildRequires:	atk-devel >= %{atk_version}
BuildRequires:	mm-common

%description
Atkmm provides a C++ interface to the Atk accessibility library.
Highlights include typesafe callbacks, widgets extensible via inheritance
and a comprehensive set of widget classes that can be freely combined to
quickly create complex user interfaces.


%package	-n %{libname}
Summary:	C++ interface for accessibility library Atk
Group:		System/Libraries
Provides:	%{name}%{api_version} = %{EVRD}
Conflicts:	%{gtkmmlibname} < 2.21

%description	-n %{libname}
Atkmm provides a C++ interface to the Atk accessibility library.
Highlights include typesafe callbacks, widgets extensible via inheritance
and a comprehensive set of widget classes that can be freely combined to
quickly create complex user interfaces.

This package contains the library needed to run programs dynamically
linked with %{name}.


%package	-n %{libnamedev}
Summary:	Headers and development files of %{name}
Group:		Development/GNOME and GTK+
Requires:	%{libname} = %{EVRD}
Provides:	%{name}%{api_version}-devel = %{EVRD}
Requires:	glibmm2.4-devel >= %{glibmm_version}
Conflicts:	%{gtkmmlibnamedev} < 2.21

%description	-n %{libnamedev}
This package contains the headers and development files that are needed,
when trying to develop or compile applications which need %{name}.


%package	doc
Summary:	Atkmm documentation
Group:		Books/Other

%description	doc
Atkmm provides a C++ interface to the Atk accessibility library. 

Highlights include typesafe callbacks, widgets extensible via inheritance
and a comprehensive set of widget classes that can be freely combined to
quickly create complex user interfaces.

This package contains all API documentation for Atkmm. You can readily read
this documentation with devhelp, a documentation reader.

%prep
%setup -q

%build
%configure2_5x \
    --enable-shared \
    --disable-static

%make

# make check does nothing

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libatkmm-%{api_version}.so.%{major}*

%files -n %{libnamedev}
%doc ChangeLog AUTHORS COPYING NEWS README
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/atkmm-%{api_version}/

%files doc
%doc %{_datadir}/doc/atkmm-%{api_version}/
%doc %{_datadir}/devhelp/books/*


%changelog
* Mon Dec 05 2011 Zé <ze@mandriva.org> 2.22.6-2
+ Revision: 738009
- clean defattr, BR, clean section and mkrel
- disable static files
- clean .la files
- move docs to devel
- now is needed to set requires to release

* Wed Oct 26 2011 Götz Waschk <waschk@mandriva.org> 2.22.6-1
+ Revision: 707294
- update to new version 2.22.6

* Wed Mar 30 2011 Götz Waschk <waschk@mandriva.org> 2.22.5-1
+ Revision: 649051
- update to new version 2.22.5

* Fri Mar 25 2011 Götz Waschk <waschk@mandriva.org> 2.22.4-1
+ Revision: 648499
- update to new version 2.22.4

* Wed Mar 23 2011 Götz Waschk <waschk@mandriva.org> 2.22.3-1
+ Revision: 648032
- update build deps
- update to new version 2.22.3

* Sat Jan 08 2011 Götz Waschk <waschk@mandriva.org> 2.22.2-1mdv2011.0
+ Revision: 630597
- update to new version 2.22.2

* Sun Nov 21 2010 Götz Waschk <waschk@mandriva.org> 2.22.1-1mdv2011.0
+ Revision: 599470
- update to new version 2.22.1

* Mon Sep 27 2010 Götz Waschk <waschk@mandriva.org> 2.22.0-1mdv2011.0
+ Revision: 581488
- update to new version 2.22.0

* Mon Jun 28 2010 Götz Waschk <waschk@mandriva.org> 2.21.2-1mdv2011.0
+ Revision: 549300
- initial package

* Tue May 04 2010 Götz Waschk <waschk@mandriva.org> 2.20.3-1mdv2010.1
+ Revision: 541987
- update to new version 2.20.3

* Fri Apr 16 2010 Götz Waschk <waschk@mandriva.org> 2.20.2-1mdv2010.1
+ Revision: 535451
- update to new version 2.20.2

* Wed Apr 07 2010 Götz Waschk <waschk@mandriva.org> 2.20.1-1mdv2010.1
+ Revision: 532791
- update to new version 2.20.1

* Tue Mar 30 2010 Götz Waschk <waschk@mandriva.org> 2.20.0-1mdv2010.1
+ Revision: 529689
- new version
- bump glibmm dep

* Thu Mar 18 2010 Götz Waschk <waschk@mandriva.org> 2.19.7-1mdv2010.1
+ Revision: 524905
- update to new version 2.19.7

* Wed Feb 24 2010 Götz Waschk <waschk@mandriva.org> 2.19.6-1mdv2010.1
+ Revision: 510579
- update to new version 2.19.6

* Tue Jan 26 2010 Götz Waschk <waschk@mandriva.org> 2.19.4-1mdv2010.1
+ Revision: 496741
- new version
- bump gtk dep

* Mon Jan 04 2010 Götz Waschk <waschk@mandriva.org> 2.19.2-1mdv2010.1
+ Revision: 486186
- update to new version 2.19.2

* Sun Oct 04 2009 Götz Waschk <waschk@mandriva.org> 2.18.2-1mdv2010.0
+ Revision: 453733
- new version

* Mon Sep 21 2009 Götz Waschk <waschk@mandriva.org> 2.18.1-1mdv2010.0
+ Revision: 446720
- new version
- update file list

* Mon Sep 07 2009 Götz Waschk <waschk@mandriva.org> 2.17.11-1mdv2010.0
+ Revision: 432734
- new version
- bump gtk dep

* Sat Aug 29 2009 Götz Waschk <waschk@mandriva.org> 2.17.9.3-1mdv2010.0
+ Revision: 422132
- update to new version 2.17.9.3
- update to new version 2.17.9.1

* Wed Aug 26 2009 Götz Waschk <waschk@mandriva.org> 2.17.9-1mdv2010.0
+ Revision: 421449
- new version
- update deps
- update file list

* Tue Jul 14 2009 Götz Waschk <waschk@mandriva.org> 2.17.2-1mdv2010.0
+ Revision: 395970
- update to new version 2.17.2

* Mon Jun 29 2009 Götz Waschk <waschk@mandriva.org> 2.17.1-1mdv2010.0
+ Revision: 390593
- bump gtk+ dep
- new version
- drop merged patch

* Mon Mar 16 2009 Götz Waschk <waschk@mandriva.org> 2.16.0-1mdv2009.1
+ Revision: 355983
- update to new version 2.16.0

* Tue Mar 03 2009 Götz Waschk <waschk@mandriva.org> 2.15.5-1mdv2009.1
+ Revision: 348121
- update to new version 2.15.5

* Fri Feb 06 2009 Götz Waschk <waschk@mandriva.org> 2.15.3-1mdv2009.1
+ Revision: 338044
- update to new version 2.15.3

* Sun Jan 25 2009 Götz Waschk <waschk@mandriva.org> 2.15.1-1mdv2009.1
+ Revision: 333556
- update to new version 2.15.1

* Mon Jan 05 2009 Götz Waschk <waschk@mandriva.org> 2.15.0-1mdv2009.1
+ Revision: 324963
- new version
- bump deps
- fix format strings

* Fri Nov 14 2008 Götz Waschk <waschk@mandriva.org> 2.14.3-1mdv2009.1
+ Revision: 303146
- update to new version 2.14.3

* Mon Nov 10 2008 Götz Waschk <waschk@mandriva.org> 2.14.2-1mdv2009.1
+ Revision: 301809
- update to new version 2.14.2

* Thu Sep 25 2008 Götz Waschk <waschk@mandriva.org> 2.14.1-1mdv2009.0
+ Revision: 288069
- new version

* Mon Sep 22 2008 Götz Waschk <waschk@mandriva.org> 2.14.0-1mdv2009.0
+ Revision: 286602
- new version
- bump pangomm dep

* Wed Sep 10 2008 Götz Waschk <waschk@mandriva.org> 2.13.8-1mdv2009.0
+ Revision: 283475
- new version
- drop patch
- update license

* Tue Sep 09 2008 Götz Waschk <waschk@mandriva.org> 2.13.7-2mdv2009.0
+ Revision: 282904
- patch for gtk api changes (fixes crash reportet as #43623)

* Wed Aug 20 2008 Götz Waschk <waschk@mandriva.org> 2.13.7-1mdv2009.0
+ Revision: 274125
- new version

* Mon Aug 04 2008 Götz Waschk <waschk@mandriva.org> 2.13.6-1mdv2009.0
+ Revision: 263349
- new version

* Wed Jul 23 2008 Götz Waschk <waschk@mandriva.org> 2.13.5-1mdv2009.0
+ Revision: 242538
- new version
- depend on pangomm

* Wed Jul 16 2008 Götz Waschk <waschk@mandriva.org> 2.13.4-1mdv2009.0
+ Revision: 236587
- new version
- update file list

* Thu Jul 03 2008 Götz Waschk <waschk@mandriva.org> 2.13.1-2mdv2009.0
+ Revision: 231287
- new version
- bump deps
- update license

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 2.12.7-2mdv2009.0
+ Revision: 221116
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Apr 02 2008 Götz Waschk <waschk@mandriva.org> 2.12.7-1mdv2008.1
+ Revision: 191629
- new version

* Tue Apr 01 2008 Götz Waschk <waschk@mandriva.org> 2.12.6-1mdv2008.1
+ Revision: 191359
- new version
- new version
- update file list

* Sun Jan 27 2008 Götz Waschk <waschk@mandriva.org> 2.12.4-2mdv2008.1
+ Revision: 158507
- rebuild for broken build system
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Nov 08 2007 Götz Waschk <waschk@mandriva.org> 2.12.3-1mdv2008.1
+ Revision: 106900
- new version

* Mon Nov 05 2007 Götz Waschk <waschk@mandriva.org> 2.12.2-1mdv2008.1
+ Revision: 106016
- new version

* Wed Oct 10 2007 Götz Waschk <waschk@mandriva.org> 2.12.1-1mdv2008.1
+ Revision: 96635
- new version
- bump glibmm dep

* Fri Sep 14 2007 Götz Waschk <waschk@mandriva.org> 2.12.0-1mdv2008.0
+ Revision: 85532
- new version
- bump deps

* Fri Aug 31 2007 Götz Waschk <waschk@mandriva.org> 2.11.8-1mdv2008.0
+ Revision: 76898
- new version

* Fri Aug 17 2007 Götz Waschk <waschk@mandriva.org> 2.11.7-1mdv2008.0
+ Revision: 65168
- new version
- new devel name

* Mon Jul 30 2007 Götz Waschk <waschk@mandriva.org> 2.11.6-1mdv2008.0
+ Revision: 56519
- new version

* Sun Jul 22 2007 Götz Waschk <waschk@mandriva.org> 2.11.5-1mdv2008.0
+ Revision: 54395
- new version
- bump deps

* Mon Jul 02 2007 Götz Waschk <waschk@mandriva.org> 2.11.4-1mdv2008.0
+ Revision: 46963
- new version

* Tue Jun 19 2007 Götz Waschk <waschk@mandriva.org> 2.11.3-2mdv2008.0
+ Revision: 41463
- rebuild

* Mon Jun 18 2007 Götz Waschk <waschk@mandriva.org> 2.11.3-1mdv2008.0
+ Revision: 40798
- new version

* Wed Jun 06 2007 Götz Waschk <waschk@mandriva.org> 2.11.2-1mdv2008.0
+ Revision: 36045
- new version
- bump deps

* Wed May 02 2007 Götz Waschk <waschk@mandriva.org> 2.10.10-1mdv2008.0
+ Revision: 20405
- new version

* Tue Apr 24 2007 Götz Waschk <waschk@mandriva.org> 2.10.9-1mdv2008.0
+ Revision: 17910
- new version

