%define version 0.10.7
%define release %mkrel 1

%define major 0
%define glib_version 1.3.13

%define libname %mklibname %{name} %{major}

Summary:	Library to support Bi-directional scripts
Name:		fribidi
Version:	%{version}
Release:	%{release}
License:	LGPL
Group:		System/Internationalization
Source: 	http://fribidi.org/download/fribidi-%{version}.tar.gz
URL:		http://fribidi.org
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
A library to handle bidirectional scripts (eg hebrew, arabic), so that
the display is done in the proper way; while the text data itself is
always written in logical order.
The library uses unicode internally.

%package	-n %{libname}
Summary:	Library to support Bi-directional scripts
Group:		System/Internationalization
Requires:	%{name} = %{version}

%description	-n %{libname}
A library to handle bidirectional scripts (eg hebrew, arabic), so that
the display is done in the proper way; while the text data itself is
always written in logical order.
The library uses unicode internally.

%package	-n %{libname}-devel
Summary:	Libraries and headers for development with %{name}
Group:		Development/C
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}

%description	-n %{libname}-devel
This package includes the libraries and header files for the %{name}
package.

Install this package if you want to develop or compile programs which
will use %{name}.

%package	-n %{libname}-static-devel
Summary:	Static development files for %{name}
Group:		Development/C
Provides:	lib%{name}-static-devel = %{version}-%{release}
Requires:	%{libname}-devel = %{version}-%{release}

%description	-n %{libname}-static-devel
Static development files for %{name}.

%prep
%setup -q

%build
%configure2_5x
%make

make check

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%multiarch_binaries $RPM_BUILD_ROOT%{_bindir}/fribidi-config

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc README AUTHORS ChangeLog TODO THANKS NEWS
%{_bindir}/fribidi

%files -n %{libname}
%defattr(-, root, root)
%{_libdir}/*.so.%{major}*

%files -n %{libname}-devel
%defattr(-, root, root)
%{_bindir}/fribidi-config
%multiarch %{multiarch_bindir}/fribidi-config
%{_libdir}/*.la
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*

%files -n %{libname}-static-devel
%defattr(-, root, root)
%{_libdir}/*.a

