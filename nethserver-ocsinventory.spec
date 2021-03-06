Name: nethserver-ocsinventory
Version: 1.1.8
Release: 2%{?dist}
Summary: Configure OCS Inventory NG
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
URL: %{url_prefix}/%{name}
License: GPL

BuildRequires: nethserver-devtools

Requires: nethserver-httpd
Requires: nethserver-mysql
Requires: ocsinventory >= 2.3.0

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
%dir %{_nseventsdir}/%{name}-update

%postun
if [ $1 == 0 ] ; then
    /usr/bin/rm -f /etc/httpd/conf.d/ocsinventory-reports.conf
    /usr/bin/rm -f /etc/httpd/conf.d/ocsinventory-server.conf
    /usr/bin/systemctl reload httpd
fi

%changelog
* Sun Jul 05 2020 stephane de Labrusse <stephdl@de-labrusse.fr> 1.1.8
- Remove http templates after rpm removal

* Wed Jun 5 2019 Stephane de Labrusse  <stephdl@de-labrusse.fr> - 1.1.7
- Enable ocsinventory repo with  software-repos-save

* Sun Sep 10 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.6-1.ns7
- Restart httpd service on trusted-network

* Wed Mar 29 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 1.1.5-1.ns7
- Template expansion on trusted-network

* Mon Mar 20 2017 stephane de Labrusse <stephdl@de-labrusse.fr> 1.1.4-2.ns7
- Upgrade to ocsinventory 2.3.0

* Sat Mar 18 2017 stephane de Labrusse <stephdl@de-labrusse.fr> 1.1.3.ns7
- First release to NS7

* Mon Sep 14 2015 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.1-1
- OCS Inventory LDAP authentication - Enhancement #3250 [NethServer]

* Tue Aug 25 2015 Davide Principi <davide.principi@nethesis.it> - 1.0.0-1
- Initial OCS Inventory NG package - Feature #3230 [NethServer]

* Wed Jul 22 2015 Giovanni Bezicheri <giovanni.bezicheri@nethesis.it>
- Initial version
