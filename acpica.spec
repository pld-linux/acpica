Summary:	ACPI Component Architecture - an assembler and disassembler for DSDT tables
Summary(pl.UTF-8):	ACPI CA - asembler i disasembler dla tablic DSDT
Name:		acpica
Version:	20090521
Release:	1
License:	distributable (http://acpica.org/downloads/unix_source_code.php)
Group:		Development/Tools
Source0:	http://acpica.org/download/%{name}-unix-%{version}.tar.gz
# Source0-md5:	b2b4aa10adcb9a6faa7ce5eaaf29fcfd
URL:		http://acpica.org/
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	sed >= 4.0
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

sed 's/-O2/$(OPTCFLAGS)/g' -i tools/acpisrc/Makefile compiler/Makefile

%build
%{__make} -C tools/acpisrc \
	CC="%{__cc}" \
	OPTCFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmcflags} %{rpmldflags}"
%{__make} -j1 -C compiler \
	CC="%{__cc}" \
	OPTCFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmcflags} %{rpmldflags}"

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
