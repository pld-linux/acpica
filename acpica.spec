#
# Conditional build:
%bcond_with	tests		# ASL tests

Summary:	ACPI Component Architecture - an assembler and disassembler for DSDT tables
Summary(pl.UTF-8):	ACPI CA - asembler i disasembler dla tablic DSDT
Name:		acpica
Version:	20181031
Release:	1
License:	GPL v2
Group:		Development/Tools
Source0:	https://acpica.org/sites/acpica/files/%{name}-unix-%{version}.tar.gz
# Source0-md5:	cea3f668b536ec56ae878a3239035f26
Source1:	https://acpica.org/sites/acpica/files/acpitests-unix-%{version}.tar.gz
# Source1-md5:	745791d46298c30cc7ee851ae045dbb0
Source2:	iasl.1
Source3:	acpibin.1
Source4:	acpidump.1
Source5:	acpiexec.1
Source6:	acpihelp.1
Source7:	acpinames.1
Source8:	acpisrc.1
Source9:	acpixtract.1
Patch0:		debian-big_endian.patch
Patch1:		debian-unaligned.patch
Patch6:		int-format.patch
Patch9:		template.patch
Patch10:	free.patch
Patch12:	ppc64le.patch
Patch13:	arm7hl.patch
Patch14:	big-endian-v2.patch
Patch15:	be-tpm2.patch
Patch16:	mips-be-fix.patch
Patch17:	cve-2017-13693.patch
Patch18:	cve-2017-13694.patch
Patch19:	cve-2017-13695.patch
Patch20:	str-trunc-warn.patch
Patch21:	ptr-cast.patch
Patch22:	aslcodegen.patch
URL:		https://acpica.org/
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
%setup -q -n %{name}-unix-%{version}
tar -x --strip-components=1 -f %{SOURCE1}
%patch0 -p1
%patch1 -p1
%patch6 -p1
%patch9 -p1
%patch10 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1

%build
%define	makeopts \\\
	HOST=_LINUX \\\
	CC="%{__cc}" \\\
	OPT_CFLAGS="%{rpmcflags}" \\\
	OPT_LDFLAGS="%{rpmcflags} %{rpmldflags}"

%{__make} %{makeopts}

%if %{with tests}
%{__make} %{makeopts} -C tests/templates

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
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_mandir}/man1
cp -p %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} %{SOURCE7} %{SOURCE8} %{SOURCE9} \
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
%attr(755,root,root) %{_bindir}/acpinames
%attr(755,root,root) %{_bindir}/acpisrc
%attr(755,root,root) %{_bindir}/acpixtract
%attr(755,root,root) %{_bindir}/iasl
%{_mandir}/man1/acpibin.1*
%{_mandir}/man1/acpidump.1*
%{_mandir}/man1/acpiexec.1*
%{_mandir}/man1/acpihelp.1*
%{_mandir}/man1/acpinames.1*
%{_mandir}/man1/acpisrc.1*
%{_mandir}/man1/acpixtract.1*
%{_mandir}/man1/iasl.1*
