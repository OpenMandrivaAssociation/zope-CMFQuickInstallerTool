%define Product CMFQuickInstallerTool
%define product cmfquickinstallertool
%define name    zope-%{Product}
%define version 2.0.4
%define release %mkrel 2

%define zope_minver     2.7
%define zope_home       %{_prefix}/lib/zope
%define software_home   %{zope_home}/lib/python

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    A facility for activation/deactivation of CMF products inside a CMF site
License:    GPL
Group:      System/Servers
URL:        http://plone.org/products/%{product}
Source:     http://plone.org/products/%{product}/releases/%{version}/%{Product}-%{version}.tar.gz
Requires:   zope >= %{zope_minver}
Requires:   zope-CMF
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
CMFQuickInstallerTool is a facility for comfortable
activation/deactivation of CMF compliant products inside a CMF
site.

QuickInstallerTool only tracks which objects are added,
but not what is changed or deleted.

%prep
%setup -c -q

%build
# Not much, eh? :-)


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}/%{software_home}/Products
%{__cp} -a * %{buildroot}%{software_home}/Products/
rm -rf %{buildroot}%{software_home}/Products/%{product}/debian

%clean
%{__rm} -rf %{buildroot}

%post
if [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
        service zope restart
fi

%postun
if [ -f "%{_prefix}/bin/zopectl" ] && [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
        service zope restart
fi

%files
%defattr(-,root,root)
%{software_home}/Products/*
