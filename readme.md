# Office365 Web App

## Overview
This is a simple Electron-based web application that provides quick access to Microsoft Office 365 services. It was created for personal use, and as such, it will not receive frequent updates or maintenance. However, feel free to fork and modify the code as needed.

## Features
- Opens Microsoft Office 365 in an Electron window.
- Provides a custom menu for easy navigation between Office applications, including:
  - Word
  - Excel
  - PowerPoint
  - Outlook
  - OneNote
  - Teams
  - OneDrive
- Allows opening multiple windows.
- Lightweight and minimal setup.

## Installation
This application is available in multiple formats:
- **RPM**: For Fedora and other RPM-based distributions.
- **AppImage**: Portable version that can run on most Linux distributions without installation.
- **tar.gz**: Archive containing pre-built binaries.

### Running the AppImage
```sh
chmod +x Office365WebApp.AppImage
./Office365WebApp.AppImage
```
### Running the RPM (Fedora, RHEL-based)
```sh
sudo dnf install office365-web-app.rpm
```

### Extracting and Running from tar.gz
```sh
tar -xzf office365-web-app.tar.gz
cd Office365WebApp
./office365-web-app
```
# Disclaimer
This project is not affiliated with or endorsed by Microsoft. It simply provides a web wrapper for Microsoft Office 365 services.

Since this project was built for personal use, support and updates will be minimal. If you encounter any issues, you are encouraged to fork the repository and make your own modifications.
