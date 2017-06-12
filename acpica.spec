#
# Conditional build:
%bcond_with	tests		# ASL tests

Summary:	ACPI Component Architecture - an assembler and disassembler for DSDT tables
Summary(pl.UTF-8):	ACPI CA - asembler i disasembler dla tablic DSDT
Name:		acpica
Version:	20170303
Release:	1
License:	GPL v2
Group:		Development/Tools
Source0:	https://acpica.org/sites/acpica/files/%{name}-unix-%{version}.tar.gz
# Source0-md5:	704c7d0ba7ee826ea489995c4837ebd2
Source1:	https://acpica.org/sites/acpica/files/acpitests-unix-%{version}.tar.gz
# Source1-md5:	2dc88f6782bb3be3c66bd1a052ee7972
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
Patch2:		name-miscompare.patch
Patch3:		asllookup-miscompare.patch
Patch4:		re-enable-big-endian.patch
Patch5:		OPT_LDFLAGS.patch
Patch6:		int-format.patch
Patch8:		asllookup-ppc64.patch
Patch9:		template.patch
Patch10:	free.patch
Patch11:	update-big-endian.patch
Patch12:	ppc64le.patch
Patch13:	arm7hl.patch
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
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1

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
