%global srcname tripleo_ipsec
%global rolename tripleo-ipsec

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           ansible-%{rolename}
Version:        8.1.0
Release:        1%{?dist}
Summary:        Ansible role for setting up IPSEC tunnels for TripleO

Group:          System Environment/Base
License:        GPLv3+
URL:            https://git.openstack.org/cgit/openstack/tripleo-ipsec
Source0:        https://tarballs.openstack.org/%{rolename}/%{rolename}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  git
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python-d2to1
BuildRequires:  python2-pbr

Requires: ansible

%description

Ansible role to configure IPSEC tunnels for TripleO

%prep
%autosetup -n %{rolename}-%{upstream_version} -S git


%build
%py2_build


%install
export PBR_VERSION=%{version}
export SKIP_PIP_INSTALL=1
%py2_install


%files
%doc README*
%license LICENSE
%{python2_sitelib}/%{srcname}-%{version}-py%{python2_version}.egg-info
%{_datadir}/ansible/roles/


%changelog
* Thu Mar 08 2018 RDO <dev@lists.rdoproject.org> 8.1.0-1
- Update to 8.1.0

* Thu Feb 22 2018 RDO <dev@lists.rdoproject.org> 8.0.2-1
- Update to 8.0.2


