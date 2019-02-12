Name:                           meta-radio
Version:                        1.0.0
Release:                        1%{?dist}
Summary:                        META-package for install and configure radio
License:                        GPLv3

Source10:                       icecast.xml
Source11:                       ices.conf

Requires:                       icecast ices meta-nginx

%description
META-package for install and configure radio.

# -------------------------------------------------------------------------------------------------------------------- #
# -----------------------------------------------------< SCRIPT >----------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

%install
install -p -m 0644 %{SOURCE10} \
    %{buildroot}%{_sysconfdir}/icecast.xml

install -p -m 0644 %{SOURCE11} \
    %{buildroot}%{_sysconfdir}/ices.conf

%files
%config %{_sysconfdir}/icecast.xml
%config %{_sysconfdir}/ices.conf

%changelog
* Tue Feb 12 2019 Kitsune Solar <kitsune.solar@gmail.com> - 1.0.0-1
- Initial build.
