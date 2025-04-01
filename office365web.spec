Name: office365-web-app
Version: 1.0.0
Release: 1%{?dist}
Summary: A Microsoft Office 365 web app powered with Electron
License: MIT
URL: https://github.com/Miyuki32/office365web
Source0: %{name}-%{version}.tar.gz

BuildArch: x86_64

Requires: gtk3, libnotify, nss, libXScrnSaver, libXtst, xdg-utils, at-spi2-core, libuuid

%description
A Microsoft Office 365 web app powered with Electron.

%prep
# No prep needed as we are using a pre-built tar.gz

%build
# No build needed as we are using a pre-built tar.gz

%install
rm -rf %{buildroot}
install -d %{buildroot}/opt/Office365WebApp
install -d %{buildroot}/usr/share/applications
install -d %{buildroot}/usr/share/icons/hicolor/1920x1920/apps

# Copy all required files, including .pak files
mkdir -p %{buildroot}/opt/Office365WebApp
tar -xzf %{SOURCE0} -C %{buildroot}/opt/Office365WebApp

# Install the .desktop file
install -m 0644 /home/miyukivigil/Codes/PersonalProject/office365web/office365-web-app.desktop %{buildroot}/usr/share/applications/

# Install the icon
install -m 0644 /home/miyukivigil/Codes/PersonalProject/office365web/icon.png %{buildroot}/usr/share/icons/hicolor/1920x1920/apps/office365-web-app.png

# Set executable permissions
chmod +x %{buildroot}/opt/Office365WebApp/office365-web-app

%files
/opt/Office365WebApp/
/usr/share/applications/office365-web-app.desktop
/usr/share/icons/hicolor/1920x1920/apps/office365-web-app.png

%changelog
* Tue Apr 01 2025 MiyukiVigil <ivanngu08@gmail.com> - 1.0.0-1
- Initial package.
