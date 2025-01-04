Name:           steavenlinuxname
Version:        3
Release:        1%{?dist}
Summary:        Branding assets and triggers for SteavenLinux

License:        MIT
URL:            https://github.com/steavenlinux/steavensettings
Source0:        steavenlinux-hooks-runner
Source1:        steavenlinux-logo.png
Source2:        steavenlinux.svg

Requires:       sed
BuildArch:      noarch

%description
This package provides branding assets and RPM triggers for SteavenLinux.

Triggers:
- `lsb-release`: Updates `/etc/lsb-release` with SteavenLinux-specific details.
- `os-release`: Updates `/etc/os-release` with SteavenLinux-specific details.
- `gdm`: Updates the GNOME login screen logo.

%prep
# No preparation needed.

%build
# Nothing to build.

%install
# Install the hooks runner script
install -Dpm0755 %{SOURCE0} %{buildroot}%{_bindir}/steavenlinux-hooks-runner

# Install branding assets
install -Dpm0644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/steavenlinux-logo.png
install -Dpm0644 %{SOURCE2} %{buildroot}%{_datadir}/icons/steavenlinux.svg

# Install triggers
mkdir -p %{buildroot}/usr/lib/rpm/macros.d
cat <<EOF > %{buildroot}/usr/lib/rpm/macros.d/lsb-release.trigger
%triggerpostun -- lsb-release
/usr/bin/steavenlinux-hooks-runner lsb-release
EOF

cat <<EOF > %{buildroot}/usr/lib/rpm/macros.d/os-release.trigger
%triggerpostun -- filesystem
/usr/bin/steavenlinux-hooks-runner os-release
EOF

cat <<EOF > %{buildroot}/usr/lib/rpm/macros.d/gdm.trigger
%triggerpostun -- gdm libgdm
/usr/bin/steavenlinux-hooks-runner gdm
EOF

%files
%license LICENSE
%{_bindir}/steavenlinux-hooks-runner
%{_datadir}/pixmaps/steavenlinux-logo.png
%{_datadir}/icons/steavenlinux.svg
%{_sysconfdir}/rpm/macros.d/*.trigger

%changelog
%autochangelog