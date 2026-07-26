%define	upstream_name	 Config-General
Name:		perl-%{upstream_name}
Version:	2.67
Release:	2

Summary:	Generic Config perl module


License:	GPL+ or Artistic
Group:		Development/Perl
Url:        https://github.com/TLINDEN/Config-General
Source0:	https://cpan.metacpan.org/authors/id/T/TL/TLINDEN/Config-General-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module opens a config file and parses it's contents for you. The
method new requires one parameter which needs to be a filename. The
method getall returns a hash which contains all options and it's
associated values of your config file.

%prep
%setup -q -n %{upstream_name}-%{version}
chmod 644 Changelog README

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changelog README
%{perl_vendorlib}/Config
%{_mandir}/man3/*



