Summary:	Quick Image Viewver
Name:		qiv
Version:	2.3.1
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://spiegl.de/qiv/download/%{name}-%{version}.tgz
# Source0-md5:	93aea7469be64ebd35277a6dac079fc8
Patch0:		%{name}-misc.patch
URL:		http://spiegl.de/qiv/
BuildRequires:	gtk+-devel
BuildRequires:	imlib2-devel
BuildRequires:	libmagic-devel
BuildRequires:	pkg-config
BuildRequires:	xorg-libXinerama-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Quick Image Viewer (qiv) is a very small and pretty fast GDK/Imlib
image viewer.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	OPTS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir} \
	MANDIR=%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README README.TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/qiv.1*

