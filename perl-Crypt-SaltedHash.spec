%define upstream_name    Crypt-SaltedHash
Name:		perl-%{upstream_name}
Version:	0.12
Release:	2
Summary:	Working with salted hashes

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/robrwo/perl-Crypt-SaltedHash
Source0:	https://cpan.metacpan.org/authors/id/R/RR/RRWO/Crypt-SaltedHash-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires: perl(Digest::SHA)
BuildRequires: perl(Test::Fatal)
BuildRequires:	perl(Digest)
BuildRequires:	perl(Module::Build::Compat)
BuildArch:	noarch

%description
The 'Crypt::SaltedHash' module provides an object oriented interface to
create salted (or seeded) hashes of clear text data. The original
formalization of this concept comes from RFC-3112 and is extended by the
use of different digital agorithms.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/Crypt

%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.50.0-2mdv2011.0
+ Revision: 680870
- mass rebuild

* Wed Oct 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.50.0-1mdv2011.0
+ Revision: 455626
- import perl-Crypt-SaltedHash


* Wed Oct 07 2009 cpan2dist 0.05-1mdv
- initial mdv release, generated with cpan2dist

