%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name idna-ssl

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        1.1.0
Release:        4%{?dist}
Summary:        Patch ssl.match_hostname for Unicode(idna) domains support

License:        MIT
URL:            https://github.com/aio-libs/idna-ssl
Source0:        https://files.pythonhosted.org/packages/source/i/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-idna >= 2.0


%description -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
%{?scl:EOF}


%build
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%py3_build
%{?scl:EOF}


%install
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%py3_install
%{?scl:EOF}


%files -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/__pycache__/idna_ssl.*
%{python3_sitelib}/idna_ssl.py
%{python3_sitelib}/idna_ssl-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Sep 06 2021 Evgeni Golov - 1.1.0-4
- Build against Python 3.8

* Thu Nov 05 2020 Evgeni Golov - 1.1.0-3
- Fix License tag in spec file

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.1.0-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 1.1.0-1
- Initial package.
