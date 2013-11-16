Summary:	GObject-based wrapper around the Exiv2 library
Summary(pl.UTF-8):	Oparte na GObject obudowanie biblioteki Exiv2
Name:		gexiv2
Version:	0.7.0
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://yorba.org/download/gexiv2/0.7/lib%{name}-%{version}.tar.xz
# Source0-md5:	15f5adab32022c6ab3f66d82eed7c1e8
URL:		http://trac.yorba.org/wiki/gexiv2
BuildRequires:	exiv2-devel >= 0.21
BuildRequires:	glib2-devel >= 1:2.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	m4
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
Requires:	exiv2-libs >= 0.21
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
Requires:	glib2-devel >= 1:2.0
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

%package -n vala-gexiv2
Summary:	Vala binding for gexiv2 library
Summary(pl.UTF-8):	Wiązanie języka vala do biblioteki gexiv2
Group:		Development/Languages
Requires:	%{name}-devel = %{version}-%{release}

%description -n vala-gexiv2
Vala binding for gexiv2 library.

%description -n vala-gexiv2 -l pl.UTF-8
Wiązanie języka vala do biblioteki gexiv2.

%prep
%setup -q -n lib%{name}-%{version}

%build
# not autoconf-generated
./configure \
	--prefix=%{_prefix}

%{__make} \
	CFLAGS="%{rpmcflags}" \
	CXX="%{__cxx}" \
	LIB="%{_lib}" \
	LDFLAGS="-lm"

# fix hardcoded ${exec_prefix}/lib
sed -i -e 's,^libdir=.*,libdir=%{_libdir},' gexiv2.pc

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	LIB="%{_lib}"

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS MAINTAINERS NEWS README THANKS
%attr(755,root,root) %{_libdir}/libgexiv2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgexiv2.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgexiv2.so
%{_libdir}/libgexiv2.la
%{_includedir}/gexiv2
%{_pkgconfigdir}/gexiv2.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgexiv2.a

%files -n vala-gexiv2
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/gexiv2.vapi
