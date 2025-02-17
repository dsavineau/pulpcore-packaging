%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name pytz

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        2021.3
Release:        1%{?dist}
Summary:        World timezone definitions, modern and historical

License:        MIT
URL:            http://pythonhosted.org/pytz
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}


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
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Wed Nov 03 2021 Odilon Sousa 2021.3-1
- Update to 2021.3

* Mon Sep 06 2021 Evgeni Golov - 2021.1-2
- Build against Python 3.8

* Fri Mar 19 2021 Evgeni Golov 2021.1-1
- Update to 2021.1

* Mon Nov 02 2020 Evgeni Golov 2020.4-1
- Update to 2020.4

* Tue Apr 28 2020 Evgeni Golov 2020.1-1
- Update to 2020.1

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2019.3-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 2019.3-1
- Initial package.
