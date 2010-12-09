# TODO:
# - Add bcond for vapi support and subpackage

Summary:	GObject-based wrapper around the  Exiv2 library
Name:		gexiv2
Version:	0.2.1
Release:	1
License:	GPL
Group:		Applications/Graphics
Source0:	http://yorba.org/download/gexiv2/0.2/lib%{name}-%{version}.tar.bz2
# Source0-md5:	eda379b9a7b482988f55d5d79962d16b
URL:		http://trac.yorba.org/wiki/gexiv2
BuildRequires:	exiv2-devel >= 0.19
BuildRequires:	pkgconfig
BuildRequires:	vala
Requires:	exiv2-libs >= 0.19
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gexiv2 is a GObject-based wrapper around the Exiv2 library. It makes
the basic features of Exiv2 available to GNOME applications.

%package devel
Summary:	GObject-based wrapper around the  Exiv2 library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	exiv2-devel >= 0.19

%description devel
gexiv2 development files

%package static
Summary:	GObject-based wrapper around the  Exiv2 library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	exiv2-static >= 0.19

%description static
gexiv2 static library

%prep
%setup -q -n lib%{name}-%{version}

%build
%{__libtoolize}
./configure --prefix=%{_prefix}

%{__make} \
	LIB="%{_lib}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	LIB="%{_lib}"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib%{name}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/lib%{name}.so.0
%attr(755,root,root) %{_libdir}/lib%{name}.so

%files devel
%defattr(644,root,root,755)
%{_libdir}/lib%{name}.la
%{_includedir}/%{name}
%{_pkgconfigdir}/%{name}.pc
%{_datadir}/vala/vapi/gexiv2.vapi

%files static
%defattr(644,root,root,755)
%{_libdir}/lib%{name}.a
