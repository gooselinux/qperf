Name:           qperf
Summary:        Measure socket and RDMA performance
Version:        0.4.6
Release:        2%{?dist}
License:        GPLv2 or BSD
Group:          Networking/Diagnostic
Source: http://www.openfabrics.org/downloads/%{name}/%{name}-%{version}-0.1.gb81434e.tar.gz
Patch0: qperf-0.4.4-noxrc.patch
Url:            http://www.openfabrics.org
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  libibverbs-devel >= 1.1.2-4, librdmacm-devel >= 1.0.8-5
ExclusiveArch:  i386 x86_64 ia64 ppc ppc64
%description
Measure socket and RDMA performance.

%prep
%setup -q
%patch0 -p1 -b .noxrc

%build
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
%configure
%{__make}

%install
rm -rf ${RPM_BUILD_ROOT}
#install -D -m 0755 src/qperf $RPM_BUILD_ROOT%{_bindir}/qperf
#install -D -m 0644 src/qperf.1 $RPM_BUILD_ROOT%{_mandir}/man1/qperf.1
%{__make} DESTDIR=${RPM_BUILD_ROOT} install

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-, root, root)
%doc COPYING
%_bindir/qperf
%_mandir/man1/qperf.1*

%changelog
* Mon Jan 25 2010 Doug Ledford <dledford@redhat.com> - 0.4.6-2.el6
- Cleanups for pkgwrangler import
- Related: bz543948

* Tue Dec 22 2009 Doug Ledford <dledford@redhat.com> - 0.4.6-1.el5
- Update to latest upstream version
- Related: bz518218

* Mon Jun 22 2009 Doug Ledford <dledford@redhat.com> - 0.4.4-3.el5
- Rebuild against libibverbs that isn't missing the proper ppc wmb() macro
- Related: bz506258

* Sun Jun 21 2009 Doug Ledford <dledford@redhat.com> - 0.4.4-2.el5
- Build against non-XRC libibverbs
- Update to ofed 1.4.1 final bits
- Related: bz506097, bz506258

* Sat Apr 18 2009 Doug Ledford <dledford@redhat.com> - 0.4.4-1.el5
- Update to ofed 1.4.1-rc3 version
- Related: bz459652

* Thu Sep 18 2008 Doug Ledford <dledford@redhat.com> - 0.4.1-2
- Add a build flag to silence some warnings

* Wed Sep 17 2008 Doug Ledford <dledford@redhat.com> - 0.4.1-1
- Update to the qperf tarball found in the OFED-1.4-beta1 tarball
- Resolves: bz451483

* Tue Apr 01 2008 Doug Ledford <dledford@redhat.com> - 0.4.0-1
- Initial import to Red Hat repo management
- Related: bz428197

* Sat Oct 20 2007 - johann@georgex.org
- Initial package
