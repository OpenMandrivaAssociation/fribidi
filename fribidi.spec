%define version 0.10.4
%define release %mkrel 6

%define major 0
%define glib_version 1.3.13

%define libname %mklibname %{name} %{major}

Summary:	Library to support Bi-directional scripts
Name:		fribidi
Version:	%{version}
Release:	%{release}
License:	LGPL
Group:		System/Internationalization
Source:		http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
URL:		http://fribidi.sourceforge.net/
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
Summary:	Static libraries and headers for %{name} library
Group:		Development/C
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}

%description	-n %{libname}-devel
This package includes the static libraries and header files for the
%{name} package.

Install this package if you want to develop or compile programs which
will use %{name}.

%prep
%setup -q

# fix detection of glib2
# 0.10.4-3mdk (Abel) no more necessary
#rm -f acinclude.m4
#touch acinclude.m4
#aclocal
#autoconf

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
%doc README AUTHORS  ChangeLog TODO THANKS NEWS
%{_bindir}/fribidi

%files -n %{libname}
%defattr(-, root, root)
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-, root, root)
%{_bindir}/fribidi-config
%multiarch %{multiarch_bindir}/fribidi-config
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*


