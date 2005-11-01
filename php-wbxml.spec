Summary:	PHP WBXML Libraray wrapper
Name:		php-wbxml
Version:	0.1
Release:	0.1
License:	Apache
Group:		Libraries
Source0:	http://www.k-fish.de/fileadmin/wbxml-%{version}.tar.gz
URL:		http://www.k-fish.de/SyncML_support.57.0.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	wbxml2-devel
BuildRequires:	php-devel
Requires:	wbxml2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/php

%description
This is a simple extension that acts as a wrapper around the
conversion functions in the WBXML Library written by Aymerick Jéhanne.

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
install -d $RPM_BUILD_ROOT

%{__make} install INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%preun
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove wbxml %{_sysconfdir}/php.ini
fi

%post
%{_sbindir}/php-module-install install wbxml %{_sysconfdir}/php.ini

%files
%defattr(644,root,root,755)
%doc README CREDITS
%{_libdir}/php/*
