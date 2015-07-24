Name: nethserver-ocsinventory
Version: 0.0.1
Release: 1%{?dist}
Summary: Conifigure OCS Inventory NG
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
URL: %{url_prefix}/%{name}
License: GPL

BuildRequires: nethserver-devtools

Requires: nethserver-httpd
Requires: nethserver-mysql
Requires: nethserver-samba
Requires: ocsinventory

%description
Install and configure an OCS Inventory NG instance on NethServer

%prep
%setup

%build
%{makedocs}
perl createlinks
mkdir -p root/etc/e-smith/templates/etc/ocsinventory/ocsinventory-reports/dbconfig.inc.php
ln -s /etc/e-smith/templates-default/template-begin-php root/etc/e-smith/templates/etc/ocsinventory/ocsinventory-reports/dbconfig.inc.php/template-begin

%install
rm -rf %{buildroot}
(cd root   ; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-filelist

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%doc COPYING

%changelog
* Wed Jul 22 2015 Giovanni Bezicheri <giovanni.bezicheri@nethesis.it>
- Initial version
