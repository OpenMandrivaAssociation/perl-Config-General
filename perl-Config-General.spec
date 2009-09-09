%define	upstream_name	 Config-General
%define upstream_version 2.44

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	Generic Config perl module
License:	GPL+ or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
BuildArch:	    noarch
BuildRoot:	    %{_tmppath}/%{name}-%{version}-%{release}

%description
This module opens a config file and parses it's contents for you. The
method new requires one parameter which needs to be a filename. The
method getall returns a hash which contains all options and it's
associated values of your config file.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
chmod 644 Changelog README

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changelog README
%{perl_vendorlib}/Config
%{_mandir}/man3/*


