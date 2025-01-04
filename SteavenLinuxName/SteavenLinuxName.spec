Name:           steavenlinuxname
Version:        1.0
Release:        3%{?dist}
Summary:        SteavenSettings configuration files
License:        MIT
URL:            https://github.com/Steavenlinux/SteavenFedora

BuildArch:      noarch
BuildRequires:  git

%description
This package provides branding assets and RPM triggers for SteavenLinux.

%prep
# Clone the repository
git clone https://github.com/Steavenlinux/SteavenFedora.git
cd SteavenFedora/SteavenLinuxName

%install
# Install DNF triggers
install -Dm644 %{_builddir}/SteavenFedora/SteavenLinuxName/gdm.trigger "$RPM_BUILD_ROOT/usr/lib/dnf/plugins/gdm.trigger"
install -Dm644 %{_builddir}/SteavenFedora/SteavenLinuxName/lsb-release.trigger "$RPM_BUILD_ROOT/usr/lib/dnf/plugins/lsb-release.trigger"
install -Dm644 %{_builddir}/SteavenFedora/SteavenLinuxName/os-release.trigger "$RPM_BUILD_ROOT/usr/lib/dnf/plugins/os-release.trigger"

# Image files
install -Dm644 %{_builddir}/SteavenFedora/SteavenLinuxName/logo.png "$RPM_BUILD_ROOT/usr/share/pixmaps/logo.png"
install -Dm644 %{_builddir}/SteavenFedora/SteavenLinuxName/logo.svg "$RPM_BUILD_ROOT/usr/share/icons/logo.svg"
install -Dm644 %{_builddir}/SteavenFedora/SteavenLinuxName/steavenlinux-logo.png "$RPM_BUILD_ROOT/usr/share/pixmaps/steavenlinux-logo.png"

# Executable script
install -Dm755 %{_builddir}/SteavenFedora/SteavenLinuxName/steavenlinux-hooks-runner "$RPM_BUILD_ROOT/usr/bin/steavenlinux-hooks-runner"

%files
/usr/lib/dnf/plugins/gdm.trigger
/usr/lib/dnf/plugins/lsb-release.trigger
/usr/lib/dnf/plugins/os-release.trigger
/usr/share/pixmaps/logo.png
/usr/share/icons/logo.svg
/usr/share/pixmaps/steavenlinux-logo.png
/usr/bin/steavenlinux-hooks-runner

%changelog
%autochangelog