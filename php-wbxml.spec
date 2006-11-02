%define		_modname	wbxml
%define		_sysconfdir	/etc/php
%define		extensionsdir	%(php-config --extension-dir 2>/dev/null)
Summary:	PHP WBXML Library wrapper
Summary(pl):	Wrapper PHP do biblioteki WBXML
Name:		php-wbxml
Version:	0.1
Release:	0.2
License:	PHP 2.02
Group:		Libraries
Source0:	http://www.k-fish.de/fileadmin/wbxml-%{version}.tar.gz
# Source0-md5:	73c23a4848478715254be2dc104596ec
URL:		http://www.k-fish.de/SyncML_support.57.0.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	php-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.322
BuildRequires:	wbxml2-devel
%{?requires_php_extension}
Requires:	%{_sysconfdir}/conf.d
Requires:	wbxml2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a simple extension that acts as a wrapper around the
conversion functions in the WBXML Library written by Aymerick Jehanne.

%description -l en
This is a simple extension that acts as a wrapper around the
conversion functions in the WBXML Library written by Aymerick Jéhanne.

%description
To jest proste rozszerzenie obudowuj±ce funkcje konwersji z biblioteki
WBXML napisanej przez Aymericka Jéhanne'a.

%prep
%setup -q -n wbxml-%{version}

%build
phpize
%{__aclocal}
%{__autoconf}
%{__autoheader}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/conf.d,%{extensionsdir}}

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

cat <<'EOF' > $RPM_BUILD_ROOT%{_sysconfdir}/conf.d/%{_modname}.ini
; Enable %{_modname} extension module
extension=%{_modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -f /etc/apache/conf.d/??_mod_php.conf ] || %service -q apache restart
[ ! -f /etc/httpd/httpd.conf/??_mod_php.conf ] || %service -q httpd restart

%postun
if [ "$1" = 0 ]; then
	[ ! -f /etc/apache/conf.d/??_mod_php.conf ] || %service -q apache restart
	[ ! -f /etc/httpd/httpd.conf/??_mod_php.conf ] || %service -q httpd restart
fi

%files
%defattr(644,root,root,755)
%doc README CREDITS
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/%{_modname}.ini
%attr(755,root,root) %{extensionsdir}/%{_modname}.so
