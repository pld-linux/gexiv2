# NOTE: on updates verify GExiv2.py python2 compatibility;
#       when broken, fork last compatible version of GExiv2.py to python-gexiv2.spec
#
# Conditional build:
%bcond_without	apidocs		# disable gtk-doc
%bcond_without	static_libs	# static library

Summary:	GObject-based wrapper around the Exiv2 library
Summary(pl.UTF-8):	Oparte na GObject obudowanie biblioteki Exiv2
Name:		gexiv2
Version:	0.14.2
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	https://download.gnome.org/sources/gexiv2/0.14/%{name}-%{version}.tar.xz
# Source0-md5:	1e65556fad5d24a4c365696544d8c945
Patch0:		%{name}-python-archdir.patch
URL:		https://wiki.gnome.org/Projects/gexiv2
BuildRequires:	exiv2-devel >= 0.27.4
BuildRequires:	glib2-devel >= 1:2.46.0
BuildRequires:	gobject-introspection-devel >= 0.10
BuildRequires:	gtk-doc >= 1.14
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	meson >= 0.64
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig >= 1:0.26
BuildRequires:	python >= 2
BuildRequires:	python-pygobject3-devel >= 3
BuildRequires:	python3 >= 1:3.2
BuildRequires:	python3-pygobject3-devel >= 3
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.752
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala
BuildRequires:	xz
Requires:	exiv2-libs >= 0.27.4
Requires:	glib2 >= 1:2.46.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# must be in sitedir due to "..overrides" and "..module" imports
%define		py_gi_overridesdir	%{py_sitedir}/gi/overrides
%define		py3_gi_overridesdir	%{py3_sitedir}/gi/overrides

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
Requires:	exiv2-devel >= 0.27.4
Requires:	glib2-devel >= 1:2.46.0
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

%package apidocs
Summary:	gexiv2 API documentation
Summary(pl.UTF-8):	Dokumentacja API gexiv2
Group:		Documentation
Requires:	gtk-doc-common
BuildArch:	noarch

%description apidocs
gexiv2 API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API gexiv2.

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
BuildArch:	noarch

%description -n vala-gexiv2
Vala binding for gexiv2 library.

%description -n vala-gexiv2 -l pl.UTF-8
Wiązanie języka vala do biblioteki gexiv2.

%prep
%setup -q
%patch0 -p1

%build
%meson build \
	%{?with_apidocs:-Dgtk_doc=true}

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

# no longer installed by meson
install -d $RPM_BUILD_ROOT%{py_sitedir}/gi/overrides
cp -p GExiv2.py $RPM_BUILD_ROOT%{py_sitedir}/gi/overrides
%py_comp $RPM_BUILD_ROOT%{py_sitedir}/gi/overrides
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}/gi/overrides
%py_postclean

%py3_comp $RPM_BUILD_ROOT%{py3_sitedir}/gi/overrides
%py3_ocomp $RPM_BUILD_ROOT%{py3_sitedir}/gi/overrides

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
%{_datadir}/gir-1.0/GExiv2-0.10.gir
%{_includedir}/gexiv2
%{_pkgconfigdir}/gexiv2.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgexiv2.a
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gexiv2
%endif

%files -n python-gexiv2
%defattr(644,root,root,755)
%{py_gi_overridesdir}/GExiv2.py[co]

%files -n python3-gexiv2
%defattr(644,root,root,755)
%{py3_gi_overridesdir}/GExiv2.py
%{py3_gi_overridesdir}/__pycache__/GExiv2.cpython-*.py[co]

%files -n vala-gexiv2
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/gexiv2.deps
%{_datadir}/vala/vapi/gexiv2.vapi
