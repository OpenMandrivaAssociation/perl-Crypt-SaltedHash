%define upstream_name    Crypt-SaltedHash
%define upstream_version 0.05

Name:       perl-%{upstream_name}
%if %mdkversion > 200900
Version:    %perl_convert_version %{upstream_version}
%else
Version:    %{upstream_version}
%endif
Release:    %mkrel 1
Summary:    Working with salted hashes
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Crypt/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Digest)
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
The 'Crypt::SaltedHash' module provides an object oriented interface to
create salted (or seeded) hashes of clear text data. The original
formalization of this concept comes from RFC-3112 and is extended by the
use of different digital agorithms.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/Crypt

