Name:           office365
Version:        1.0.0
Release:        1%{?dist}
Summary:        A standalone app for accessing Microsoft Office 365 Online.

License:        MIT
URL:            https://github.com/miyukivigil/office365
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gcc, make, rpm-build
Requires:       gtk3, libnotify, nss, libXScrnSaver, libXtst, xdg-utils, at-spi2-core, libuuid

%description
A standalone app for accessing Microsoft Office 365 Online. This application provides a desktop-like experience for Microsoft Office 365.

%prep
# Preparations like unpacking the source code, if needed

%build
# Any build steps (e.g., compiling the app) will go here

%install
# Specify how to install the files, such as:
install -d %{buildroot}/opt/Office365WebApp
cp -r %{_builddir}/%{name}-%{version}/dist/* %{buildroot}/opt/Office365WebApp/

# Install desktop entry and icon
install -D -m 644 build/icon.png %{buildroot}/usr/share/icons/hicolor/500x500/apps/office365.png
install -D -m 644 build/office365.desktop %{buildroot}/usr/share/applications/office365.desktop

%files
/opt/Office365WebApp
/usr/share/icons/hicolor/500x500/apps/office365.png
/usr/share/applications/office365.desktop

%changelog
* Mon Apr 01 2025 Miyuki Vigil <miyuki@example.com> - 1.0.0-1
- Initial release.
