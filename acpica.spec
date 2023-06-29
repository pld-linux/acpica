#
# Conditional build:
%bcond_with	tests		# ASL tests

Summary:	ACPI Component Architecture - an assembler and disassembler for DSDT tables
Summary(pl.UTF-8):	ACPI CA - asembler i disasembler dla tablic DSDT
Name:		acpica
Version:	20220331
Release:	1
License:	GPL v2
Group:		Development/Tools
Source0:	https://acpica.org/sites/acpica/files/%{name}-unix2-%{version}.tar.gz
# Source0-md5:	5721db851442be86054d45acd1dcacef
Source1:	https://acpica.org/sites/acpica/files/acpitests-unix-%{version}.tar.gz
# Source1-md5:	9902b30fd402852a90a4ec59e471c5ff
Source2:	iasl.1
Source3:	acpibin.1
Source4:	acpidump.1
Source5:	acpiexec.1
Source6:	acpihelp.1
Source8:	acpisrc.1
Source9:	acpixtract.1
Patch0:		0001-Add-in-basic-infrastructure-for-big-endian-support.patch
Patch1:		0002-Modify-utility-functions-to-be-endian-agnostic.patch
Patch2:		0003-Always-display-table-header-content-in-human-readabl.patch
Patch3:		0004-Re-enable-support-for-big-endian-machines.patch
Patch4:		0005-Correct-an-endian-ness-problem-when-converting-ASL-t.patch
Patch5:		0006-Use-more-reliable-ACPI_COPY_NAMSEG-in-GPE-name-check.patch
Patch6:		0007-Handle-dumping-Unicode-properly-when-big-endian.patch
Patch7:		0008-Support-MADT-aka-APIC-in-a-big-endian-world.patch
Patch8:		0009-Support-ASF-tables-in-a-big-endian-world.patch
Patch9:		0010-Support-CPEP-tables-in-a-big-endian-world.patch
Patch10:	0011-Support-DBG2-table-in-a-big-endian-world.patch
Patch11:	0012-Support-DMAR-in-a-big-endian-world.patch
Patch12:	0013-Support-DRTM-in-a-big-endian-world.patch
Patch13:	0014-Support-EINJ-in-a-big-endian-world.patch
Patch14:	0015-Support-ERST-in-a-big-endian-world.patch
Patch15:	0016-Support-FADT-aka-FACP-in-a-big-endian-world.patch
Patch16:	0017-Support-most-FPDTs-in-a-big-endian-world.patch
Patch17:	0018-Support-GTDT-in-a-big-endian-world.patch
Patch18:	0019-Support-HEST-in-a-big-endian-world.patch
Patch19:	0020-Support-RSDT-RSD-PTR-in-a-big-endian-world.patch
Patch20:	0021-Support-XSDT-in-a-big-endian-world.patch
Patch21:	0022-Support-SRAT-in-a-big-endian-world.patch
Patch22:	0023-Support-SLIT-in-a-big-endian-world.patch
Patch23:	0024-Support-MSCT-in-a-big-endian-world.patch
Patch24:	0025-Support-MPST-in-a-big-endian-world.patch
Patch25:	0026-Support-NFIT-in-a-big-endian-world.patch
Patch26:	0027-Support-SDEV-in-a-big-endian-world.patch
Patch27:	0028-Support-HMAT-in-a-big-endian-world.patch
Patch28:	0029-Support-PDTT-in-a-big-endian-world.patch
Patch29:	0030-Support-PPTT-in-a-big-endian-world.patch
Patch30:	0031-Support-PCCT-in-a-big-endian-world.patch
Patch31:	0032-Support-WDAT-in-a-big-endian-world.patch
Patch32:	0033-Support-TCPA-in-a-big-endian-world.patch
Patch33:	0034-Support-STAO-in-a-big-endian-world.patch
Patch34:	0035-Support-SLIC-and-MSDM-in-a-big-endian-world.patch
Patch35:	0036-Support-MCFG-in-a-big-endian-world.patch
Patch36:	0037-Support-LPIT-in-a-big-endian-world.patch
Patch37:	0038-Support-PMTT-in-a-big-endian-world.patch
Patch38:	0039-Support-TPM2-in-a-big-endian-world.patch
Patch39:	0040-Support-S3PT-in-a-big-endian-world.patch
Patch40:	0041-Support-IORT-in-a-big-endian-world.patch
Patch41:	0042-Support-IVRS-in-a-big-endian-world.patch
Patch42:	0043-Support-DSDT-SSDT-in-a-big-endian-world.patch
# skipped in Fedora(?)
#Patch43:	0044-Initial-support-for-WPBT-in-big-endian-needs-more.patch
Patch44:	0045-CSRT-fixed-use-of-optional-ResourceInfo.patch
Patch45:	0046-Support-PHAT-in-a-big-endian-world.patch
Patch46:	0047-Support-PRMT-in-a-big-endian-world.patch
Patch47:	0048-Support-RGRT-in-a-big-endian-world.patch
Patch48:	0049-Support-SVKL-in-a-big-endian-world.patch
Patch100:	%{name}-unaligned.patch
Patch101:	%{name}-OPT_LDFLAGS.patch
Patch102:	int-format.patch
Patch104:	template.patch
Patch105:	arm7hl.patch
Patch106:       %{name}-simple-64bit.patch
Patch107:	mips-be-fix.patch
Patch108:	cve-2017-13693.patch
Patch109:	cve-2017-13694.patch
Patch110:	cve-2017-13695.patch
Patch111:	str-trunc-warn.patch
Patch112:	ptr-cast.patch
Patch113:	armv7-str-fixes.patch
Patch114:	%{name}-dbtest.patch
Patch115:	%{name}-ull-32bit.patch
Patch116:	%{name}-dangling-ptr.patch
Patch117:	%{name}-uuid-len.patch
URL:		https://acpica.org/
BuildRequires:	bison
BuildRequires:	flex
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
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
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
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
#patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch100 -p1
%patch101 -p1
%patch102 -p1
%patch104 -p1
%patch105 -p1
%patch106 -p1
%patch107 -p1
%patch108 -p1
%patch109 -p1
%patch110 -p1
%patch111 -p1
%patch112 -p1
%patch113 -p1
%patch114 -p1
%patch115 -p1
%patch116 -p1
%patch117 -p1

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
