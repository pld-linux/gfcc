Summary:	GTK firewall control center
Summary(pl):	Centrum kontroli firewalla
Summary(pt_BR):	Centro de controle de firewall GTK
Name:		gfcc
Version:	0.7.4
Release:	6
License:	GPL
Group:		X11/Applications/Networking
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	37644150506d6a76d4b0ec3f0e5a14aa
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-inc.patch
Patch1:		%{name}-gtkrc.patch
Icon:		gfcc.xpm
#URL:		http://account.joayo.net/~tri/index.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libipfwc
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gfcc (GTK+ Firewall Control Center) is a GTK+ application which can
control Linux firewall policies and rules, based on ipchains package.

%description -l pl
gfcc jest aplikacj± opart± na ipchains i wykorzystuj±c± bibliotekê
GTK+, która umo¿liwia zarz±dzanie filtrowaniem pakietów IP.

%description -l pt_BR
O gfcc (GTK+ Firewall Control Center) é uma aplicação GTK+ que pode
controlar políticas e regras de firewall, baseado no pacote ipchains.

%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-ipfwc=/usr/%{_lib}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/gfcc
%{_desktopdir}/gfcc.desktop
%{_pixmapsdir}/*
