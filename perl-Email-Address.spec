#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Email
%define	pnam	Address
Summary:	Email::Address - RFC 2822 Address Parsing and Creation
Summary(pl):	Email::Address - Parsowanie i tworzenie adresów zgodnych z RFC 2822
Name:		perl-Email-Address
Version:	1.80
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b57726d9915a502bc6b52966217a453e
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class implements a complete RFC 2822 parser that locates email
addresses in strings and returns a list of Email::Address objects
found. Alternatley you may construct objects manually. The goal of
this software is to be correct, very very fast, and API compatible
with the MailTools version. Did I mention fast?

%description -l pl
Ta klasa implementuje zgodny z RFC 2822 parser który lokalizuje adresy
email w ci±gach znaków i zwraca listê obiektów Email::Address. Mo¿liwe
jest tak¿e tworzenie takich obiektów rêczenie. Oprogramowanie to ma
byæ poprawne, bardzo bardzo szybkie, i z API zgodnym z MailTools. 

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Email/*.pm
%{_mandir}/man3/*
