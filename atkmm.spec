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
Provides:	%{name}%{api_version} = %{version}-%{release}
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
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}%{api_version}-devel = %{version}-%{release}
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
%setup -q -n %{name}-%{version}

%build
%configure2_5x \
    --enable-static \
    --enable-shared \
    --disable-static
%make

# make check does nothing

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -name \*.la|xargs rm -f

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
