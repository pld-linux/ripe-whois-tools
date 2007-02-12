Summary:	The RIPE version of the whois client program
Summary(pl.UTF-8):	Program do odpytywania bazy whois (stworzony przez RIPE)
Name:		ripe-whois-tools
Version:	2.4
Release:	4
License:	distributable
Group:		Applications/Networking
Source0:	ftp://ftp.ripe.net/tools/%{name}-%{version}.tar.gz
# Source0-md5:	e6bf6cd019b2fd6e49409850b92c34ad
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

%description -l pl.UTF-8
Wersja RIPE programu whois.

Ta wersja jest pomyślana dla europejskich użytkowników, ponieważ może
odpytywać serwer whois RIPE z rozszerzonymi możliwościami whois
zamiast serwera standardowego protokołu whois. Program jest w pełni
kompatybilny ze standardowym protokołem, więc może być używany jako
domyślny program whois.

Ten program bierze pod uwagę trochę dodatkowych flag, których
standardowy whois nie obsługuje. Uruchom 'whois' bez argumentów aby
zobaczyć ich objaśnienie. Większość z tych flag NIE jest obsługiwana
przez serwery whois inne niż RIPE. Aby odpytać inne serwery whois, nie
używaj żadnej z dodatkowych flag.

%prep
%setup -q -c

%build
%{__cc} %{rpmcflags} %{rpmldflags} -ansi -pedantic -DRIPE -DGLIBC whois.c -o whois
%{__cc} %{rpmcflags} %{rpmldflags} -ansi -pedantic -DRIPE -DGLIBC -DNETWORKUPDATE -lcrypt whois.c -o networkupdate
%{__cc} %{rpmcflags} %{rpmldflags} -ansi -pedantic -DRIPE -DGLIBC -lcrypt cryptpw.c -o cryptpw

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install whois $RPM_BUILD_ROOT%{_bindir}/ripe-whois
install networkupdate $RPM_BUILD_ROOT%{_bindir}/networkupdate
install cryptpw $RPM_BUILD_ROOT%{_bindir}/cryptpw

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/ripe-whois
%attr(755,root,root) %{_bindir}/networkupdate
%attr(755,root,root) %{_bindir}/cryptpw
