# https://github.com/chrismalek/oktasdk-go
%global goipath         github.com/chrismalek/oktasdk-go
%global commit          c38de6febf6bc5d93004d830b0a8ad6a3423a725

%gometa 

Name:           golang-github-chrismalek-oktasdk-go
Version:        0
Release:        0.4%{?dist}
Summary:        OKTA REST API Client for Go
# Detected licences
# - Expat License at 'LICENSE.txt'
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(github.com/google/go-querystring/query)

%description
%{summary}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%check
%gochecks


%files devel -f devel.file-list
%license LICENSE.txt
%doc readme.md


%changelog
* Mon Nov 12 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20181113gitc38de6f
- Bump to commit c38de6febf6bc5d93004d830b0a8ad6a3423a725
- Update to new Go packaging

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20170911gitae553c9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20170911gitae553c9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct 07 2017 Ed Marshall <esm@logic.net> - 0-0.1.20170911gitae553c9
- First package for Fedora

