%define esgrep_release 1
%define esgrep_version 1.7

Name:		esgrep
Version:	%{esgrep_version}
Release:	%{esgrep_release}%{dist}
Summary:	Tool for running Kibana style queries from the command line

Group:		Applications/System
License:	none
URL:		N/A
Source0:	esgrep-%{esgrep_version}-%{esgrep_release}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:	noarch
Requires: python3
Requires: python3-PyYAML
Requires: python3-libmoose


%description
esgrep is a simple command line tool that aims to run Kibana like queries from the command line. While Kibana's Discover interface just uses the Query String Query, it also does some things like searching inside the _source field that this tool seeks to emulate. Queries may also be run using the full Elasticsearch DSL

%prep
%setup -q -n %{name}-%{esgrep_version}-%{esgrep_release}


%build


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/bin/
mkdir -p %{buildroot}/etc/esgrep/
install -m 0755 esgrep %{buildroot}/usr/local/bin/esgrep
install -m 0644 esgrep.yml %{buildroot}/etc/esgrep/esgrep.yml

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/usr/local/bin/esgrep
%config(noreplace) /etc/esgrep/esgrep.yml


%changelog
* Thu Jan 2 2024 Teddy Wells <twells@nexcess.net> - 1.7-1
- update esgrep python shebang
* Wed Jan 1 2024 Teddy Wells <twells@nexcess.net> - 1.7-0
- refactor to use libmoose
- add -c/--count, -n/--no-preserve-order flags
- replace unused -F/--fields flag with -F/--full-docs flag
* Thu Jun 1 2023 Teddy Wells <twells@nexcess.net> - 1.6-0
- apply timeout when initiating global elasticsearch object
* Wed Jun 23 2021 Ted Wells <twells@nexcess.net> - 1.5-0
- update Requires from python to python3
- remove rpm dependency for python-elasticsearch
- set timeout value to int
- use %config(noreplace) for /etc/esgrep/esgrep.yml
- include release version in setup macro (defaults to %{name}-%{version})
* Tue Nov 13 2018 Ted Wells <twells@nexcess.net> - 1.4
- don't show program field by default
- use request_timeout param instead of timeout
* Mon Jan 15 2018 Ted Wells <twells@nexcess.net> - 1.3
- add -t/--timeout flags
* Thu Jan 04 2018 Ted Wells <twells@nexcess.net> - 1.2
- initial (rpm) release
