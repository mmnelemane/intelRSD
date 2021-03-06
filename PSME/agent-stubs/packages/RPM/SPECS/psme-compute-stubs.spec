Summary: Package for RSA PSME compute stubs
Name: psme-compute-stubs
Version: 0.0.0.0
Release: PreAlpha
License: Apache License 2.0
Group: Applications/System
Requires: jsoncpp libmicrohttpd libcurl libstdc++ uuid-c++
Source: %{expand:%%(pwd)}
BuildRoot: %{_topdir}/BUILD/%{name}-%{version}

%description
%{summary}

%prep
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/etc/psme
cd $RPM_BUILD_ROOT
cp -p %{SOURCEURL0}%{_bindir}/* .%{_bindir}
cp -p %{SOURCEURL0}/etc/psme/psme-compute-stubs-configuration.json ./etc/psme/

%pre
if [ "$1" != 1 ]; then
	if [ -f /etc/psme/psme-compute-stubs-configuration.json ]; then
		cp /etc/psme/psme-compute-stubs-configuration.json /etc/psme/psme-compute-stubs-configuration.json.old
	fi
else
	exit 0
fi

%post
cat <<EOF >/lib/systemd/system/psme-compute-stubs.service
[Unit]
Description=Managing PSME compute stubs
After=network.target network-online.target

[Service]
Type=simple
ExecStart=/usr/bin/psme-compute-stubs /etc/psme/psme-compute-stubs-configuration.json
PIDFile=/var/run/psme-compute-stubs.pid

[Install]
WantedBy=multi-user.target
EOF
if [ ! -f /etc/systemd/system/psme-compute-stubs.service ]; then
    ln -s /lib/systemd/system/psme-compute-stubs.service /etc/systemd/system/psme-compute-stubs.service
fi
systemctl daemon-reload
systemctl enable psme-compute-stubs

%preun
systemctl stop psme-compute-stubs

%postun
if [ "$1" == 0 ]; then
	systemctl disable psme-compute-stubs
	if [ -f /etc/systemd/system/psme-compute-stubs.service ]; then
	    rm /etc/systemd/system/psme-compute-stubs.service
	fi
	if [ -f /lib/systemd/system/psme-compute-stubs.service ]; then
	    rm /lib/systemd/system/psme-compute-stubs.service
	fi
	systemctl daemon-reload
else
	exit 0
fi

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/*
/etc/psme/*

%changelog
