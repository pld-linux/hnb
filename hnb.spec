Summary:	Hierarchical ncurses/batch data organizer and XML editor
Summary(pl):	Hierarchiczny organizer na ncurses lub wsadowy oraz edytor XML
Name:		hnb
Version:	1.8.1
Release:	1
License:	GPL
Group:		Applications/Editors
Group(de):	Applikationen/Editors
Group(pl):	Aplikacje/Edytory
Group(pt):	Aplica��es/Editores
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
zbierania wielu rodzaj�w danych w jednym miejscu, np. adres�w, list
rzeczy do zrobienia, pomys��w, recenzji, efekt�w "burzy m�zg�w",
przygotowywania przem�wie�, prowadzenia notatek, oraz prawdopodobnie
wielu wi�cej rzeczy, o kt�rych autor jeszcze nie pomy�la�...

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
