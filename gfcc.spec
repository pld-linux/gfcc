Summary:	GTK firewall control center
Summary(pl):	Centrum kontroli firewalla
Name:		gfcc
Version:	0.7.4
Release:	3
License:	GPL
Group:		X11/Applications/Networking
Group(de):	X11/Applikationen/Netzwerkwesen
Group(pl):	X11/Aplikacje/Sieciowe
Source0:	http://icarus.autostock.co.kr/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-inc.patch
Patch1:		%{name}-gtkrc.patch
Icon:		%{name}.xpm
URL:		http://account.joayo.net/~tri/index.html
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libipfwc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
gfcc (GTK+ Firewall Control Center) is a GTK+ application which can
control Linux firewall policies and rules, based on ipchains package.

%description -l pl
gfcc jest aplikacj± opart± na ipchains i wykorzystuj±c± bibliotekê
GTK+, która umo¿liwia zarz±dzanie filtrowaniem pakietów IP.

%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build
%configure \
	--with-ipfwc=/usr/lib
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Administration,%{_datadir}/pixmaps}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Administration
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/gfcc
%{_applnkdir}/Administration/gfcc.desktop
%{_datadir}/pixmaps/*
