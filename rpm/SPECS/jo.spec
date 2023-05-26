Name:           jo
Version:        1.9
Release:        10%{?dist}
Summary:        JSON output from a shell
License:        GPLv2
URL:            https://github.com/jpmens/jo
Source0:        https://github.com/jpmens/jo/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  make
BuildRequires:  musl-static >= 1.2.4-0


%description
jo is a small utility to create JSON objects
https://jpmens.net/2016/03/05/a-shell-command-to-create-json-jo/


%prep
%setup -qn %{name}-%{version}


%build
%configure \
  CC="musl-gcc" \
  CFLAGS="-fPIC -Wl,-static" \
  LDFLAGS="-static"
make %{?_smp_mflags}


%install
make DESTDIR=%{buildroot} install-strip


%check
make check


%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*
%{_sysconfdir}/bash_completion.d/%{name}.bash
%{_datarootdir}/zsh/*/*%{name}


%changelog
* Thu May 25 2023 ryanwoodsmall
- musl 1.2.4

* Sun Nov 6 2022 ryan woodsmall
- jo 1.7
- jo 1.9

* Fri Apr 29 2022 ryan woodsmall
- release bump for musl 1.2.3

* Thu Jan 27 2022 ryan woodsmall
- jo 1.6
- jo 1.5

* Fri Jan 15 2021 ryan woodsmall
- release bump for musl 1.2.2

* Wed Dec 30 2020 ryan woodsmall
- release bump for musl CVE-2020-28928

* Thu Dec 03 2020 ryan woodsmall
- jo 1.4

* Tue Oct 20 2020 ryan woodsmall
- release bump for musl 1.2.1

* Tue Nov 12 2019 ryan woodsmall
- jo 1.3

* Sat Oct 26 2019 ryan woodsmall
- release bump for musl 1.1.24

* Wed Jul 17 2019 ryan woodsmall
- release bump for musl 1.1.23

* Thu Apr 11 2019 ryan woodsmall
- release bump for musl 1.1.22

* Tue Jan 22 2019 ryan woodsmall
- release bump for musl-1.1.21

* Sat Dec 22 2018 ryan woodsmall
- jo 1.2

* Thu Oct 18 2018 ryan woodsmall
- jo 1.1
