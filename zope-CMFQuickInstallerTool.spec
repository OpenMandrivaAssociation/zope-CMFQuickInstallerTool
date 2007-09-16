%define Product CMFQuickInstallerTool
%define product cmfquickinstallertool
%define name    zope-%{Product}
%define version 2.0.3
%define release %mkrel 1

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

Therefore it has to be installed as a tool inside a CMF portal,
where it stores the information about the installed products.

The requirements for a product to be installable with
QuickInstallerTool are quite simple (almost all existing CMF
products fulfill them):

  External Product:  The product has to implement an external
                     method 'install' in a python module 'Install.py'
                     in its Extensions directory.

  TTW Product: The product has to have a 'Install' folder
               and have a python script titled 'install' inside
               that folder.

Products can be uninstalled and QuickInstellerTool removes
the following items a product creates during install:

portal types,
portal skins,
portal actions,
portalobjects (objects created in the root of the portal),
workflows,
left and right slots (also checks them only for the portal)

Attention: QuickInstallerTool just tracks which objects are
ADDED, but not what is changed or deleted.

second Attention:
QuickInstallerTool just can uninstall products that are
installed via QuickInstallerTool


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
