Summary:	ACPI Component Architecture - an assembler and disassembler for DSDT tables
Summary(pl.UTF-8):	ACPI CA - asembler i disasembler dla tablic DSDT
Name:		acpica
Version:	20080729
Release:	1
License:	distributable (http://acpica.org/downloads/unix_source_code.php)
Group:		Development/Tools
Source0:	http://acpica.org/download/%{name}-unix-%{version}.tar.gz
# Source0-md5:	507a688b7231b4f62f296f77dcf765fa
URL:		http://acpica.org/
BuildRequires:	bison
Provides:	iasl
Obsoletes:	iasl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ACPI Component Architecture - an assembler and disassembler for DSDT
tables.

%description -l pl.UTF-8
Pakiet ACPI Component Architecture zawiera asembler i disasembler do
tablic DSDT.

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

install tools/acpisrc/acpisrc compiler/iasl $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README changes.txt
%attr(755,root,root) %{_bindir}/acpisrc
%attr(755,root,root) %{_bindir}/iasl
