%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x5d2d1e4fb8d38e6af76c50d53d4fec30cf5ce3da
%global srcname tripleo_ipsec
%global rolename tripleo-ipsec

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           ansible-%{rolename}
Version:        10.0.1
Release:        1%{?dist}
Summary:        Ansible role for setting up IPSEC tunnels for TripleO

Group:          System Environment/Base
License:        GPLv3+
URL:            https://git.openstack.org/cgit/openstack/tripleo-ipsec
Source0:        https://tarballs.openstack.org/%{rolename}/%{rolename}-%{version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{rolename}/%{rolename}-%{version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
BuildRequires:  openstack-macros
%endif
BuildRequires:  git
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr

Requires:       python3dist(ansible)

%description

Ansible role to configure IPSEC tunnels for TripleO

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{rolename}-%{upstream_version} -S git


%build
%{py3_build}


%install
export PBR_VERSION=%{version}
export SKIP_PIP_INSTALL=1
%{py3_install}


%files
%doc README*
%license LICENSE
%{python3_sitelib}/%{srcname}-*.egg-info
%{_datadir}/ansible/roles/


%changelog
* Fri Mar 19 2021 RDO <dev@lists.rdoproject.org> 10.0.1-1
- Update to 10.0.1

* Thu Jan 14 2021 RDO <dev@lists.rdoproject.org> 10.0.0-1
- Update to 10.0.0


