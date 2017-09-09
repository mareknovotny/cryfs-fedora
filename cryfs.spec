#
# Spec file for package cryfs
#

Name:           cryfs
Version:        0.9.7
Release:        1%{?dist}
Summary:        cryfs encryption
License:        GPL-2.0+
Group:          Security
Source:         %{name}-%{version}-src.tar.gz
URL:            https://github.com/cryfs/cryfs
#=================================
BuildRequires: cmake
BuildRequires: %{_lib}boost-devel
BuildRequires: %{_lib}boost-static-devel
BuildRequires: %{_lib}cryptopp6-devel
BuildRequires: %{_lib}curl-devel
BuildRequires: %{_lib}fuse-devel
BuildRequires: %{_lib}openssl-devel
#=================================

%description
CryFS encrypts your files, so you can safely store them anywhere.
It works well together with cloud services like Dropbox,
iCloud, OneDrive and others.


%prep
%setup -q

%build
mkdir cmake-build
cd cmake-build
cmake ..
%make
cd ..

%install
rm -rf %buildroot
%make_install -C cmake-build

%clean
rm -rf %{buildroot}

%files
%defattr(0755,root,root)
%{_bindir}/cryfs*

%changelog
* Fri Sep 08 2017 mnovotny 0.9.7-0.1
- update to 0.9.7

* Sun Jul 03 2016 bb <bb> 0.9.5-0.5442662pclos2016
- create

