Name:           steavensettings
Version:        1.0
Release:        1%{?dist}
Summary:        SteavenSettings configuration files
License:        MIT
URL:            https://github.com/Steavenlinux/SteavenSettings

BuildArch:      noarch
BuildRequires:  git

Requires: zram-generator
Requires: lua-luv

Provides: zram-generator-defaults
Obsoletes: zram-generator-defaults < 2

%description
This package installs the SteavenSettings configuration files to the system.

%prep
# Clone the repository
git clone https://github.com/Steavenlinux/SteavenSettings.git
cd SteavenSettings

%install
# Install the files using the 'install' command with proper permissions and directories
install -Dm755 %{_builddir}/SteavenSettings/usr/bin/amd-gpu-run "$RPM_BUILD_ROOT/usr/bin/amd-gpu-run"
install -Dm755 %{_builddir}/SteavenSettings/usr/bin/intel-gpu-run "$RPM_BUILD_ROOT/usr/bin/intel-gpu-run"
install -Dm755 %{_builddir}/SteavenSettings/usr/bin/nvidia-gpu-run "$RPM_BUILD_ROOT/usr/bin/nvidia-gpu-run"
install -Dm755 %{_builddir}/SteavenSettings/usr/bin/nouveau-gpu-run "$RPM_BUILD_ROOT/usr/bin/nouveau-gpu-run"
install -Dm755 %{_builddir}/SteavenSettings/usr/bin/killpicom "$RPM_BUILD_ROOT/usr/bin/killpicom"
install -Dm755 %{_builddir}/SteavenSettings/usr/bin/game-run "$RPM_BUILD_ROOT/usr/bin/game-run"
install -Dm755 %{_builddir}/SteavenSettings/usr/bin/zink-run "$RPM_BUILD_ROOT/usr/bin/zink-run"

install -Dm644 %{_builddir}/SteavenSettings/etc/conf.d/libvirt-guests "$RPM_BUILD_ROOT/etc/conf.d/libvirt-guests"
install -Dm644 %{_builddir}/SteavenSettings/etc/environment.d/editor.conf "$RPM_BUILD_ROOT/usr/lib/environment.d/editor.conf"
install -Dm644 %{_builddir}/SteavenSettings/etc/grub.d/40_cpu_mitigations.cfg "$RPM_BUILD_ROOT/etc/grub.d/40_cpu_mitigations.cfg"
install -Dm644 %{_builddir}/SteavenSettings/etc/grub.d/40_distrust_cpu.cfg "$RPM_BUILD_ROOT/etc/grub.d/40_distrust_cpu.cfg"
install -Dm644 %{_builddir}/SteavenSettings/etc/grub.d/40_enable_iommu.cfg "$RPM_BUILD_ROOT/etc/grub.d/40_enable_iommu.cfg"
install -Dm644 %{_builddir}/SteavenSettings/etc/modprobe.d/amdgpu.conf "$RPM_BUILD_ROOT/usr/lib/modprobe.d/amdgpu.conf"
install -Dm644 %{_builddir}/SteavenSettings/etc/modprobe.d/kvmfr.conf "$RPM_BUILD_ROOT/usr/lib/modprobe.d/kvmfr.conf"
install -Dm644 %{_builddir}/SteavenSettings/etc/modprobe.d/nvidia.conf "$RPM_BUILD_ROOT/usr/lib/modprobe.d/nvidia.conf"
mv $RPM_BUILD_ROOT/usr/lib/modprobe.d/nvidia.conf $RPM_BUILD_ROOT/usr/lib/modprobe.d/nvidia-steavenlinux.conf
install -Dm644 %{_builddir}/SteavenSettings/etc/modprobe.d/v4l2loopback.conf "$RPM_BUILD_ROOT/usr/lib/modprobe.d/v4l2loopback.conf"
install -Dm644 %{_builddir}/SteavenSettings/etc/modules-load.d/kvmfr.conf "$RPM_BUILD_ROOT/usr/lib/modules-load.d/kvmfr.conf"
install -Dm644 %{_builddir}/SteavenSettings/etc/modules-load.d/v4l2loopback.conf "$RPM_BUILD_ROOT/usr/lib/modules-load.d/v4l2loopback.conf"
install -Dm644 %{_builddir}/SteavenSettings/etc/NetworkManager/conf.d/default-wifi-powersave-on.conf "$RPM_BUILD_ROOT/usr/lib/NetworkManager/conf.d/default-wifi-powersave-on.conf"
install -Dm644 %{_builddir}/SteavenSettings/etc/sysctl.d/80-gamecompatibility.conf "$RPM_BUILD_ROOT/usr/lib/sysctl.d/80-gamecompatibility.conf"
install -Dm644 %{_builddir}/SteavenSettings/etc/systemd/timesyncd.conf.d/timesyncd.conf "$RPM_BUILD_ROOT/usr/lib/systemd/timesyncd.conf.d/timesyncd.conf"
install -Dm644 %{_builddir}/SteavenSettings/etc/systemd/journald.conf.d/00-journal-size.conf "$RPM_BUILD_ROOT/usr/lib/systemd/journald.conf.d/00-journal-size.conf"
install -Dm644 %{_builddir}/SteavenSettings/etc/systemd/system/battery_charge_threshold.service "$RPM_BUILD_ROOT/usr/lib/systemd/system/battery_charge_threshold.service"
install -Dm644 %{_builddir}/SteavenSettings/etc/systemd/system/user@.service.d/99-reduce-time.conf "$RPM_BUILD_ROOT/usr/lib/systemd/user@.service.d/99-reduce-time.conf"
install -Dm644 %{_builddir}/SteavenSettings/etc/systemd/system.conf.d/00-timeout.conf "$RPM_BUILD_ROOT/usr/lib/systemd/system.conf.d/00-timeout.conf"
install -Dm644 %{_builddir}/SteavenSettings/etc/systemd/zram-generator.conf "$RPM_BUILD_ROOT/usr/lib/systemd/zram-generator.conf"
install -Dm644 %{_builddir}/SteavenSettings/etc/udev/rules.d/30-zram.rules "$RPM_BUILD_ROOT/usr/lib/udev/rules.d/30-zram.rules"
install -Dm644 %{_builddir}/SteavenSettings/etc/udev/rules.d/40-hpet-permissions.rules "$RPM_BUILD_ROOT/usr/lib/udev/rules.d/40-hpet-permissions.rules"
install -Dm644 %{_builddir}/SteavenSettings/etc/udev/rules.d/50-sata.rules "$RPM_BUILD_ROOT/usr/lib/udev/rules.d/50-sata.rules"
install -Dm644 %{_builddir}/SteavenSettings/etc/udev/rules.d/60-ioschedulers.rules "$RPM_BUILD_ROOT/usr/lib/udev/rules.d/60-ioschedulers.rules"
install -Dm644 %{_builddir}/SteavenSettings/etc/udev/rules.d/71-nvidia.rules "$RPM_BUILD_ROOT/usr/lib/udev/rules.d/71-nvidia.rules"
install -Dm644 %{_builddir}/SteavenSettings/etc/udev/rules.d/99-intel-cpu-watts-fix.rules "$RPM_BUILD_ROOT/usr/lib/udev/rules.d/99-intel-cpu-watts-fix.rules"
install -Dm644 %{_builddir}/SteavenSettings/etc/udev/rules.d/99-ntfs3_by_default.rules "$RPM_BUILD_ROOT/usr/lib/udev/rules.d/99-ntfs3_by_default.rules"
install -Dm644 %{_builddir}/SteavenSettings/etc/udev/rules.d/99-ntsync.rules "$RPM_BUILD_ROOT/usr/lib/udev/rules.d/99-ntsync.rules"
install -Dm644 %{_builddir}/SteavenSettings/etc/udev/rules.d/50-disable-usb-autosuspend.rules "$RPM_BUILD_ROOT/usr/lib/udev/rules.d/50-disable-usb-autosuspend.rules"
install -Dm644 %{_builddir}/SteavenSettings/etc/udisks2/mount_options.conf "$RPM_BUILD_ROOT/usr/lib/udisks2/mount_options.conf"
install -Dm644 %{_builddir}/SteavenSettings/etc/chrony.conf "$RPM_BUILD_ROOT/etc/chrony.conf"
install -Dm644 %{_builddir}/SteavenSettings/etc/polkit-1/rules.d/99-shutdown-reboot.rules "$RPM_BUILD_ROOT/etc/polkit-1/rules.d/99-shutdown-reboot.rules"
install -Dm644 %{_builddir}/SteavenSettings/etc/polkit-1/rules.d/90-flatpak.rules "$RPM_BUILD_ROOT/etc/polkit-1/rules.d/90-flatpak.rules"

%files
/usr/bin/amd-gpu-run
/usr/bin/intel-gpu-run
/usr/bin/nvidia-gpu-run
/usr/bin/nouveau-gpu-run
/usr/bin/killpicom
/usr/bin/game-run
/usr/bin/zink-run
/etc/conf.d/libvirt-guests
/usr/lib/environment.d/editor.conf
/etc/grub.d/40_cpu_mitigations.cfg
/etc/grub.d/40_distrust_cpu.cfg
/etc/grub.d/40_enable_iommu.cfg
/usr/lib/modprobe.d/amdgpu.conf
/usr/lib/modprobe.d/kvmfr.conf
/usr/lib/modprobe.d/nvidia-steavenlinux.conf
/usr/lib/modprobe.d/v4l2loopback.conf
/usr/lib/modules-load.d/kvmfr.conf
/usr/lib/modules-load.d/v4l2loopback.conf
/usr/lib/NetworkManager/conf.d/default-wifi-powersave-on.conf
/usr/lib/sysctl.d/80-gamecompatibility.conf
/usr/lib/systemd/timesyncd.conf.d/timesyncd.conf
/usr/lib/systemd/journald.conf.d/00-journal-size.conf
/usr/lib/systemd/system/battery_charge_threshold.service
/usr/lib/systemd/user@.service.d/99-reduce-time.conf
/usr/lib/systemd/system.conf.d/00-timeout.conf
/usr/lib/systemd/zram-generator.conf
/usr/lib/udev/rules.d/30-zram.rules
/usr/lib/udev/rules.d/40-hpet-permissions.rules
/usr/lib/udev/rules.d/50-sata.rules
/usr/lib/udev/rules.d/60-ioschedulers.rules
/usr/lib/udev/rules.d/71-nvidia.rules
/usr/lib/udev/rules.d/99-intel-cpu-watts-fix.rules
/usr/lib/udev/rules.d/99-ntfs3_by_default.rules
/usr/lib/udev/rules.d/99-ntsync.rules
/usr/lib/udev/rules.d/50-disable-usb-autosuspend.rules
/usr/lib/udisks2/mount_options.conf
/etc/chrony.conf
/etc/polkit-1/rules.d/99-shutdown-reboot.rules
/etc/polkit-1/rules.d/90-flatpak.rules

%changelog
%autochangelog