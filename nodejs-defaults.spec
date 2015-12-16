%{?scl:%scl_package nodejs-defaults}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

Name:           %{?scl_prefix}nodejs-defaults
Version:        1.0.0
Release:        5%{?dist}
Summary:        A simple one level options merge utility
License:        MIT
Group:          Development/Languages/Other
Url:            https://github.com/tmpvar/defaults
Source:         http://registry.npmjs.org/defaults/-/defaults-%{version}.tgz
BuildRequires:  nodejs010
BuildRequires:	nodejs010-runtime
BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-build
BuildArch:      noarch
ExclusiveArch:  %{ix86} x86_64 %{arm} noarch

%description
Merge single level defaults over a config object.

%prep
%setup -q -n package
%nodejs_fixdep clone '=0.2.0'
%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/defaults
cp -pr package.json index.js \
        %{buildroot}%{nodejs_sitelib}/defaults/

%nodejs_symlink_deps

%files
%defattr(-,root,root,-)
%doc  README.md
%{nodejs_sitelib}/defaults

%changelog
* Tue Jul 21 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.0-5
- rebuilt

* Tue Jul 21 2015 Tomas Hrcka <thrcka@redhat.com>
- Add missing build requires.

* Mon Jul 20 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.0-3
- Fix url. Resolves: RHBZ#1210384

* Mon Jan 12 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.0-2
- Initial build

