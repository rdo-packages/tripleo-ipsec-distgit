# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
# End of macros for py2/py3 compatibility
%global srcname tripleo_ipsec
%global rolename tripleo-ipsec

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           ansible-%{rolename}
Version:        XXX
Release:        XXX
Summary:        Ansible role for setting up IPSEC tunnels for TripleO

Group:          System Environment/Base
License:        GPLv3+
URL:            https://git.openstack.org/cgit/openstack/tripleo-ipsec
Source0:        https://tarballs.openstack.org/%{rolename}/%{rolename}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  git
BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-setuptools
BuildRequires:  python%{pyver}-pbr

# Handle python2 exception
%if %{pyver} == 2
BuildRequires:  python-d2to1
Requires:       ansible
%else
BuildRequires:  python%{pyver}-d2to1
Requires:       ansible-python3
%endif

%description

Ansible role to configure IPSEC tunnels for TripleO

%prep
%autosetup -n %{rolename}-%{upstream_version} -S git


%build
%{pyver_build}


%install
export PBR_VERSION=%{version}
export SKIP_PIP_INSTALL=1
%{pyver_install}


%files
%doc README*
%license LICENSE
%{pyver_sitelib}/%{srcname}-*.egg-info
%{_datadir}/ansible/roles/


%changelog

