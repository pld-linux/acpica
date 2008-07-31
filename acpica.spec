Summary:	ACPI Component Architecture - an assembler and disassembler for DSDT tables
Name:		acpica
Version:	20080729
Release:	1
License:	http://www.acpica.org/downloads/unix_source_code.php
URL:		http://www.acpica.org
Source0:	http://www.acpica.org/download/%{name}-unix-%{version}.tar.gz
# Source0-md5:	507a688b7231b4f62f296f77dcf765fa
Group:		Development/Tools
BuildRequires:	bison
Provides:	iasl
Obsoletes:	iasl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ACPI Component Architecture - an assembler and disassembler for DSDT
tables

%prep
%setup -q -n %{name}-unix-%version

find . -name Makefile |xargs perl -pi -e "s,-O2,%{rpmcflags},g"

%build
%{__make} -C tools/acpisrc \
	CC="%{__cc}"
%{__make} -C compiler \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install -c compiler/iasl $RPM_BUILD_ROOT%{_bindir}

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*

%clean
rm -rf $RPM_BUILD_ROOT $RPM_BUILD_DIR/%{name}-%{version}
