%define tarball_version 1_4_6

Name:		mp3gain
Version:	1.4.6
Release:	5%{?dist}
Summary:	Lossless MP3 volume adjustment tool

Group:		Applications/Multimedia
License:	LGPL
URL:		http://mp3gain.sourceforge.net
Source0:	http://osdn.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{tarball_version}-src.zip
Source1:	%{name}.1.gz
Source2:	README.method
Patch0:		%{name}-tempfile-default.patch
Patch1:		%{name}-exit.patch
Patch2:		%{name}-cflags.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
	

%description
MP3Gain analyzes and adjusts mp3 files so that they have the same
volume. It does not just do peak normalization, as many normalizers
do. Instead, it does some statistical analysis to determine how loud
the file actually sounds to the human ear. Also, the changes MP3Gain
makes are completely lossless. There is no quality lost in the change
because the program adjusts the mp3 file directly, without decoding
and re-encoding.


%prep
%setup -q -c %{name}-%{tarball_version}
%patch0 -p1 -b .tempfile
%patch1 -p1 -b .exit
%patch2 -p1 -b .cflags
install -p -m 644 %{SOURCE2} .
%{__sed} -i 's/\r//' lgpl.txt


%build
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
install -Dp -m 755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -Dp -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1.gz


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc lgpl.txt README.method
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz


%changelog
* Mon Aug 04 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 1.4.6-5
- rebuild

* Tue Nov 28 2006 Brian Pepple <bpepple@fedoraproject.org> - 1.4.6-4
- Bump.

* Sun Nov 26 2006 Brian Pepple <bpepple@fedoraproject.org> - 1.4.6-3
- D'Oh! Add HAVE_MEMCPY back to cflag patch.

* Sun Nov 26 2006 Brian Pepple <bpepple@fedoraproject.org> - 1.4.6-2
- Update cflags patch to use RPM_OPT_FLAGS.

* Mon Nov 20 2006 Brian Pepple <bpepple@fedoraproject.org> - 1.4.6-1
- Initial Livna spec.

