#
# Spec file for package cryfs
#
%define _prefix  /usr/local
Name:           cryfs
Version:        0.10.2
Release:        1%{?dist}
Summary:        cryfs encryption
License:        GPL-2.0+
Group:          Security
Source:         %{name}-%{version}-src.tar.gz
## get real source for the git Source0:         https://github.com/cryfs/cryfs/releases/download/%{version}/cryfs-%{version}.tar.gz
URL:            https://github.com/cryfs/cryfs
#=================================
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: python
BuildRequires: boost-devel
BuildRequires: boost-static
BuildRequires: cryptopp-devel
BuildRequires: curl-devel
BuildRequires: fuse-devel
BuildRequires: openssl-devel
#=================================

%description
CryFS encrypts your files, so you can safely store them anywhere.
It works well together with cloud services like Dropbox,
iCloud, OneDrive and others.

%global debug_package %{nil}

%prep
%setup -q

%build
mkdir cmake && cd cmake
cmake .. -DCMAKE_BUILD_TYPE=Release -DBUILD_TESTING=off
%{__make}
cd ..

%install
rm -rf %{buildroot}
%make_install -C cmake

%clean
rm -rf %{buildroot}

%files
%defattr(0755,root,root)
%{_bindir}/cryfs*
%{_mandir}/man1/cryfs.1.gz

%changelog
* Sun Aug 04 2019 mnovotny 0.10.2-1
- update to 0.10.2

* Wed Apr 10 2019 mnovotny 0.10.1-1
- update to 0.10.1

* Tue Feb 12 2019 mnovotny 0.10.0-1
- update to 0.10.0

* Wed Jan 30 2019 mnovotny 0.9.10-0.1
- update to 0.9.10

* Tue Nov 6 2018 mnovotny 0.9.9-0.2
- rebuild for Fedora 29

* Thu Feb 15 2018 mnovotny 0.9.9-0.1
- update to 0.9.9

* Fri Sep 08 2017 mnovotny 0.9.7-0.1
- update to 0.9.7

* Sun Jul 03 2016 mnovotny 0.9.5-0.1
- create

