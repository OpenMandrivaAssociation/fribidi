%define major 0
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	Library to support Bi-directional scripts
Name:		fribidi
Version:	0.19.5
Release:	5
License:	LGPLv2+
Group:		System/Internationalization
Url:		http://fribidi.org
Source0:	http://fribidi.org/download/fribidi-%{version}.tar.bz2
Patch0:		fribidi-0.19.1-fix-str-fmt.patch

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
%setup -q
%patch0 -p0

%build
%configure2_5x \
	--disable-static

%make

%check
make check

%install
%makeinstall_std

%files
%doc README AUTHORS ChangeLog TODO THANKS NEWS
%{_bindir}/fribidi

%files -n %{libname}
%{_libdir}/libfribidi.so.%{major}*

%files -n %{devname}
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*
%_mandir/man3/*

