Summary:	A dictionary for Mana
Summary(pl.UTF-8):	Słownik dla Mana
Name:		manadic
Version:	0.1.4
Release:	3
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.jp/shinji/15963/%{name}-%{version}.tar.bz2
# Source0-md5:	051b564ccea0e0257fe404a715845fe9
Patch0:		%{name}-DESTDIR.patch
URL:		http://sourceforge.jp/projects/shinji/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	mana
Requires:	mana
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A dictionary for Mana.

%description -l pl.UTF-8
Słownik dla Mana.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc

%{__make} install \
	CHASEN_CHASENRC_PATH=$RPM_BUILD_ROOT/etc/manarc \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README doc/ipadic-ja.pdf
%config(noreplace) %verify(not md5 mtime size) /etc/manarc
%{_libdir}/mana/dic
