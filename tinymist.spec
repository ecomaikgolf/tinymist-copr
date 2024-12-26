Name:       tinymist
Version:    0.12.14
Release:    %autorelease
Summary:    Tinymist is an integrated language service for Typst. 

License:    Apache-2.0
URL:        https://github.com/Myriad-Dreamin/tinymist
Source0:    %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: rust-packaging
BuildRequires: nodejs
BuildRequires: yarnpkg


%description
Tinymist is an integrated language service for Typst


%prep
%autosetup


%build
yarn && yarn build:preview
cargo build --release --all-features --locked


%install
install -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 target/release/%{name} %{buildroot}%{_bindir}/%{name}
install -m 0755 target/release/typlite %{buildroot}%{_bindir}/typlite


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_bindir}/typlite


%changelog
%autochangelog
