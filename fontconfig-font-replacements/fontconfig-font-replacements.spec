Name:    fontconfig-font-replacements
Version: 0.6
Release: 8%{?dist}
Summary: Font replacement rules for popular proprietary fonts

Group:   System Environment/Libraries
License: MIT
URL:     https://github.com/ramottamado/fedora-better-fonts
Source0: 37-repl-global-free.conf
Source1: 52-latin-free.conf
Source2: 66-aliases-wine-free.conf

BuildArch:     noarch
BuildRequires: fontpackages-devel
Requires:      adobe-source-code-pro-fonts
Requires:      adobe-source-sans-pro-fonts
Requires:      archivo-black-fonts
Requires:      catharsis-cormorant-garamond-fonts
Requires:      courier-prime-fonts
Requires:      fontpackages-filesystem
Requires:      gelasio-fonts
Requires:      google-croscore-arimo-fonts
Requires:      google-croscore-cousine-fonts
Requires:      google-croscore-tinos-fonts
Requires:      google-crosextra-caladea-fonts
Requires:      google-crosextra-carlito-fonts
Requires:      google-noto-sans-fonts
Requires:      google-noto-serif-fonts
Requires:      google-roboto-fonts
Requires:      komika-text-fonts
Requires:      lato-fonts
Requires:      liberation-narrow-fonts
Requires:      libre-baskerville-fonts
Requires:      libreoffice-opensymbol-fonts
Requires:      linux-libertine-biolinum-fonts
Requires:      mozilla-fira-mono-fonts
Requires:      mozilla-fira-sans-fonts
Requires:      open-sans-fonts
Requires:      passion-one-fonts
Requires:      sorkintype-merriweather-fonts
Requires:      sorkintype-merriweather-sans-fonts
Requires:      urw-base35-nimbus-sans-fonts

%description
Font replacement rules for popular proprietary fonts. This includes
Microsoft TrueType Core Fonts, Microsoft ClearType Font Collection and
some others.
Based on Bohoomil's fontconfig ultimate.

%prep

%build

%install
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE0} \
        %{buildroot}%{_fontconfig_templatedir}/37-repl-global-free.conf
ln -s %{_fontconfig_templatedir}/37-repl-global-free.conf \
      %{buildroot}%{_fontconfig_confdir}/37-repl-global-free.conf
install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/52-latin-free.conf
ln -s %{_fontconfig_templatedir}/52-latin-free.conf \
      %{buildroot}%{_fontconfig_confdir}/52-latin-free.conf
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/66-aliases-wine-free.conf
ln -s %{_fontconfig_templatedir}/66-aliases-wine-free.conf \
      %{buildroot}%{_fontconfig_confdir}/66-aliases-wine-free.conf

%files
%{_fontconfig_confdir}/*
%{_fontconfig_templatedir}/*

%changelog
* Sat Mar 06 2021 Tamado Sitohang <ramot@ramottamado.dev> - 0.6-8
- Change fallback fonts for sans

* Fri Mar 05 2021 Tamado Sitohang <ramot@ramottamado.dev> - 0.6-7
- Change fallback fonts for sans

* Thu Jan 14 11:17:28 WIB 2021 Tamado Sitohang <ramot@ramottamado.dev> - 0.6-6
- Add required dependencies

* Wed Jan 13 12:29:05 WIB 2021 Tamado Sitohang <ramot@ramottamado.dev> - 0.6-5
- Change fallback fonts

* Tue Jan 12 2021 Tamado Sitohang <ramot@ramottamado.dev> - 0.6-4
- Fix wrong fontconfig mapping

* Tue Jan 12 2021 Tamado Sitohang <ramot@ramottamado.dev> - 0.6-3
- Fix fontconfig wrong fonts mapping
- Delete liberation fonts mapping

* Mon Nov 02 2020 Dawid Zych <dawid.zych@yandex.com> - 0.6-2
- Add Open Sans as requirement

* Fri Oct 30 2020 Dawid Zych <dawid.zych@yandex.com> - 0.6-1
- Use Merriweather fonts from Fedora repo
- Replace EB Garamond with Cormorant Garamond

* Wed Aug 28 2019 Dawid Zych <dawid.zych@yandex.com> - 0.5-2
- Remove liberation-narrow-fonts from Fedora 30+

* Fri Apr 13 2018 Dawid Zych <dawid.zych@yandex.com> - 0.5-1
- Remove some less common Lucida variants substitutions
- Substitute Lucida Console with Fira Mono
- Substitute Lucida Sans fonts with Source Code Pro
- Substitute Consolas with Fira Mono
- Substitute Helvetica Neue with Source Code Pro
- Substitute Menlo with Cousine
- Substitute Wingdings with Open Symbol
- Substitute Comic Sans MS with Komika Text

* Thu Apr 12 2018 Dawid Zych <dawid.zych@yandex.com> - 0.4-2
- Update version

* Thu Apr 12 2018 Dawid Zych <dawid.zych@yandex.com> - 0.4-1
- Replace SymbolNeu with Open Symbol
- Fix package versioning

* Fri Apr 05 2018 Dawid Zych <dawid.zych@yandex.com> - 0.1-1
- Replace cabin with lato

* Wed Jan 11 2017 Dawid Zych <dawid.zych@yandex.com> - 0.003-1
- Update font replacement rules

* Wed Jan 11 2017 Dawid Zych <dawid.zych@yandex.com> - 0.002-1
- Set monospace font to Source Code Pro
- Add fantasy and cursive default fonts

* Thu Jan 05 2017 Dawid Zych <dawid.zych@yandex.com> - 0.001-1
- Initial packaging.
