Summary:	FTP port bouncer
Summary(pl.UTF-8):   Przekazywanie portów FTP
Name:		hpbnc
Version:	1.5
Release:	0.2
License:	GPL
Group:		Applications/Networking
Source0:	http://mobilcom.dyndns.org/~iwdisb/glftpd/%{name}.v%{version}_test2.tar.gz
# Source0-md5:	cdaf5880e6a4edc1b070fb2375a1f83d
Patch0:		hpbnc-nofork.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FTP port bouncer.

%description -l pl.UTF-8
Program do przekazywania portów FTP.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__cc} %{rpmcflags} %{rpmldflags} -o hpbnc hpbnc.c rfc931.c

%install
rm -rf $RPM_BUILD_ROOT

install -D hpbnc $RPM_BUILD_ROOT%{_bindir}/hpbnc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGELOG hpbnc.conf
%attr(755,root,root) %{_bindir}/*
