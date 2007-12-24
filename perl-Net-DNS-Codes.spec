#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	DNS-Codes
Summary:	Net::DNS::Codes - collection of C library DNS codes
Summary(pl.UTF-8):	Net::DNS::Codes - kolekcja kodów DNS
Name:		perl-Net-DNS-Codes
Version:	0.09
Release:	1
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e1c5c38d557b60fefd0965569b9a08d9
URL:		http://search.cpan.org/dist/Net-DNS-Codes/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::DNS::Codes provides forward and reverse lookup for most
common C library DNS codes as well as all the codes for the DNS 
HEADER field.

%description -l pl.UTF-8
Net::DNS::Codes dostarcza wyszukiwanie zwykłe i odwrotne dla
większości popularnych kodów DNS biblioteki C, a także kody dla pola
HEADER DNS.

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
%{perl_vendorlib}/Net/DNS/Codes.pm
%{_mandir}/man3/*
