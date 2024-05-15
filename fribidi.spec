# fribidi is used by pango, pango is used by gst-plugins-base,
# gst-plugins-base is used by wine
%ifarch %{x86_64}
%bcond_without compat32
%endif

%define major 0
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d
%define lib32name %mklib32name %{name} %{major}
%define dev32name %mklib32name %{name} -d

Summary:	Library to support Bi-directional scripts
Name:		fribidi
Version:	1.0.14
Release:	1
License:	LGPLv2+
Group:		System/Internationalization
Url:		http://fribidi.org
Source0:	https://github.com/fribidi/fribidi/releases/download/v%{version}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	meson
%if %{with compat32}
BuildRequires:	devel(libglib-2.0)
%endif

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

%if %{with compat32}
%package -n %{lib32name}
Summary:	Library to support Bi-directional scripts (32-bit)
Group:		System/Internationalization

%description -n %{lib32name}
A library to handle bidirectional scripts (eg hebrew, arabic), so that
the display is done in the proper way; while the text data itself is
always written in logical order.
The library uses unicode internally.

%package -n %{dev32name}
Summary:	Libraries and headers for development with %{name} (32-bit)
Group:		Development/C
Requires:	%{devname} = %{version}-%{release}
Requires:	%{lib32name} = %{version}-%{release}

%description -n %{dev32name}
This package includes the libraries and header files for the %{name}
package.
%endif

%prep
%autosetup -p1
%if %{with compat32}
%meson32
%endif
%meson

%build
%if %{with compat32}
%ninja_build -C build32
%endif
%meson_build

%install
%if %{with compat32}
%ninja_install -C build32
%endif
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
%doc %{_mandir}/man3/*

%if %{with compat32}
%files -n %{lib32name}
%{_prefix}/lib/libfribidi.so.%{major}*

%files -n %{dev32name}
%{_prefix}/lib/*.so
%{_prefix}/lib/pkgconfig/*
%endif
