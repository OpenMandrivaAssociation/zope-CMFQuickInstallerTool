%define product        CMFQuickInstallerTool
%define version        1.5.9
%define release        1

%define zope_minver    2.7

%define zope_home       %{_prefix}/lib/zope
%define software_home   %{zope_home}/lib/python

Summary:        A facility for activation/deactivation of CMF products inside a CMF site
Name:           zope-%{product}
Version:        %{version}
Release:        %mkrel %{release}
License:        GPL
Group:          System/Servers
Source:         http://plone.org/products/cmfquickinstallertool/releases/%{version}/CMFQuickInstallerTool-%{version}.tar.bz2
URL:            http://sourceforge.net/projects/collective
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:      noarch
Requires:       zope >= %{zope_minver}
Requires:       zope-CMF

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
%defattr(0644, root, root, 0755)
%{software_home}/Products/*


