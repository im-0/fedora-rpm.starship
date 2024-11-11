%global source_date_epoch_from_changelog 0
%global __brp_mangle_shebangs_exclude_from ^/usr/src/.*$

Name:           starship
Version:        1.21.1
Release:        1%{?dist}
Summary:        The minimal, blazing-fast, and infinitely customizable prompt for any shell!

License:        ISC
URL:            https://github.com/starship/starship
Source0:        https://github.com/starship/starship/archive/v%{version}/%{name}-%{version}.tar.gz

# Contains starship-$VERSION/vendor/*.
#     $ cargo vendor
#     $ mkdir starship-X.Y.Z
#     $ mv vendor starship-X.Y.Z/
#     $ tar vcJf starship-X.Y.Z.cargo-vendor.tar.xz starship-X.Y.Z
Source1:    %{name}-%{version}.cargo-vendor.tar.xz
Source2:    config.toml

BuildRequires:  cargo-rpm-macros
BuildRequires:  gcc
BuildRequires:  g++


%description
The minimal, blazing-fast, and infinitely customizable prompt for any shell!


%prep
%setup -q -D -T -b0 -n %{name}-%{version}
%setup -q -D -T -b1 -n %{name}-%{version}

mkdir .cargo
cp %{SOURCE2} .cargo/config.toml


%build
# Check https://pagure.io/fedora-rust/rust2rpm/blob/main/f/data/macros.rust for
# rust-specific variables.
export RUSTC_BOOTSTRAP=1

cargo build %{__cargo_common_opts} --release --frozen


%install
install -Dm755 target/release/starship %{buildroot}%{_bindir}/starship


%files
%{_bindir}/starship


%changelog
