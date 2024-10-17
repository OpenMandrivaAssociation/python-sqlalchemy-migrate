%define module sqlalchemy-migrate

%define debug_package %{nil}

Name:           python-%{module}
Version:        0.7.2
Release:        2
License:        MIT
Source:         http://sqlalchemy-migrate.googlecode.com/files/sqlalchemy-migrate-%{version}.tar.gz
Group:          Development/Python
Summary:        Database schema migration for SQLAlchemy
BuildRequires:  python-py
Url:            https://pypi.python.org/pypi/sqlalchemy-migrate
BuildRequires:  python-setuptools
Requires:       python-nose >= 0.10
Requires:       python-sqlalchemy >= 0.5
Requires:       python-sphinx >= 0.5
Requires:       python-tempita
Requires:       python-decorator

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
%{__python} setup.py install --root %{buildroot} --install-purelib=%{py_platsitedir}

%clean

%files 
%doc PKG-INFO README docs
%{_bindir}/migrate*
%{py_platsitedir}/*


