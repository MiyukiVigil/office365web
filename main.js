const { app, BrowserWindow, Menu } = require('electron');
const path = require('path');

function createWindow() {
    // Create the browser window
    const win = new BrowserWindow({
        width: 1200,
        height: 800,
        webPreferences: {
            nodeIntegration: false, // Disable Node.js integration for security
            contextIsolation: true, // Enable context isolation for security
        },
        icon: path.join(__dirname, 'icon.png'), // Optional: Remove if no icon.png exists
    });

    // Load the Microsoft 365 home page by default
    win.loadURL('https://www.office.com');

    // Define the custom menu
    const menuTemplate = [
        {
            label: 'File',
            submenu: [
                {
                    label: 'New Window',
                    click: () => createWindow(), // Opens a new instance of the app
                },
                {
                    label: 'Quit',
                    click: () => app.quit(),
                },
            ],
        },
                {
            label: 'Home',
            click: () => win.loadURL('https://www.office.com'),
        },
        {
            label: 'Apps',
            submenu: [
                {
                    label: 'Word',
                    click: () => win.loadURL('https://www.office.com/launch/word'),
                },
                {
                    label: 'Excel',
                    click: () => win.loadURL('https://www.office.com/launch/excel'),
                },
                {
                    label: 'PowerPoint',
                    click: () => win.loadURL('https://www.office.com/launch/powerpoint'),
                },
                {
                    label: 'Outlook',
                    click: () => win.loadURL('https://outlook.office.com/mail'),
                },
                {
                    label: 'OneNote',
                    click: () => win.loadURL('https://www.office.com/launch/OneNote')
                },
                {
                    label: 'Teams',
                    click: () => win.loadURL('https://teams.microsoft.com/'),
                },
                {
                    label: 'One Drive',
                    click: () => win.loadURL('https://m365.cloud.microsoft/onedrive/?auth=2'),
                },
            ],
        },
        {
            label: 'Help',
            submenu: [
                {
                    label: 'About',
                    click: () => win.loadURL('https://www.microsoft.com/en-us/microsoft-365'),
                },
            ],
        },
    ];

    // Build and set the menu
    const menu = Menu.buildFromTemplate(menuTemplate);
    Menu.setApplicationMenu(menu);
}

// When Electron is ready, create the window
app.whenReady().then(() => {
    createWindow();

    // Recreate window if closed and reopened on macOS
    app.on('activate', () => {
        if (BrowserWindow.getAllWindows().length === 0) {
            createWindow();
        }
    });
});

// Quit the app when all windows are closed (except on macOS)
app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit();
    }
});