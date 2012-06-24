Summary:	Hierarchical ncurses/batch data organizer and XML editor
Summary(pl):	Hierarchiczny organizer na ncurses lub wsadowy oraz edytor XML-a
Name:		hnb
Version:	1.8.1
Release:	3
License:	GPL
Group:		Applications/Editors
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	bcbf069d7cb3d3f80d7ee39bc6f5f669
Patch0:		%{name}-libs.patch
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
zbierania wielu rodzaj�w danych w jednym miejscu, np. adres�w, list
rzeczy do zrobienia, pomys��w, recenzji, efekt�w "burzy m�zg�w",
przygotowywania przem�wie�, prowadzenia notatek, oraz prawdopodobnie
wielu wi�cej rzeczy, o kt�rych autor jeszcze nie pomy�la�...

%prep
%setup  -q
%patch0 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog AUTHORS contrib
%attr(0755,root,root) %{_bindir}/hnb
%{_mandir}/man1/*
