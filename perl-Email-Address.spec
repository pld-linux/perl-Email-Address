# ToDo:
# - pl description
#
# Conditional build:
%bcond_without  tests           # do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Email
%define	pnam	Address
Summary:	Email::Address - RFC 2822 Address Parsing and Creation
Summary(pl):	Email::Address - Parsowanie i tworzenie adres�w zgodnych z RFC 2822
Name:		perl-Email-Address
Version:	1.2
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b356b65411d4f52e02b8b0c9c0942e58
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class implements a complete RFC 2822 parser that locates email
addresses in strings and returns a list of C<Email::Address> objects
found. Alternatley you may construct objects manually. The goal
of this software is to be correct, very very fast, and API compatible
with the MailTools version. Did I mention fast?

#%description -l pl

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
