Summary:	Hierarchical ncurses/batch data organizer and XML editor
Summary(pl):	Hierarchiczny organizer na ncurses lub wsadowy oraz edytor XML
Name:		hnb
Version:	1.8.1
Release:	1
License:	GPL
Group:		Applications/Editors
Group(de):	Applikationen/Editors
Group(pl):	Aplikacje/Edytory
Group(pt):	Aplicações/Editores
Source0:	http://hnb.sourceforge.net/%{name}-%{version}.tar.gz
Patch0:		%{name}-libs.patch
URL:		http://hnb.sourceforge.net
BuildRequires:	libxml2-devel
BuildRequires:	ncurses-devel
BuildRequires:	automake
BuildRequires:	autoconf
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
%patch0 -p1

%build
aclocal
autoconf
automake -a -c
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README ChangeLog AUTHORS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(0755,root,root) %{_bindir}/hnb
