%define url_ver %(echo %{version}|cut -d. -f1,2)

%define api	2.36
%define major	1
%define libname	%mklibname %{name} %{api} %{major}
%define devname	%mklibname -d %{name} %{api}
%define _disable_rebuild_configure 1

Summary:	C++ interface for accessibility library Atk
Name:		atkmm
Version:	2.36.3
Release:	4
#gw lib is LGPL, tool is GPL
License:	LGPLv2+ and GPLv2+
Group:		System/Libraries
Url:		https://gtkmm.sourceforge.net/
Source0:	https://ftp.gnome.org/pub/GNOME/sources/atkmm/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	meson
BuildRequires:	mm-common
BuildRequires:	pkgconfig(atk)
BuildRequires:	pkgconfig(glibmm-2.68)

%description
Atkmm provides a C++ interface to the Atk accessibility library.
Highlights include typesafe callbacks, widgets extensible via inheritance
and a comprehensive set of widget classes that can be freely combined to
quickly create complex user interfaces.


%package	-n %{libname}
Summary:	C++ interface for accessibility library Atk
Group:		System/Libraries
Provides:	%{name}%{api} = %{EVRD}

%description	-n %{libname}
Atkmm provides a C++ interface to the Atk accessibility library.
Highlights include typesafe callbacks, widgets extensible via inheritance
and a comprehensive set of widget classes that can be freely combined to
quickly create complex user interfaces.

This package contains the library needed to run programs dynamically
linked with %{name}.

%package	-n %{devname}
Summary:	Headers and development files of %{name}
Group:		Development/GNOME and GTK+
Requires:	%{libname} = %{EVRD}
Provides:	%{name}%{api}-devel = %{EVRD}
Obsoletes:	%{name}-docs

%description	-n %{devname}
This package contains the headers and development files that are needed,
when trying to develop or compile applications which need %{name}.

%prep
%setup -q

%build
%meson  \
          -Dbuild-deprecated-api=true
%meson_build

%install
%meson_install

%files -n %{libname}
%{_libdir}/libatkmm-%{api}.so.%{major}*

%files -n %{devname}
%doc ChangeLog COPYING NEWS README*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/atkmm-%{api}/
#doc #{_datadir}/doc/atkmm-%{api}/
#doc #{_datadir}/devhelp/books/*

