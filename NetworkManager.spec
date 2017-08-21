#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : NetworkManager
Version  : 1.8.0
Release  : 21
URL      : https://download.gnome.org/sources/NetworkManager/1.8/NetworkManager-1.8.0.tar.xz
Source0  : https://download.gnome.org/sources/NetworkManager/1.8/NetworkManager-1.8.0.tar.xz
Summary  : System for maintaining active network connection
Group    : Development/Tools
License  : GPL-2.0
Requires: NetworkManager-bin
Requires: NetworkManager-config
Requires: NetworkManager-autostart
Requires: NetworkManager-lib
Requires: NetworkManager-data
Requires: NetworkManager-doc
Requires: NetworkManager-locales
Requires: dhcp
Requires: network-manager-applet
Requires: wpa_supplicant
BuildRequires : dbus-dev
BuildRequires : dbus-dev32
BuildRequires : dbus-glib-dev
BuildRequires : dbus-glib-dev32
BuildRequires : dhcp
BuildRequires : docbook-xml
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : gettext
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : intltool
BuildRequires : iptables
BuildRequires : iptables-dev
BuildRequires : iptables-dev32
BuildRequires : libndp-dev
BuildRequires : libndp-dev32
BuildRequires : libnl-dev
BuildRequires : libnl-dev32
BuildRequires : libsoup-dev
BuildRequires : libsoup-dev32
BuildRequires : libxslt-bin
BuildRequires : ncurses-dev
BuildRequires : ncurses-dev32
BuildRequires : nss-dev
BuildRequires : nss-lib32
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(32dbus-1)
BuildRequires : pkgconfig(32dbus-glib-1)
BuildRequires : pkgconfig(32gio-unix-2.0)
BuildRequires : pkgconfig(32gmodule-2.0)
BuildRequires : pkgconfig(32libcurl)
BuildRequires : pkgconfig(32libnl-3.0)
BuildRequires : pkgconfig(32libsystemd)
BuildRequires : pkgconfig(32libudev)
BuildRequires : pkgconfig(32systemd)
BuildRequires : pkgconfig(32uuid)
BuildRequires : pkgconfig(bluez)
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(dbus-glib-1)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(gmodule-2.0)
BuildRequires : pkgconfig(gnutls)
BuildRequires : pkgconfig(libcurl)
BuildRequires : pkgconfig(libnl-3.0)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(nss)
BuildRequires : pkgconfig(polkit-agent-1)
BuildRequires : pkgconfig(systemd)
BuildRequires : pkgconfig(uuid)
BuildRequires : pygobject
BuildRequires : readline-dev
Patch1: spoof-online.patch
Patch2: 0001-platform-Explicitly-unmanage-all-ethernet-devices.patch
Patch3: 0002-settings-Ensure-the-keyfile-storage-directory-actual.patch

%description
******************
2008-12-11: NetworkManager core daemon has moved to git.freedesktop.org!

%package autostart
Summary: autostart components for the NetworkManager package.
Group: Default

%description autostart
autostart components for the NetworkManager package.


%package bin
Summary: bin components for the NetworkManager package.
Group: Binaries
Requires: NetworkManager-data
Requires: NetworkManager-config

%description bin
bin components for the NetworkManager package.


%package config
Summary: config components for the NetworkManager package.
Group: Default

%description config
config components for the NetworkManager package.


%package data
Summary: data components for the NetworkManager package.
Group: Data

%description data
data components for the NetworkManager package.


%package dev
Summary: dev components for the NetworkManager package.
Group: Development
Requires: NetworkManager-lib
Requires: NetworkManager-bin
Requires: NetworkManager-data
Provides: NetworkManager-devel

%description dev
dev components for the NetworkManager package.


%package dev32
Summary: dev32 components for the NetworkManager package.
Group: Default
Requires: NetworkManager-lib32
Requires: NetworkManager-bin
Requires: NetworkManager-data
Requires: NetworkManager-dev

%description dev32
dev32 components for the NetworkManager package.


%package doc
Summary: doc components for the NetworkManager package.
Group: Documentation

%description doc
doc components for the NetworkManager package.


%package lib
Summary: lib components for the NetworkManager package.
Group: Libraries
Requires: NetworkManager-data
Requires: NetworkManager-config

%description lib
lib components for the NetworkManager package.


%package lib32
Summary: lib32 components for the NetworkManager package.
Group: Default
Requires: NetworkManager-data
Requires: NetworkManager-config

%description lib32
lib32 components for the NetworkManager package.


%package locales
Summary: locales components for the NetworkManager package.
Group: Default

%description locales
locales components for the NetworkManager package.


%prep
%setup -q -n NetworkManager-1.8.0
%patch1 -p1
%patch2 -p1
%patch3 -p1
pushd ..
cp -a NetworkManager-1.8.0 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1503331391
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
%configure --disable-static --disable-ppp \
--disable-teamdctl \
--with-nmcli=yes \
--disable-json-validation \
--with-config-plugins-default=keyfile \
--with-dist-version="Clear Linux Software for Intel Architecture" \
--with-dhclient=/usr/bin/dhclient \
--with-session-tracking=systemd \
--with-suspend-resume=systemd \
--with-systemd-logind=yes \
--with-systemd-journal=yes \
--enable-modify-system \
--disable-ppp \
--enable-polkit-agent \
--enable-polkit=yes \
--with-kernel-firmware-dir=/usr/lib/firmware \
--with-dbus-sys-dir=/usr/share/dbus-1/system.d \
--enable-wifi \
--enable-bluez5-dun \
--with-system-ca-path=/usr/share/ca-certs \
--with-iptables=/usr/bin/iptables \
PYTHON=/usr/bin/python3
make V=1  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static --disable-ppp \
--disable-teamdctl \
--with-nmcli=yes \
--disable-json-validation \
--with-config-plugins-default=keyfile \
--with-dist-version="Clear Linux Software for Intel Architecture" \
--with-dhclient=/usr/bin/dhclient \
--with-session-tracking=systemd \
--with-suspend-resume=systemd \
--with-systemd-logind=yes \
--with-systemd-journal=yes \
--enable-modify-system \
--disable-ppp \
--enable-polkit-agent \
--enable-polkit=yes \
--with-kernel-firmware-dir=/usr/lib/firmware \
--with-dbus-sys-dir=/usr/share/dbus-1/system.d \
--enable-wifi \
--enable-bluez5-dun \
--with-system-ca-path=/usr/share/ca-certs \
--with-iptables=/usr/bin/iptables \
PYTHON=/usr/bin/python3 --disable-ppp \
--disable-teamdctl \
--with-nmcli=no \
--disable-json-validation \
--with-config-plugins-default=keyfile \
--with-dist-version="Clear Linux Software for Intel Architecture" \
--with-dhclient=/usr/bin/dhclient \
--with-session-tracking=systemd \
--with-suspend-resume=systemd \
--with-systemd-logind=yes \
--with-systemd-journal=yes \
--enable-modify-system \
--disable-ppp \
--disable-polkit-agent \
--enable-polkit=disabled \
--with-kernel-firmware-dir=/usr/lib/firmware \
--with-dbus-sys-dir=/usr/share/dbus-1/system.d \
--enable-wifi \
--with-system-ca-path=/usr/share/ca-certs \
--with-iptables=/usr/bin/iptables \
PYTHON=/usr/bin/python3  --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make V=1  %{?_smp_mflags}
popd
%install
export SOURCE_DATE_EPOCH=1503331391
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install
%find_lang NetworkManager
## make_install_append content
pushd %{buildroot}/usr/lib/systemd/system
ln -s NetworkManager.service dbus-org.freedesktop.NetworkManager.service
ln -s NetworkManager-dispatcher.service dbus-org.freedesktop.nm-dispatcher.service
popd
## make_install_append end

%files
%defattr(-,root,root,-)
/usr/lib32/girepository-1.0/NM-1.0.typelib
/usr/lib32/girepository-1.0/NMClient-1.0.typelib
/usr/lib32/girepository-1.0/NetworkManager-1.0.typelib

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/network-online.target.wants/NetworkManager-wait-online.service

%files bin
%defattr(-,root,root,-)
/usr/bin/NetworkManager
/usr/bin/nm-online
/usr/bin/nmcli
/usr/libexec/nm-dhcp-helper
/usr/libexec/nm-dispatcher
/usr/libexec/nm-iface-helper

%files config
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/network-online.target.wants/NetworkManager-wait-online.service
/usr/lib/systemd/system/NetworkManager-dispatcher.service
/usr/lib/systemd/system/NetworkManager-wait-online.service
/usr/lib/systemd/system/NetworkManager.service
/usr/lib/systemd/system/dbus-org.freedesktop.NetworkManager.service
/usr/lib/systemd/system/dbus-org.freedesktop.nm-dispatcher.service
/usr/lib/udev/rules.d/84-nm-drivers.rules
/usr/lib/udev/rules.d/85-nm-unmanaged.rules

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/NM-1.0.typelib
/usr/lib64/girepository-1.0/NMClient-1.0.typelib
/usr/lib64/girepository-1.0/NetworkManager-1.0.typelib
/usr/share/bash-completion/completions/nmcli
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.AccessPoint.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.AgentManager.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Checkpoint.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Connection.Active.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.DHCP4Config.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.DHCP6Config.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Adsl.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Bluetooth.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Bond.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Bridge.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Dummy.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Generic.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.IPTunnel.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Infiniband.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Macsec.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Macvlan.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Modem.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.OlpcMesh.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Statistics.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Team.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Tun.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Veth.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Vlan.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Vxlan.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.WiMax.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Wired.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Wireless.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.DnsManager.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.IP4Config.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.IP6Config.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.PPP.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.SecretAgent.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Settings.Connection.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Settings.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.VPN.Connection.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.VPN.Plugin.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.WiMax.Nsp.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.xml
/usr/share/dbus-1/system-services/org.freedesktop.NetworkManager.service
/usr/share/dbus-1/system-services/org.freedesktop.nm_dispatcher.service
/usr/share/dbus-1/system.d/nm-dispatcher.conf
/usr/share/dbus-1/system.d/org.freedesktop.NetworkManager.conf
/usr/share/gir-1.0/*.gir
/usr/share/polkit-1/actions/org.freedesktop.NetworkManager.policy

%files dev
%defattr(-,root,root,-)
/usr/include/NetworkManager/NetworkManager.h
/usr/include/NetworkManager/NetworkManagerVPN.h
/usr/include/NetworkManager/nm-connection.h
/usr/include/NetworkManager/nm-setting-8021x.h
/usr/include/NetworkManager/nm-setting-adsl.h
/usr/include/NetworkManager/nm-setting-bluetooth.h
/usr/include/NetworkManager/nm-setting-bond.h
/usr/include/NetworkManager/nm-setting-bridge-port.h
/usr/include/NetworkManager/nm-setting-bridge.h
/usr/include/NetworkManager/nm-setting-cdma.h
/usr/include/NetworkManager/nm-setting-connection.h
/usr/include/NetworkManager/nm-setting-dcb.h
/usr/include/NetworkManager/nm-setting-generic.h
/usr/include/NetworkManager/nm-setting-gsm.h
/usr/include/NetworkManager/nm-setting-infiniband.h
/usr/include/NetworkManager/nm-setting-ip4-config.h
/usr/include/NetworkManager/nm-setting-ip6-config.h
/usr/include/NetworkManager/nm-setting-olpc-mesh.h
/usr/include/NetworkManager/nm-setting-ppp.h
/usr/include/NetworkManager/nm-setting-pppoe.h
/usr/include/NetworkManager/nm-setting-serial.h
/usr/include/NetworkManager/nm-setting-team-port.h
/usr/include/NetworkManager/nm-setting-team.h
/usr/include/NetworkManager/nm-setting-vlan.h
/usr/include/NetworkManager/nm-setting-vpn.h
/usr/include/NetworkManager/nm-setting-wimax.h
/usr/include/NetworkManager/nm-setting-wired.h
/usr/include/NetworkManager/nm-setting-wireless-security.h
/usr/include/NetworkManager/nm-setting-wireless.h
/usr/include/NetworkManager/nm-setting.h
/usr/include/NetworkManager/nm-utils-enum-types.h
/usr/include/NetworkManager/nm-utils.h
/usr/include/NetworkManager/nm-version-macros.h
/usr/include/NetworkManager/nm-version.h
/usr/include/libnm-glib/libnm_glib.h
/usr/include/libnm-glib/nm-access-point.h
/usr/include/libnm-glib/nm-active-connection.h
/usr/include/libnm-glib/nm-client.h
/usr/include/libnm-glib/nm-device-adsl.h
/usr/include/libnm-glib/nm-device-bond.h
/usr/include/libnm-glib/nm-device-bridge.h
/usr/include/libnm-glib/nm-device-bt.h
/usr/include/libnm-glib/nm-device-ethernet.h
/usr/include/libnm-glib/nm-device-generic.h
/usr/include/libnm-glib/nm-device-infiniband.h
/usr/include/libnm-glib/nm-device-modem.h
/usr/include/libnm-glib/nm-device-olpc-mesh.h
/usr/include/libnm-glib/nm-device-team.h
/usr/include/libnm-glib/nm-device-vlan.h
/usr/include/libnm-glib/nm-device-wifi.h
/usr/include/libnm-glib/nm-device-wimax.h
/usr/include/libnm-glib/nm-device.h
/usr/include/libnm-glib/nm-dhcp4-config.h
/usr/include/libnm-glib/nm-dhcp6-config.h
/usr/include/libnm-glib/nm-glib-enum-types.h
/usr/include/libnm-glib/nm-ip4-config.h
/usr/include/libnm-glib/nm-ip6-config.h
/usr/include/libnm-glib/nm-object.h
/usr/include/libnm-glib/nm-remote-connection.h
/usr/include/libnm-glib/nm-remote-settings.h
/usr/include/libnm-glib/nm-secret-agent.h
/usr/include/libnm-glib/nm-types.h
/usr/include/libnm-glib/nm-vpn-connection.h
/usr/include/libnm-glib/nm-vpn-enum-types.h
/usr/include/libnm-glib/nm-vpn-plugin-ui-interface.h
/usr/include/libnm-glib/nm-vpn-plugin-utils.h
/usr/include/libnm-glib/nm-vpn-plugin.h
/usr/include/libnm-glib/nm-wimax-nsp.h
/usr/include/libnm/NetworkManager.h
/usr/include/libnm/nm-access-point.h
/usr/include/libnm/nm-active-connection.h
/usr/include/libnm/nm-client.h
/usr/include/libnm/nm-connection.h
/usr/include/libnm/nm-core-enum-types.h
/usr/include/libnm/nm-core-types.h
/usr/include/libnm/nm-dbus-interface.h
/usr/include/libnm/nm-device-adsl.h
/usr/include/libnm/nm-device-bond.h
/usr/include/libnm/nm-device-bridge.h
/usr/include/libnm/nm-device-bt.h
/usr/include/libnm/nm-device-dummy.h
/usr/include/libnm/nm-device-ethernet.h
/usr/include/libnm/nm-device-generic.h
/usr/include/libnm/nm-device-infiniband.h
/usr/include/libnm/nm-device-ip-tunnel.h
/usr/include/libnm/nm-device-macsec.h
/usr/include/libnm/nm-device-macvlan.h
/usr/include/libnm/nm-device-modem.h
/usr/include/libnm/nm-device-olpc-mesh.h
/usr/include/libnm/nm-device-team.h
/usr/include/libnm/nm-device-tun.h
/usr/include/libnm/nm-device-vlan.h
/usr/include/libnm/nm-device-vxlan.h
/usr/include/libnm/nm-device-wifi.h
/usr/include/libnm/nm-device-wimax.h
/usr/include/libnm/nm-device.h
/usr/include/libnm/nm-dhcp-config.h
/usr/include/libnm/nm-enum-types.h
/usr/include/libnm/nm-errors.h
/usr/include/libnm/nm-ip-config.h
/usr/include/libnm/nm-object.h
/usr/include/libnm/nm-remote-connection.h
/usr/include/libnm/nm-secret-agent-old.h
/usr/include/libnm/nm-setting-8021x.h
/usr/include/libnm/nm-setting-adsl.h
/usr/include/libnm/nm-setting-bluetooth.h
/usr/include/libnm/nm-setting-bond.h
/usr/include/libnm/nm-setting-bridge-port.h
/usr/include/libnm/nm-setting-bridge.h
/usr/include/libnm/nm-setting-cdma.h
/usr/include/libnm/nm-setting-connection.h
/usr/include/libnm/nm-setting-dcb.h
/usr/include/libnm/nm-setting-dummy.h
/usr/include/libnm/nm-setting-generic.h
/usr/include/libnm/nm-setting-gsm.h
/usr/include/libnm/nm-setting-infiniband.h
/usr/include/libnm/nm-setting-ip-config.h
/usr/include/libnm/nm-setting-ip-tunnel.h
/usr/include/libnm/nm-setting-ip4-config.h
/usr/include/libnm/nm-setting-ip6-config.h
/usr/include/libnm/nm-setting-macsec.h
/usr/include/libnm/nm-setting-macvlan.h
/usr/include/libnm/nm-setting-olpc-mesh.h
/usr/include/libnm/nm-setting-ppp.h
/usr/include/libnm/nm-setting-pppoe.h
/usr/include/libnm/nm-setting-proxy.h
/usr/include/libnm/nm-setting-serial.h
/usr/include/libnm/nm-setting-team-port.h
/usr/include/libnm/nm-setting-team.h
/usr/include/libnm/nm-setting-tun.h
/usr/include/libnm/nm-setting-user.h
/usr/include/libnm/nm-setting-vlan.h
/usr/include/libnm/nm-setting-vpn.h
/usr/include/libnm/nm-setting-vxlan.h
/usr/include/libnm/nm-setting-wimax.h
/usr/include/libnm/nm-setting-wired.h
/usr/include/libnm/nm-setting-wireless-security.h
/usr/include/libnm/nm-setting-wireless.h
/usr/include/libnm/nm-setting.h
/usr/include/libnm/nm-simple-connection.h
/usr/include/libnm/nm-types.h
/usr/include/libnm/nm-utils.h
/usr/include/libnm/nm-version-macros.h
/usr/include/libnm/nm-version.h
/usr/include/libnm/nm-vpn-connection.h
/usr/include/libnm/nm-vpn-dbus-interface.h
/usr/include/libnm/nm-vpn-editor-plugin.h
/usr/include/libnm/nm-vpn-editor.h
/usr/include/libnm/nm-vpn-plugin-info.h
/usr/include/libnm/nm-vpn-plugin-old.h
/usr/include/libnm/nm-vpn-service-plugin.h
/usr/include/libnm/nm-wimax-nsp.h
/usr/lib64/libnm-glib-vpn.so
/usr/lib64/libnm-glib.so
/usr/lib64/libnm-util.so
/usr/lib64/libnm.so
/usr/lib64/pkgconfig/NetworkManager.pc
/usr/lib64/pkgconfig/libnm-glib-vpn.pc
/usr/lib64/pkgconfig/libnm-glib.pc
/usr/lib64/pkgconfig/libnm-util.pc
/usr/lib64/pkgconfig/libnm.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libnm-glib-vpn.so
/usr/lib32/libnm-glib.so
/usr/lib32/libnm-util.so
/usr/lib32/libnm.so
/usr/lib32/pkgconfig/32NetworkManager.pc
/usr/lib32/pkgconfig/32libnm-glib-vpn.pc
/usr/lib32/pkgconfig/32libnm-glib.pc
/usr/lib32/pkgconfig/32libnm-util.pc
/usr/lib32/pkgconfig/32libnm.pc
/usr/lib32/pkgconfig/NetworkManager.pc
/usr/lib32/pkgconfig/libnm-glib-vpn.pc
/usr/lib32/pkgconfig/libnm-glib.pc
/usr/lib32/pkgconfig/libnm-util.pc
/usr/lib32/pkgconfig/libnm.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/NetworkManager/*
%doc /usr/share/man/man1/*
%doc /usr/share/man/man5/*
%doc /usr/share/man/man7/*
%doc /usr/share/man/man8/*
/usr/share/gtk-doc/html/NetworkManager/NetworkManager.conf.html
/usr/share/gtk-doc/html/NetworkManager/NetworkManager.devhelp2
/usr/share/gtk-doc/html/NetworkManager/NetworkManager.html
/usr/share/gtk-doc/html/NetworkManager/ch01.html
/usr/share/gtk-doc/html/NetworkManager/dbus-secret-agent.html
/usr/share/gtk-doc/html/NetworkManager/dbus-types.html
/usr/share/gtk-doc/html/NetworkManager/dbus-vpn-types.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.AccessPoint.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.AgentManager.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Connection.Active.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.DHCP4Config.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.DHCP6Config.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Device.Adsl.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Device.Bluetooth.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Device.Bond.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Device.Bridge.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Device.Dummy.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Device.Generic.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Device.IPTunnel.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Device.Infiniband.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Device.Macsec.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Device.Macvlan.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Device.Modem.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Device.OlpcMesh.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Device.Statistics.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Device.Team.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Device.Tun.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Device.Veth.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Device.Vlan.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Device.Vxlan.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Device.WiMax.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Device.Wired.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Device.Wireless.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Device.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.DnsManager.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.IP4Config.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.IP6Config.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.PPP.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.SecretAgent.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Settings.Connection.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Settings.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.VPN.Connection.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.VPN.Plugin.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.html
/usr/share/gtk-doc/html/NetworkManager/home.png
/usr/share/gtk-doc/html/NetworkManager/index.html
/usr/share/gtk-doc/html/NetworkManager/ix01.html
/usr/share/gtk-doc/html/NetworkManager/left-insensitive.png
/usr/share/gtk-doc/html/NetworkManager/left.png
/usr/share/gtk-doc/html/NetworkManager/license.html
/usr/share/gtk-doc/html/NetworkManager/manpages.html
/usr/share/gtk-doc/html/NetworkManager/nm-dbus-types.html
/usr/share/gtk-doc/html/NetworkManager/nm-online.html
/usr/share/gtk-doc/html/NetworkManager/nm-settings-ifcfg-rh.html
/usr/share/gtk-doc/html/NetworkManager/nm-settings-keyfile.html
/usr/share/gtk-doc/html/NetworkManager/nm-settings.html
/usr/share/gtk-doc/html/NetworkManager/nm-vpn-dbus-types.html
/usr/share/gtk-doc/html/NetworkManager/nmcli-examples.html
/usr/share/gtk-doc/html/NetworkManager/nmcli.html
/usr/share/gtk-doc/html/NetworkManager/nmtui.html
/usr/share/gtk-doc/html/NetworkManager/ref-dbus-access-points.html
/usr/share/gtk-doc/html/NetworkManager/ref-dbus-active-connections.html
/usr/share/gtk-doc/html/NetworkManager/ref-dbus-agent-manager.html
/usr/share/gtk-doc/html/NetworkManager/ref-dbus-devices.html
/usr/share/gtk-doc/html/NetworkManager/ref-dbus-dhcp4-configs.html
/usr/share/gtk-doc/html/NetworkManager/ref-dbus-dhcp6-configs.html
/usr/share/gtk-doc/html/NetworkManager/ref-dbus-dns-manager.html
/usr/share/gtk-doc/html/NetworkManager/ref-dbus-ip4-configs.html
/usr/share/gtk-doc/html/NetworkManager/ref-dbus-ip6-configs.html
/usr/share/gtk-doc/html/NetworkManager/ref-dbus-manager.html
/usr/share/gtk-doc/html/NetworkManager/ref-dbus-settings-manager.html
/usr/share/gtk-doc/html/NetworkManager/ref-dbus-settings.html
/usr/share/gtk-doc/html/NetworkManager/ref-settings.html
/usr/share/gtk-doc/html/NetworkManager/right-insensitive.png
/usr/share/gtk-doc/html/NetworkManager/right.png
/usr/share/gtk-doc/html/NetworkManager/secret-agents.html
/usr/share/gtk-doc/html/NetworkManager/secrets-flags.html
/usr/share/gtk-doc/html/NetworkManager/settings-802-11-olpc-mesh.html
/usr/share/gtk-doc/html/NetworkManager/settings-802-11-wireless-security.html
/usr/share/gtk-doc/html/NetworkManager/settings-802-11-wireless.html
/usr/share/gtk-doc/html/NetworkManager/settings-802-1x.html
/usr/share/gtk-doc/html/NetworkManager/settings-802-3-ethernet.html
/usr/share/gtk-doc/html/NetworkManager/settings-adsl.html
/usr/share/gtk-doc/html/NetworkManager/settings-bluetooth.html
/usr/share/gtk-doc/html/NetworkManager/settings-bond.html
/usr/share/gtk-doc/html/NetworkManager/settings-bridge-port.html
/usr/share/gtk-doc/html/NetworkManager/settings-bridge.html
/usr/share/gtk-doc/html/NetworkManager/settings-cdma.html
/usr/share/gtk-doc/html/NetworkManager/settings-connection.html
/usr/share/gtk-doc/html/NetworkManager/settings-dcb.html
/usr/share/gtk-doc/html/NetworkManager/settings-dummy.html
/usr/share/gtk-doc/html/NetworkManager/settings-generic.html
/usr/share/gtk-doc/html/NetworkManager/settings-gsm.html
/usr/share/gtk-doc/html/NetworkManager/settings-infiniband.html
/usr/share/gtk-doc/html/NetworkManager/settings-ip-tunnel.html
/usr/share/gtk-doc/html/NetworkManager/settings-ipv4.html
/usr/share/gtk-doc/html/NetworkManager/settings-ipv6.html
/usr/share/gtk-doc/html/NetworkManager/settings-macsec.html
/usr/share/gtk-doc/html/NetworkManager/settings-macvlan.html
/usr/share/gtk-doc/html/NetworkManager/settings-ppp.html
/usr/share/gtk-doc/html/NetworkManager/settings-pppoe.html
/usr/share/gtk-doc/html/NetworkManager/settings-proxy.html
/usr/share/gtk-doc/html/NetworkManager/settings-serial.html
/usr/share/gtk-doc/html/NetworkManager/settings-team-port.html
/usr/share/gtk-doc/html/NetworkManager/settings-team.html
/usr/share/gtk-doc/html/NetworkManager/settings-tun.html
/usr/share/gtk-doc/html/NetworkManager/settings-user.html
/usr/share/gtk-doc/html/NetworkManager/settings-vlan.html
/usr/share/gtk-doc/html/NetworkManager/settings-vpn.html
/usr/share/gtk-doc/html/NetworkManager/settings-vxlan.html
/usr/share/gtk-doc/html/NetworkManager/settings-wimax.html
/usr/share/gtk-doc/html/NetworkManager/spec.html
/usr/share/gtk-doc/html/NetworkManager/style.css
/usr/share/gtk-doc/html/NetworkManager/up-insensitive.png
/usr/share/gtk-doc/html/NetworkManager/up.png
/usr/share/gtk-doc/html/NetworkManager/vpn-plugins.html
/usr/share/gtk-doc/html/libnm-glib/NMAccessPoint.html
/usr/share/gtk-doc/html/libnm-glib/NMActiveConnection.html
/usr/share/gtk-doc/html/libnm-glib/NMClient.html
/usr/share/gtk-doc/html/libnm-glib/NMDHCP4Config.html
/usr/share/gtk-doc/html/libnm-glib/NMDHCP6Config.html
/usr/share/gtk-doc/html/libnm-glib/NMDevice.html
/usr/share/gtk-doc/html/libnm-glib/NMDeviceAdsl.html
/usr/share/gtk-doc/html/libnm-glib/NMDeviceBond.html
/usr/share/gtk-doc/html/libnm-glib/NMDeviceBridge.html
/usr/share/gtk-doc/html/libnm-glib/NMDeviceBt.html
/usr/share/gtk-doc/html/libnm-glib/NMDeviceEthernet.html
/usr/share/gtk-doc/html/libnm-glib/NMDeviceGeneric.html
/usr/share/gtk-doc/html/libnm-glib/NMDeviceInfiniband.html
/usr/share/gtk-doc/html/libnm-glib/NMDeviceModem.html
/usr/share/gtk-doc/html/libnm-glib/NMDeviceOlpcMesh.html
/usr/share/gtk-doc/html/libnm-glib/NMDeviceTeam.html
/usr/share/gtk-doc/html/libnm-glib/NMDeviceVlan.html
/usr/share/gtk-doc/html/libnm-glib/NMDeviceWifi.html
/usr/share/gtk-doc/html/libnm-glib/NMDeviceWimax.html
/usr/share/gtk-doc/html/libnm-glib/NMIP4Config.html
/usr/share/gtk-doc/html/libnm-glib/NMIP6Config.html
/usr/share/gtk-doc/html/libnm-glib/NMObject.html
/usr/share/gtk-doc/html/libnm-glib/NMRemoteConnection.html
/usr/share/gtk-doc/html/libnm-glib/NMRemoteSettings.html
/usr/share/gtk-doc/html/libnm-glib/NMSecretAgent.html
/usr/share/gtk-doc/html/libnm-glib/NMVPNConnection.html
/usr/share/gtk-doc/html/libnm-glib/NMWimaxNsp.html
/usr/share/gtk-doc/html/libnm-glib/annotation-glossary.html
/usr/share/gtk-doc/html/libnm-glib/api-index-full.html
/usr/share/gtk-doc/html/libnm-glib/ch02.html
/usr/share/gtk-doc/html/libnm-glib/home.png
/usr/share/gtk-doc/html/libnm-glib/index.html
/usr/share/gtk-doc/html/libnm-glib/left-insensitive.png
/usr/share/gtk-doc/html/libnm-glib/left.png
/usr/share/gtk-doc/html/libnm-glib/libnm-glib-NMVPNPlugin.html
/usr/share/gtk-doc/html/libnm-glib/libnm-glib-NMVpnPluginUiWidget.html
/usr/share/gtk-doc/html/libnm-glib/libnm-glib-nm-types.html
/usr/share/gtk-doc/html/libnm-glib/libnm-glib-nm-vpn-plugin-utils.html
/usr/share/gtk-doc/html/libnm-glib/libnm-glib.devhelp2
/usr/share/gtk-doc/html/libnm-glib/libnm-glib.png
/usr/share/gtk-doc/html/libnm-glib/object-tree.html
/usr/share/gtk-doc/html/libnm-glib/ref-overview.html
/usr/share/gtk-doc/html/libnm-glib/right-insensitive.png
/usr/share/gtk-doc/html/libnm-glib/right.png
/usr/share/gtk-doc/html/libnm-glib/style.css
/usr/share/gtk-doc/html/libnm-glib/up-insensitive.png
/usr/share/gtk-doc/html/libnm-glib/up.png
/usr/share/gtk-doc/html/libnm-util/NMConnection.html
/usr/share/gtk-doc/html/libnm-util/NMSetting.html
/usr/share/gtk-doc/html/libnm-util/NMSetting8021x.html
/usr/share/gtk-doc/html/libnm-util/NMSettingAdsl.html
/usr/share/gtk-doc/html/libnm-util/NMSettingBluetooth.html
/usr/share/gtk-doc/html/libnm-util/NMSettingBond.html
/usr/share/gtk-doc/html/libnm-util/NMSettingBridge.html
/usr/share/gtk-doc/html/libnm-util/NMSettingBridgePort.html
/usr/share/gtk-doc/html/libnm-util/NMSettingCdma.html
/usr/share/gtk-doc/html/libnm-util/NMSettingConnection.html
/usr/share/gtk-doc/html/libnm-util/NMSettingDcb.html
/usr/share/gtk-doc/html/libnm-util/NMSettingGeneric.html
/usr/share/gtk-doc/html/libnm-util/NMSettingGsm.html
/usr/share/gtk-doc/html/libnm-util/NMSettingIP4Config.html
/usr/share/gtk-doc/html/libnm-util/NMSettingIP6Config.html
/usr/share/gtk-doc/html/libnm-util/NMSettingInfiniband.html
/usr/share/gtk-doc/html/libnm-util/NMSettingOlpcMesh.html
/usr/share/gtk-doc/html/libnm-util/NMSettingPPP.html
/usr/share/gtk-doc/html/libnm-util/NMSettingPPPOE.html
/usr/share/gtk-doc/html/libnm-util/NMSettingSerial.html
/usr/share/gtk-doc/html/libnm-util/NMSettingTeam.html
/usr/share/gtk-doc/html/libnm-util/NMSettingTeamPort.html
/usr/share/gtk-doc/html/libnm-util/NMSettingVPN.html
/usr/share/gtk-doc/html/libnm-util/NMSettingVlan.html
/usr/share/gtk-doc/html/libnm-util/NMSettingWimax.html
/usr/share/gtk-doc/html/libnm-util/NMSettingWired.html
/usr/share/gtk-doc/html/libnm-util/NMSettingWireless.html
/usr/share/gtk-doc/html/libnm-util/NMSettingWirelessSecurity.html
/usr/share/gtk-doc/html/libnm-util/annotation-glossary.html
/usr/share/gtk-doc/html/libnm-util/api-index-full.html
/usr/share/gtk-doc/html/libnm-util/ch01.html
/usr/share/gtk-doc/html/libnm-util/home.png
/usr/share/gtk-doc/html/libnm-util/index.html
/usr/share/gtk-doc/html/libnm-util/left-insensitive.png
/usr/share/gtk-doc/html/libnm-util/left.png
/usr/share/gtk-doc/html/libnm-util/libnm-util-NetworkManager.html
/usr/share/gtk-doc/html/libnm-util/libnm-util-NetworkManagerVPN.html
/usr/share/gtk-doc/html/libnm-util/libnm-util-nm-utils.html
/usr/share/gtk-doc/html/libnm-util/libnm-util.devhelp2
/usr/share/gtk-doc/html/libnm-util/object-tree.html
/usr/share/gtk-doc/html/libnm-util/right-insensitive.png
/usr/share/gtk-doc/html/libnm-util/right.png
/usr/share/gtk-doc/html/libnm-util/style.css
/usr/share/gtk-doc/html/libnm-util/up-insensitive.png
/usr/share/gtk-doc/html/libnm-util/up.png
/usr/share/gtk-doc/html/libnm/NMAccessPoint.html
/usr/share/gtk-doc/html/libnm/NMActiveConnection.html
/usr/share/gtk-doc/html/libnm/NMClient.html
/usr/share/gtk-doc/html/libnm/NMConnection.html
/usr/share/gtk-doc/html/libnm/NMDevice.html
/usr/share/gtk-doc/html/libnm/NMDeviceAdsl.html
/usr/share/gtk-doc/html/libnm/NMDeviceBond.html
/usr/share/gtk-doc/html/libnm/NMDeviceBridge.html
/usr/share/gtk-doc/html/libnm/NMDeviceBt.html
/usr/share/gtk-doc/html/libnm/NMDeviceDummy.html
/usr/share/gtk-doc/html/libnm/NMDeviceEthernet.html
/usr/share/gtk-doc/html/libnm/NMDeviceGeneric.html
/usr/share/gtk-doc/html/libnm/NMDeviceIPTunnel.html
/usr/share/gtk-doc/html/libnm/NMDeviceInfiniband.html
/usr/share/gtk-doc/html/libnm/NMDeviceMacsec.html
/usr/share/gtk-doc/html/libnm/NMDeviceMacvlan.html
/usr/share/gtk-doc/html/libnm/NMDeviceModem.html
/usr/share/gtk-doc/html/libnm/NMDeviceOlpcMesh.html
/usr/share/gtk-doc/html/libnm/NMDeviceTeam.html
/usr/share/gtk-doc/html/libnm/NMDeviceTun.html
/usr/share/gtk-doc/html/libnm/NMDeviceVlan.html
/usr/share/gtk-doc/html/libnm/NMDeviceVxlan.html
/usr/share/gtk-doc/html/libnm/NMDeviceWifi.html
/usr/share/gtk-doc/html/libnm/NMDeviceWimax.html
/usr/share/gtk-doc/html/libnm/NMDhcpConfig.html
/usr/share/gtk-doc/html/libnm/NMIPConfig.html
/usr/share/gtk-doc/html/libnm/NMObject.html
/usr/share/gtk-doc/html/libnm/NMRemoteConnection.html
/usr/share/gtk-doc/html/libnm/NMSecretAgentOld.html
/usr/share/gtk-doc/html/libnm/NMSetting.html
/usr/share/gtk-doc/html/libnm/NMSetting8021x.html
/usr/share/gtk-doc/html/libnm/NMSettingAdsl.html
/usr/share/gtk-doc/html/libnm/NMSettingBluetooth.html
/usr/share/gtk-doc/html/libnm/NMSettingBond.html
/usr/share/gtk-doc/html/libnm/NMSettingBridge.html
/usr/share/gtk-doc/html/libnm/NMSettingBridgePort.html
/usr/share/gtk-doc/html/libnm/NMSettingCdma.html
/usr/share/gtk-doc/html/libnm/NMSettingConnection.html
/usr/share/gtk-doc/html/libnm/NMSettingDcb.html
/usr/share/gtk-doc/html/libnm/NMSettingDummy.html
/usr/share/gtk-doc/html/libnm/NMSettingGeneric.html
/usr/share/gtk-doc/html/libnm/NMSettingGsm.html
/usr/share/gtk-doc/html/libnm/NMSettingIP4Config.html
/usr/share/gtk-doc/html/libnm/NMSettingIP6Config.html
/usr/share/gtk-doc/html/libnm/NMSettingIPConfig.html
/usr/share/gtk-doc/html/libnm/NMSettingIPTunnel.html
/usr/share/gtk-doc/html/libnm/NMSettingInfiniband.html
/usr/share/gtk-doc/html/libnm/NMSettingMacsec.html
/usr/share/gtk-doc/html/libnm/NMSettingMacvlan.html
/usr/share/gtk-doc/html/libnm/NMSettingOlpcMesh.html
/usr/share/gtk-doc/html/libnm/NMSettingPpp.html
/usr/share/gtk-doc/html/libnm/NMSettingPppoe.html
/usr/share/gtk-doc/html/libnm/NMSettingSerial.html
/usr/share/gtk-doc/html/libnm/NMSettingTeam.html
/usr/share/gtk-doc/html/libnm/NMSettingTeamPort.html
/usr/share/gtk-doc/html/libnm/NMSettingTun.html
/usr/share/gtk-doc/html/libnm/NMSettingVlan.html
/usr/share/gtk-doc/html/libnm/NMSettingVpn.html
/usr/share/gtk-doc/html/libnm/NMSettingVxlan.html
/usr/share/gtk-doc/html/libnm/NMSettingWimax.html
/usr/share/gtk-doc/html/libnm/NMSettingWired.html
/usr/share/gtk-doc/html/libnm/NMSettingWireless.html
/usr/share/gtk-doc/html/libnm/NMSettingWirelessSecurity.html
/usr/share/gtk-doc/html/libnm/NMSimpleConnection.html
/usr/share/gtk-doc/html/libnm/NMVpnConnection.html
/usr/share/gtk-doc/html/libnm/NMVpnEditorPlugin.html
/usr/share/gtk-doc/html/libnm/NMWimaxNsp.html
/usr/share/gtk-doc/html/libnm/annotation-glossary.html
/usr/share/gtk-doc/html/libnm/api-index-full.html
/usr/share/gtk-doc/html/libnm/ch02.html
/usr/share/gtk-doc/html/libnm/ch03.html
/usr/share/gtk-doc/html/libnm/ch04.html
/usr/share/gtk-doc/html/libnm/ch05.html
/usr/share/gtk-doc/html/libnm/ch06.html
/usr/share/gtk-doc/html/libnm/home.png
/usr/share/gtk-doc/html/libnm/index.html
/usr/share/gtk-doc/html/libnm/left-insensitive.png
/usr/share/gtk-doc/html/libnm/left.png
/usr/share/gtk-doc/html/libnm/libnm-nm-dbus-interface.html
/usr/share/gtk-doc/html/libnm/libnm-nm-errors.html
/usr/share/gtk-doc/html/libnm/libnm-nm-utils.html
/usr/share/gtk-doc/html/libnm/libnm-nm-version.html
/usr/share/gtk-doc/html/libnm/libnm-nm-vpn-dbus-interface.html
/usr/share/gtk-doc/html/libnm/libnm.devhelp2
/usr/share/gtk-doc/html/libnm/libnm.png
/usr/share/gtk-doc/html/libnm/object-tree.html
/usr/share/gtk-doc/html/libnm/ref-overview.html
/usr/share/gtk-doc/html/libnm/right-insensitive.png
/usr/share/gtk-doc/html/libnm/right.png
/usr/share/gtk-doc/html/libnm/style.css
/usr/share/gtk-doc/html/libnm/up-insensitive.png
/usr/share/gtk-doc/html/libnm/up.png
/usr/share/gtk-doc/html/libnm/usage.html

%files lib
%defattr(-,root,root,-)
/usr/lib64/NetworkManager/libnm-device-plugin-adsl.so
/usr/lib64/NetworkManager/libnm-device-plugin-wifi.so
/usr/lib64/NetworkManager/libnm-settings-plugin-ibft.so
/usr/lib64/libnm-glib-vpn.so.1
/usr/lib64/libnm-glib-vpn.so.1.2.0
/usr/lib64/libnm-glib.so.4
/usr/lib64/libnm-glib.so.4.9.0
/usr/lib64/libnm-util.so.2
/usr/lib64/libnm-util.so.2.7.0
/usr/lib64/libnm.so.0
/usr/lib64/libnm.so.0.1.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/NetworkManager/libnm-device-plugin-adsl.so
/usr/lib32/NetworkManager/libnm-device-plugin-wifi.so
/usr/lib32/NetworkManager/libnm-settings-plugin-ibft.so
/usr/lib32/libnm-glib-vpn.so.1
/usr/lib32/libnm-glib-vpn.so.1.2.0
/usr/lib32/libnm-glib.so.4
/usr/lib32/libnm-glib.so.4.9.0
/usr/lib32/libnm-util.so.2
/usr/lib32/libnm-util.so.2.7.0
/usr/lib32/libnm.so.0
/usr/lib32/libnm.so.0.1.0

%files locales -f NetworkManager.lang
%defattr(-,root,root,-)

