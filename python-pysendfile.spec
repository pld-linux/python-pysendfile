#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Python 2 interface to sendfile(2)
Summary(pl.UTF-8):	Interfejs Pythona 2 do wywołania sendfile(2)
Name:		python-pysendfile
Version:	2.0.1
Release:	10
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.python.org/simple/pysendfile/
Source0:	https://pypi.python.org/packages/source/p/pysendfile/pysendfile-%{version}.tar.gz
# Source0-md5:	e7b301eddd703ab74a48c59a8fda1f97
URL:		https://github.com/giampaolo/pysendfile
%if %{with python2}
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-libs >= 1:2.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python 2 interface to sendfile(2).

sendfile(2) is a system call which provides a "zero-copy" way of
copying data from one file descriptor to another (a socket). The
phrase "zero-copy" refers to the fact that all of the copying of data
between the two descriptors is done entirely by the kernel, with no
copying of data into userspace buffers. This is particularly useful
when sending a file over a socket (e.g. FTP).

%description -l pl.UTF-8
Interfejs Pythona 2 do wywołania sendfile(2)

sendfile(2) to wywołanie systemowe zapewniające kopiowanie "bez
kopiowania" z jednego deskryptora pliku do innego (gniazda).
Sformułowanie "bez kopiowania" oznacza tu, że całe kopiowanie danych
między deskryptorami jest wykonywane całkowicie w jądrze, bez
kopiowania danych do buforów w przestrzeni użytkownika. Jest to
przydatne szczególnie przy wysyłaniu pliku po gnieździe (np. FTP).

%package -n python3-pysendfile
Summary:	Python 3 interface to sendfile(2)
Summary(pl.UTF-8):	Interfejs Pythona 3 do wywołania sendfile(2)
Group:		Libraries/Python
Requires:	python3-libs >= 1:3.2

%description -n python3-pysendfile
Python 3 interface to sendfile(2).

sendfile(2) is a system call which provides a "zero-copy" way of
copying data from one file descriptor to another (a socket). The
phrase "zero-copy" refers to the fact that all of the copying of data
between the two descriptors is done entirely by the kernel, with no
copying of data into userspace buffers. This is particularly useful
when sending a file over a socket (e.g. FTP).

%description -n python3-pysendfile -l pl.UTF-8
Interfejs Pythona 3 do wywołania sendfile(2)

sendfile(2) to wywołanie systemowe zapewniające kopiowanie "bez
kopiowania" z jednego deskryptora pliku do innego (gniazda).
Sformułowanie "bez kopiowania" oznacza tu, że całe kopiowanie danych
między deskryptorami jest wykonywane całkowicie w jądrze, bez
kopiowania danych do buforów w przestrzeni użytkownika. Jest to
przydatne szczególnie przy wysyłaniu pliku po gnieździe (np. FTP).

%prep
%setup -q -n pysendfile-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTHONPATH=$(pwd)/$(echo build-2/lib.*) \
%{__python} test/test_sendfile.py
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd)/$(echo build-3/lib.*) \
%{__python3} test/test_sendfile.py
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc HISTORY.rst LICENSE README.rst
%attr(755,root,root) %{py_sitedir}/sendfile.so
%{py_sitedir}/pysendfile-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pysendfile
%defattr(644,root,root,755)
%doc HISTORY.rst LICENSE README.rst
%attr(755,root,root) %{py3_sitedir}/sendfile.cpython-*.so
%{py3_sitedir}/pysendfile-%{version}-py*.egg-info
%endif
