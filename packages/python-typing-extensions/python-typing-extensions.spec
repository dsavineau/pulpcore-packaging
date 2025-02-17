%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name typing-extensions

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        3.10.0.2
Release:        1%{?dist}
Summary:        Backported and Experimental Type Hints for Python 3

License:        PSF
URL:            https://github.com/python/typing/blob/master/typing_extensions/README.rst
Source0:        https://files.pythonhosted.org/packages/source/t/%{pypi_name}/typing_extensions-%{version}.tar.gz
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
%autosetup -n typing_extensions-%{version}
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
%{python3_sitelib}/__pycache__/typing_extensions.*
%{python3_sitelib}/typing_extensions.py
%{python3_sitelib}/typing_extensions-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Nov 09 2021 Odilon Sousa <osousa@redhat.com> - 3.10.0.2-1
- Release python-typing-extensions 3.10.0.2

* Fri Sep 10 2021 Evgeni Golov - 3.7.4.3-3
- Don't require typing, our Python is new enough

* Wed Sep 08 2021 Evgeni Golov - 3.7.4.3-2
- Build against Python 3.8

* Tue Sep 01 2020 Evgeni Golov 3.7.4.3-1
- Update to 3.7.4.3

* Tue Apr 14 2020 Evgeni Golov 3.7.4.2-1
- Update to 3.7.4.2

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.7.4.1-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 3.7.4.1-1
- Initial package.
