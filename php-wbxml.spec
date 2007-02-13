%define		_modname	wbxml
Summary:	PHP WBXML Library wrapper
Summary(pl.UTF-8):	Wrapper PHP do biblioteki WBXML
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
BuildRequires:	rpmbuild(macros) >= 1.344
BuildRequires:	wbxml2-devel
%{?requires_php_extension}
Requires:	php-common >= 4:5.0.4
Requires:	wbxml2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a simple extension that acts as a wrapper around the
conversion functions in the WBXML Library written by Aymerick Jehanne.

%description -l en.UTF-8
This is a simple extension that acts as a wrapper around the
conversion functions in the WBXML Library written by Aymerick Jéhanne.

%description -l pl.UTF-8
To jest proste rozszerzenie obudowujące funkcje konwersji z biblioteki
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
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{_modname}.ini
; Enable %{_modname} extension module
extension=%{_modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%php_webserver_restart

%postun
if [ "$1" = 0 ]; then
	%php_webserver_restart
fi

%files
%defattr(644,root,root,755)
%doc README CREDITS
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{_modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{_modname}.so
