Name:           ooping
Version:        0.1.0
Release:        1%{?dist}
Summary:        Measures ICMP round-trip time, jitter, and packet loss with microsecond precision.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ooping
Source0:        ooping-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ooping is a sovereign, capability-bounded ICMP LATENCY written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ooping
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ooping-uninstall

%files
/usr/bin/ooping
/usr/bin/ooping-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
