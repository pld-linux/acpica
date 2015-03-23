#
# Conditional build:
%bcond_with	tests		# build without tests

Summary:	ACPI Component Architecture - an assembler and disassembler for DSDT tables
Summary(pl.UTF-8):	ACPI CA - asembler i disasembler dla tablic DSDT
Name:		acpica
Version:	20141107
Release:	1
License:	GPL v2
Group:		Development/Tools
Source0:	https://acpica.org/sites/acpica/files/%{name}-unix2-%{version}.tar.gz
# Source0-md5:	af9f1e67023fa85f9d6abf28b5345abd
Source1:	https://acpica.org/sites/acpica/files/acpitests-unix-%{version}.tar.gz
# Source1-md5:	64f6360eb986524254849930ff0a711f
Patch0:		debian-big_endian.patch
Patch1:		debian-unaligned.patch
Patch2:		name-miscompare.patch
Patch3:		aapits-linux.patch
Patch4:		asllookup-miscompare.patch
Patch5:		aapits-makefile.patch
Patch6:		re-enable-big-endian.patch
Patch7:		OPT_LDFLAGS.patch
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

%build
%define	makeopts \\\
	HOST=_LINUX \\\
	CC="%{__cc}" \\\
	OPT_CFLAGS="%{rpmcflags}" \\\
	OPT_LDFLAGS="%{rpmcflags} %{rpmldflags}"

%{__make} %{makeopts}

%if %{with tests}
%{__make} %{makeopts} -C tests/aapits
%{__make} %{makeopts} -C tests/aapits/asl \
	ASL=$(pwd)/generate/unix/bin/iasl
%{__make} %{makeopts} -C tests/templates

cd tests

# ASL tests
./aslts.sh # relies on non-zero exit
[ $? -eq 0 ] || exit 1

# API tests
cd aapits/bin
./aapitsrun
[ $? -eq 0 ] || exit 1
cd ../..

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
