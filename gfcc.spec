Summary:	GTK firewall control center
Summary(pl):	Centrum kontroli firewalla
Name:		gfcc
Version:	0.7.2.1
Release:	1
Copyright:	GPL
Group:		X11/Networking/Utilities
Group(pl):	X11/Sieciowe/Narzêdzia
Source0:	http://account.joayo.net/~tri/%{name}-%{version}.tar.gz
Source1:	gfcc.desktop
Patch0:		gfcc-inc.patch
Patch1:		gfcc-gtkrc.patch
URL:		http://account.joayo.net/~tri/index.html
BuildRequires:	XFree86-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	glib-devel >= 1.2.0
BuildRequires:	libipfwc
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix		/usr/X11R6
%define		_applnkdir	%{_datadir}/applnk

%description
gfcc (GTK+ Firewall Control Center) is a GTK+ application which can
control Linux firewall policies and rules, based on ipchains package.

%description -l pl
gfcc jest aplikacj± opart± na ipchains i wykorzystuj±c± bibliotekê GTK+,
która umo¿liwia zarz±dzanie filtrowaniem pakietów IP.

%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build
LDFLAGS="-s"; export LDFLAGS
%configure \
	--with-ipfwc=/usr/lib
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Administration

make install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Administration

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/gfcc

%{_applnkdir}/Administration/gfcc.desktop
