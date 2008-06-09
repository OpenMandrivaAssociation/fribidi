%define major 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d
%define staticdevelname %mklibname %{name} -d -s

Summary:	Library to support Bi-directional scripts
Name:		fribidi
Version:	0.10.9
Release:	%mkrel 1
License:	LGPLv2+
Group:		System/Internationalization
Source: 	http://fribidi.org/download/fribidi-%{version}.tar.bz2
URL:		http://fribidi.org
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
A library to handle bidirectional scripts (eg hebrew, arabic), so that
the display is done in the proper way; while the text data itself is
always written in logical order.
The library uses unicode internally.

%package -n %{libname}
Summary:	Library to support Bi-directional scripts
Group:		System/Internationalization
Requires:	%{name} = %{version}

%description -n %{libname}
A library to handle bidirectional scripts (eg hebrew, arabic), so that
the display is done in the proper way; while the text data itself is
always written in logical order.
The library uses unicode internally.

%package -n %{develname}
Summary:	Libraries and headers for development with %{name}
Group:		Development/C
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%mklibname %{name} 0 -d

%description -n %{develname}
This package includes the libraries and header files for the %{name}
package.

Install this package if you want to develop or compile programs which
will use %{name}.

%package -n %{staticdevelname}
Summary:	Static development files for %{name}
Group:		Development/C
Provides:	lib%{name}-static-devel = %{version}-%{release}
Requires:	%{develname} = %{version}-%{release}
Obsoletes:	%mklibname %{name} 0 -d -s

%description -n %{staticdevelname}
Static development files for %{name}.

%prep
%setup -q

%build
%configure2_5x
%make

%check
make check

%install
rm -rf %{buildroot}
%makeinstall_std

%multiarch_binaries %{buildroot}%{_bindir}/fribidi-config

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root)
%doc README AUTHORS ChangeLog TODO THANKS NEWS
%{_bindir}/fribidi

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-, root, root)
%{_bindir}/fribidi-config
%multiarch %{multiarch_bindir}/fribidi-config
%{_libdir}/*.la
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*

%files -n %{staticdevelname}
%defattr(-, root, root)
%{_libdir}/*.a
