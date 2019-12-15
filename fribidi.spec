%define major 0
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	Library to support Bi-directional scripts
Name:		fribidi
Version:	1.0.8
Release:	1
License:	LGPLv2+
Group:		System/Internationalization
Url:		http://fribidi.org
Source0:	https://github.com/fribidi/fribidi/releases/download/v1.0.8/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	meson

%description
A library to handle bidirectional scripts (eg hebrew, arabic), so that
the display is done in the proper way; while the text data itself is
always written in logical order.
The library uses unicode internally.

%package -n %{libname}
Summary:	Library to support Bi-directional scripts
Group:		System/Internationalization

%description -n %{libname}
A library to handle bidirectional scripts (eg hebrew, arabic), so that
the display is done in the proper way; while the text data itself is
always written in logical order.
The library uses unicode internally.

%package -n %{devname}
Summary:	Libraries and headers for development with %{name}
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%{_lib}fribidi-static-devel < 0.19.2-6

%description -n %{devname}
This package includes the libraries and header files for the %{name}
package.

%prep
%autosetup -p1

%build
%meson

%meson_build

%install
%meson_install

%files
%doc README AUTHORS ChangeLog TODO THANKS NEWS
%{_bindir}/fribidi

%files -n %{libname}
%{_libdir}/libfribidi.so.%{major}*

%files -n %{devname}
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_mandir}/man3/*
