Summary:	The RIPE version of the whois client program
Summary(pl):	Program do odpytywania bazy whois (stworzony przez RIPE)
Name:		ripe-whois
Version:	2.4
Release:	1
License:	Distributable
Group:		Applications/Networking
Group(de):	Applikationen/Netzwerkwesen
Group(pl):	Aplikacje/Sieciowe
Source0:	ftp://ftp.ripe.net/tools/%{name}-tools-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The RIPE version of the whois client program.

This is intended for European users as it will query a RIPE whois
server with extended whois capabilities rather than a standard whois
protocol server. The whois program is fully compatible with the
standard whois protocol and can thus replace your default whois
program.

This program is aware of quite some extra flags that the standard
whois doesn't support. Just try 'whois' without arguments to see an
explanation of these. Please note that most of these flags are NOT
supported by non RIPE whois servers. In cases where you use this
client to query non RIPE whois servers, you should not use any of
these flags.

%description -l pl
Wersja RIPE programu whois.

Ta wersja jest pomy¶lana dla europejskich u¿ytkowników, poniewa¿ mo¿e
odpytuje serwer whois RIPE z rozszerzonymi mo¿liwo¶ciami whois zamiast
serwera standardowego protoko³u whois. Program jest w pe³ni
kompatybilny ze standardowym i mo¿e zast±piæ standardowy program
whois.

Ten program bierze pod uwagê trochê dodatkowych flag, których
standardowy whois nie obs³uguje. Uruchom 'whois' bez argumentów aby
zobaczyæ ich obja¶nienie. Wiêkszo¶æ z tych flag NIE jest obs³ugiwana
przez serwery whois inne ni¿ RIPE. Aby odpytaæ inne serwery whois, nie
u¿ywaj ¿adnej z dodatkowych flag.

%prep
%setup -q -c %{name} -n %{name}

%build
%{__cc} %{rpmcflags} %{rpmldflags} -ansi -pedantic -DRIPE -DGLIBC whois.c -o whois
%{__cc} %{rpmcflags} %{rpmldflags} -ansi -pedantic -DRIPE -DGLIBC -DNETWORKUPDATE -lcrypt whois.c -o networkupdate
%{__cc} %{rpmcflags} %{rpmldflags} -ansi -pedantic -DRIPE -DGLIBC -lcrypt cryptpw.c -o cryptpw

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install whois $RPM_BUILD_ROOT/%{_bindir}/ripe-whois
install networkupdate $RPM_BUILD_ROOT/%{_bindir}/networkupdate
install cryptpw $RPM_BUILD_ROOT/%{_bindir}/cryptpw

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) %{_bindir}/ripe-whois
%attr(755,root,root) %{_bindir}/networkupdate
%attr(755,root,root) %{_bindir}/cryptpw
