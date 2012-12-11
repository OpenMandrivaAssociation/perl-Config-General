%define	upstream_name	 Config-General
%define upstream_version 2.50

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Generic Config perl module
License:	GPL+ or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module opens a config file and parses it's contents for you. The
method new requires one parameter which needs to be a filename. The
method getall returns a hash which contains all options and it's
associated values of your config file.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
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

%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 2.500.0-2mdv2011.0
+ Revision: 680839
- mass rebuild

* Thu Dec 02 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.500.0-1mdv2011.0
+ Revision: 604709
- update to new version 2.50

* Wed Jul 14 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.490.0-1mdv2011.0
+ Revision: 553075
- update to 2.49

* Wed Apr 14 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.480.0-1mdv2010.1
+ Revision: 534937
- new version

* Fri Apr 09 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.460.0-1mdv2010.1
+ Revision: 533383
- update to 2.46

* Tue Apr 06 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.450.0-1mdv2010.1
+ Revision: 532139
- update to 2.45

* Wed Sep 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.440.0-1mdv2010.0
+ Revision: 434697
- update to new version 2.44

* Thu Jul 23 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.430.0-1mdv2010.0
+ Revision: 398853
- update to 2.43
- using %%perl_convert_version
- fixed license field

* Sun Dec 28 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.42-1mdv2009.1
+ Revision: 320426
- update to new version 2.42

* Mon Jun 23 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.40-1mdv2009.0
+ Revision: 227970
- update to new version 2.40

* Tue Jun 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.39-1mdv2009.0
+ Revision: 222652
- update to new version 2.39

* Mon Mar 03 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.38-1mdv2008.1
+ Revision: 177902
- update to new version 2.38

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Nov 27 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.37-1mdv2008.1
+ Revision: 113420
- update to new version 2.37
- update to new version 2.37

* Sun Oct 21 2007 Funda Wang <fwang@mandriva.org> 2.36-1mdv2008.1
+ Revision: 100834
- update to new version 2.36

* Tue May 01 2007 Olivier Thauvin <nanardon@mandriva.org> 2.33-1mdv2008.0
+ Revision: 19811
- 2.33


* Fri Mar 09 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.32-1mdv2007.1
+ Revision: 138794
- new version
- Import perl-Config-General

* Fri Jan 20 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.31-1mdk
- New release 2.31

* Thu Sep 22 2005 Guillaume Rousse <guillomovitch@mandriva.org> 2.30-1mdk
- New release 2.30
- fix source URL
- don't ship empty directories
- make test in %%check
- fix doc files perms
- non-redundant summary

* Fri Jun 03 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.29-1mdk
- 2.29

* Sat May 28 2005 Nicolas Lécureuil <neoclust@mandriva.org> 2.28-1mdk
- 2.28
- Make rpmbuildable

* Wed Feb 09 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.27-2mdk
- rebuild for new perl

* Sun Jun 20 2004 Per Ã˜yvind Karlsen <peroyvind@linux-mandrake.com> 2.27-1mdk
- 2.27

* Tue Mar 30 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 2.26-1mdk
- 2.26

