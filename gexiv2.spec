#
# Conditional build:
%bcond_without	static_libs	# static library

Summary:	GObject-based wrapper around the Exiv2 library
Summary(pl.UTF-8):	Oparte na GObject obudowanie biblioteki Exiv2
Name:		gexiv2
Version:	0.10.3
Release:	5
License:	GPL v2
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gexiv2/0.10/%{name}-%{version}.tar.xz
# Source0-md5:	f255100a009027d4eaa0f075bb79c655
URL:		https://wiki.gnome.org/Projects/gexiv2
BuildRequires:	exiv2-devel >= 0.21
BuildRequires:	glib2-devel >= 1:2.26.1
BuildRequires:	gobject-introspection-devel >= 0.10
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	m4
BuildRequires:	pkgconfig >= 1:0.26
BuildRequires:	python >= 2
BuildRequires:	python-pygobject3-devel >= 3
BuildRequires:	python3 >= 1:3.2
BuildRequires:	python3-pygobject3-devel >= 3
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	exiv2-libs >= 0.21
Requires:	glib2 >= 1:2.26.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gexiv2 is a GObject-based wrapper around the Exiv2 library. It makes
the basic features of Exiv2 available to GNOME applications.

%description -l pl.UTF-8
gexiv2 to oparte na GObject obudowanie biblioteki Exiv2. Udostępnia
podstawowe możliwości Exiv2 aplikacjom GNOME.

%package devel
Summary:	Header files for gexiv2 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki gexiv2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	exiv2-devel >= 0.21
Requires:	glib2-devel >= 1:2.26.1
Requires:	libstdc++-devel

%description devel
Header files for gexiv2 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki gexiv2.

%package static
Summary:	Static gexiv2 library
Summary(pl.UTF-8):	Statyczna biblioteka gexiv2
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gexiv2 library.

%description static -l pl.UTF-8
Statyczna biblioteka gexiv2.

%package -n python-gexiv2
Summary:	Python 2 binding for gexiv2 library
Summary(pl.UTF-8):	Wiązanie Pythona 2 do biblioteki gexiv2
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python-pygobject3 >= 3

%description -n python-gexiv2
Python 2 binding for gexiv2 library.

%description -n python-gexiv2 -l pl.UTF-8
Wiązanie Pythona 2 do biblioteki gexiv2.

%package -n python3-gexiv2
Summary:	Python 3 binding for gexiv2 library
Summary(pl.UTF-8):	Wiązanie Pythona 3 do biblioteki gexiv2
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python3-pygobject3 >= 3

%description -n python3-gexiv2
Python 3 binding for gexiv2 library.

%description -n python3-gexiv2 -l pl.UTF-8
Wiązanie Pythona 3 do biblioteki gexiv2.

%package -n vala-gexiv2
Summary:	Vala binding for gexiv2 library
Summary(pl.UTF-8):	Wiązanie języka vala do biblioteki gexiv2
Group:		Development/Languages
Requires:	%{name}-devel = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description -n vala-gexiv2
Vala binding for gexiv2 library.

%description -n vala-gexiv2 -l pl.UTF-8
Wiązanie języka vala do biblioteki gexiv2.

%prep
%setup -q

%build
%configure \
	--enable-introspection \
	%{?with_static_libs:--enable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_comp $RPM_BUILD_ROOT%{py_sitedir}/gi/overrides
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}/gi/overrides
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS
%attr(755,root,root) %{_libdir}/libgexiv2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgexiv2.so.2
%{_libdir}/girepository-1.0/GExiv2-0.10.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgexiv2.so
%{_libdir}/libgexiv2.la
%{_datadir}/gir-1.0/GExiv2-0.10.gir
%{_includedir}/gexiv2
%{_pkgconfigdir}/gexiv2.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgexiv2.a
%endif

%files -n python-gexiv2
%defattr(644,root,root,755)
%{py_sitedir}/gi/overrides/GExiv2.py[co]

%files -n python3-gexiv2
%defattr(644,root,root,755)
%{py3_sitedir}/gi/overrides/GExiv2.py

%files -n vala-gexiv2
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/gexiv2.vapi
