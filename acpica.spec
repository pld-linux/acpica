#
# Conditional build:
%bcond_with	tests		# ASL tests

Summary:	ACPI Component Architecture - an assembler and disassembler for DSDT tables
Summary(pl.UTF-8):	ACPI CA - asembler i disasembler dla tablic DSDT
Name:		acpica
Version:	20260408
Release:	1
License:	GPL v2
Group:		Development/Tools
#Source0Download: https://github.com/open-acpica/acpica/releases
Source0:	https://github.com/open-acpica/acpica/releases/download/%{version}/%{name}-unix2-%{version}.tar.gz
# Source0-md5:	9f271ef5d0e8adbe09c09be83673d3c4
Source1:	https://github.com/open-acpica/acpica/releases/download/%{version}/acpitests-unix-%{version}.tar.gz
# Source1-md5:	d87dab04f10f691605ec31ecdc50584f
Source2:	iasl.1
Source3:	acpibin.1
Source4:	acpidump.1
Source5:	acpiexec.1
Source6:	acpihelp.1
Source8:	acpisrc.1
Source9:	acpixtract.1
Patch100:	%{name}-unaligned.patch
Patch102:	int-format.patch
Patch104:	template.patch
Patch105:	arm7hl.patch
Patch110:	cve-2017-13695.patch
Patch111:	str-trunc-warn.patch
Patch116:	%{name}-dangling-ptr.patch
Patch117:	%{name}-uuid-len.patch
Patch200:	%{name}-verbose.patch
URL:		https://github.com/open-acpica/acpica
BuildRequires:	bison >= 2.5.3
BuildRequires:	flex >= 2.4.1
BuildRequires:	sed >= 4.0
Provides:	iasl
Obsoletes:	iasl < 20061110
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ACPI Component Architecture - an assembler and disassembler for DSDT
tables.

%description -l pl.UTF-8
Pakiet ACPI Component Architecture zawiera asembler i disasembler do
tablic DSDT.

%prep
%setup -q -n %{name}-unix2-%{version}
tar -x --strip-components=1 -f %{SOURCE1}
%patch -P100 -p1
%patch -P102 -p1
%patch -P104 -p1
%patch -P105 -p1
%patch -P110 -p1
%patch -P111 -p1
%patch -P116 -p1
%patch -P117 -p1
%patch -P200 -p1

%build
%define	makeopts \\\
	ACPI_HOST=_LINUX \\\
	CC="%{__cc}" \\\
	OPT_CFLAGS="%{rpmcflags}" \\\
	OPT_LDFLAGS="%{rpmcflags} %{rpmldflags}"

%{__make} %{makeopts}

%if %{with tests}
cd tests

# ASL tests
./aslts.sh # relies on non-zero exit
[ $? -eq 0 ] || exit 1

# misc tests
#./run-misc-tests.sh $RPM_BUILD_ROOT%{_bindir} %{version}

# Template tests
cd templates
if [ -f diff.log ]; then
	if [ -s diff.log ]; then
		# implies errors occurred
		exit 1
	fi
fi
cd ..
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALLFLAGS="-m755"

install -d $RPM_BUILD_ROOT%{_mandir}/man1
cp -p %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} %{SOURCE8} %{SOURCE9} \
	$RPM_BUILD_ROOT%{_mandir}/man1

%{__rm} $RPM_BUILD_ROOT%{_bindir}/acpiexamples

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc changes.txt source/compiler/new_table.txt
%attr(755,root,root) %{_bindir}/acpibin
%attr(755,root,root) %{_bindir}/acpidump
%attr(755,root,root) %{_bindir}/acpiexec
%attr(755,root,root) %{_bindir}/acpihelp
%attr(755,root,root) %{_bindir}/acpisrc
%attr(755,root,root) %{_bindir}/acpixtract
%attr(755,root,root) %{_bindir}/iasl
%{_mandir}/man1/acpibin.1*
%{_mandir}/man1/acpidump.1*
%{_mandir}/man1/acpiexec.1*
%{_mandir}/man1/acpihelp.1*
%{_mandir}/man1/acpisrc.1*
%{_mandir}/man1/acpixtract.1*
%{_mandir}/man1/iasl.1*
