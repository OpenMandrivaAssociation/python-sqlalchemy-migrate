%define module sqlalchemy-migrate
Name:           python-%{module}
Version:        0.6.1
Release:        %mkrel 1
License:        MIT
Source:         %{module}-%{version}.tar.bz2
Group:          Development/Python
Summary:        Database schema migration for SQLAlchemy
BuildRequires:  python-py
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Url:            http://pypi.python.org/pypi/sqlalchemy-migrate
BuildRequires:  python-setuptools
Requires:       python-nose >= 0.10
Requires:       python-sqlalchemy >= 0.5
Requires:       python-sphinx >= 0.5
Requires:       python-tempita
Requires:       python-decorator
Buildarch:	noarch

%description
Inspired by Ruby on Rails' migrations, Migrate provides a way to deal with
database schema changes in SQLAlchemy projects.

Migrate extends SQLAlchemy to have database changeset handling. It provides a
database change repository mechanism which can be used from the command line as
well as from inside python code.

%prep
%setup -q -n %module-%version

%build
CFLAGS="%{optflags}" python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --root $RPM_BUILD_ROOT --install-purelib=%{python_sitearch}

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc PKG-INFO README docs
%{_bindir}/migrate*
%{python_sitearch}/*



%changelog
* Wed Jun 08 2011 Antoine Ginies <aginies@mandriva.com> 0.6.1-1mdv2011.0
+ Revision: 683270
- import python-sqlalchemy-migrate


