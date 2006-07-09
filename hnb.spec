Summary:	Hierarchical ncurses/batch data organizer and XML editor
Summary(pl):	Hierarchiczny organizer na ncurses lub wsadowy oraz edytor XML-a
Name:		hnb
Version:	1.9.17
Release:	1
License:	GPL
Group:		Applications/Editors
Source0:	http://dl.sourceforge.net/hnb/%{name}-%{version}.tar.gz
# Source0-md5:	c73b5f63d8ffe1976c915c1f8265951d
URL:		http://hnb.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libxml2-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
hierarchical notebook (hnb) is program to organize, many kinds of data
in one place, for example adresses, todo lists, ideas, book "reviews",
brainstorming, organizing a speech, making a structured packing list
random notes, and probably many more I haven't thought of yet..

%description -l pl
Hierarchiczny notes (hnb - hierarchical notebook) to program do
zbierania wielu rodzajów danych w jednym miejscu, np. adresów, list
rzeczy do zrobienia, pomys³ów, recenzji, efektów "burzy mózgów",
przygotowywania przemówieñ, prowadzenia notatek, oraz prawdopodobnie
wielu wiêcej rzeczy, o których autor jeszcze nie pomy¶la³...

%prep
%setup  -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -I/usr/include/ncurses -Ilibcli -I.. -DHAVE_CONFIG_H"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install src/hnb	$RPM_BUILD_ROOT%{_bindir}/hnb
install doc/hnb.1 $RPM_BUILD_ROOT%{_mandir}/man1/hnb.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/hnb
%{_mandir}/man1/*
