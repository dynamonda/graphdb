'use strict';

var electron = require('electron');
var app = electron.app;
var BrowserWindow = electron.BrowserWindow;
var Menu = electron.Menu;

var mainWindow = null;

app.on('window-all-closed', function(){
    if(process.platform != 'darwin'){
        app.quit();
    }
});

app.on('ready', function(){
    Menu.setApplicationMenu(menu);

    mainWindow = new BrowserWindow({width: 800, height: 600});
    mainWindow.loadURL('file://' + __dirname + '/index.html');

    mainWindow.on('closed', function(){
        mainWindow = null;
    });
});

var MenuTemplate = [
    {
        label: 'ReadUs',
        submenu: [
            {label: `Quit`, accelerator: 'Command+Q', click: function(){app.quit()}}
        ]
    }, {
        label: 'File',
        submenu: [
            {
                label: 'Open', 
                accelerator: 'Command+O', 
                // [FixMe]: dialogモジュールエラー
                click: function(){
                    require('dialog').showOpenDialog( {properties:['openDirectory']},
                        function(baseDir){
                            if(baseDir && baseDir[0]){
                                openWindow(baseDir[0]);
                            }
                        }
                    );
                }
            }
        ]
    }, {
        label: 'View',
        submenu: [
            { 
                label: 'Reload',
                accelerator: 'Command+R', 
                click: function(){ BrowserWindow.getFocusedWindow().reload(); }
            }, {
                label: 'Toggle DevTools',
                accelerator: 'Alt+Command+I',
                click: function(){ BrowserWindow.getFocusedWindow().toggleDevTools(); }
            }
        ]
    }
];

var menu = Menu.buildFromTemplate(MenuTemplate);
