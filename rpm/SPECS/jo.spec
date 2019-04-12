Name:           jo
Version:        1.2
Release:        3%{?dist}
Summary:        JSON output from a shell
License:        GPLv2
URL:            https://github.com/jpmens/jo
Source0:        https://github.com/jpmens/jo/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  make
BuildRequires:  musl-static >= 1.1.22


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


%changelog
* Thu Apr 11 2019 ryan woodsmall <rwoodsmall@gmail.com> - 1.2-3
- release bump for musl 1.1.22

* Tue Jan 22 2019 ryan woodsmall <rwoodsmall@gmail.com> - 1.2-2
- release bump for musl-1.1.21

* Sat Dec 22 2018 ryan woodsmall <rwoodsmall@gmail.com> - 1.2-1
- jo 1.2

* Thu Oct 18 2018 ryan woodsmall <rwoodsmall@gmail.com> - 1.1-1
- jo 1.1
