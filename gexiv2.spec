# TODO:
# - Add bcond for vapi support and subpackage

Summary:	GObject-based wrapper around the  Exiv2 library
Name:		gexiv2
Version:	0.1.0
Release:	1
License:	GPL
Group:		Applications/Graphics
Source0:	http://yorba.org/download/%{name}/0.1/lib%{name}-%{version}.tar.bz2
# Source0-md5:	efae406dac86aa6db4cfb75569cbb3f9
URL:		http://libexif.sourceforge.net/
Patch0:		gexiv2-libtool.patch
BuildRequires:	exiv2-devel
BuildRequires:	pkgconfig
Requires:	exiv2-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gexiv2 is a GObject-based wrapper around the  Exiv2 library. It makes
the basic features of Exiv2 available to GNOME applications.

%package devel
Summary: GObject-based wrapper around the  Exiv2 library
Requires:	exiv2-devel
Group:	Development/Libraries

%description devel
gexiv2 development files

%package static
Summary: GObject-based wrapper around the  Exiv2 library
Requires:	exiv2-static
Group:	Development/Libraries

%description static
gexiv2 static library

%prep
%setup -q -n lib%{name}-%{version}
%patch0 -p0

%build
%{__libtoolize}
./configure --prefix=%{_prefix}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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

%files static
%defattr(644,root,root,755)
%{_libdir}/lib%{name}.a
