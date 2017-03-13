%{?scl:%scl_package nodejs-defaults}
%{!?scl:%global pkg_name %{name}}
%global enable_tests 0
%{?nodejs_find_provides_and_requires}

Name:           %{?scl_prefix}nodejs-defaults
Version:        1.0.3
Release:        1%{?dist}
Summary:        A simple one level options merge utility
License:        MIT
Url:            https://github.com/tmpvar/defaults
Source:         http://registry.npmjs.org/defaults/-/defaults-%{version}.tgz
BuildRequires:  %{?scl_prefix}nodejs-devel
BuildRequires:	%{?scl_prefix}runtime
BuildArch:      noarch
ExclusiveArch:  %{ix86} x86_64 %{arm} noarch

%if 0%{enable_tests}
BuildRequires:    %{?scl_prefix}npm(tap)
%endif

%description
Merge single level defaults over a config object.

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/defaults
cp -pr package.json index.js \
        %{buildroot}%{nodejs_sitelib}/defaults/

%nodejs_symlink_deps

%if 0%{enable_tests}
%check
%nodejs_symlink_deps --check
node test.js
%endif

%files
%doc  README.md LICENSE
%{nodejs_sitelib}/defaults

%changelog
* Wed Sep 07 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.3-1
- Updated with script, add license

* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.0-7
- Use macro in -runtime dependency
- Rebuilt with updated metapackage

* Tue Jul 21 2015 Tomas Hrcka <thrcka@redhat.com>
- Add missing build requires.

* Mon Jul 20 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.0-3
- Fix url. Resolves: RHBZ#1210384

* Mon Jan 12 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.0-2
- Initial build

