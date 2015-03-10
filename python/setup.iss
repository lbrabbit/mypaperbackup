[Setup]
AppName=留言板備份
AppVerName=留言板備份 v0.1
DefaultDirName={pf}\BBackup
DefaultGroupName=留言板備份
UninstallDisplayIcon={app}\Main.exe
Compression=lzma
SolidCompression=yes

[Files]
Source: tcl\tcl8.4\*; DestDir: {app}\tcl\tcl8.4\; Flags: ignoreversion recursesubdirs
Source: tcl\tk8.4\images\*; DestDir: {app}\tcl\tk8.4\images\; Flags: ignoreversion recursesubdirs
Source: tcl\tk8.4\msgs\*; DestDir: {app}\tcl\tk8.4\msgs\; Flags: ignoreversion recursesubdirs
Source: tcl\tk8.4\*; DestDir: {app}\tcl\tk8.4\; Flags: ignoreversion
Source: _socket.pyd; DestDir: {app}
Source: _ssl.pyd; DestDir: {app}
Source: _tkinter.pyd; DestDir: {app}
Source: library.zip; DestDir: {app}
Source: python24.dll; DestDir: {app}
Source: tcl84.dll; DestDir: {app}
Source: tk84.dll; DestDir: {app}
Source: w9xpopen.exe; DestDir: {app}
Source: main.exe; DestDir: {app}

Source: ..\PChome_Mypaper.py; DestDir: {app}
Source: ..\plugin.py; DestDir: {app}
Source: ..\Taipeilink_Guest.py; DestDir: {app}
Source: ..\textbox.py; DestDir: {app}
Source: ..\txt_chinese.py; DestDir: {app}
Source: ..\Wretch_Guest.py; DestDir: {app}

Source: ..\gpl_big5.txt; DestDir: {app}
Source: ..\gpl.txt; DestDir: {app}
Source: ..\readme.txt; DestDir: {app}
Source: ..\release.txt; DestDir: {app}
[Icons]
Name: {group}\留言板備份; Filename: {app}\main.exe; WorkingDir: {app}
Name: {group}\解除安裝; Filename: {uninstallexe}
[Languages]
Name: big5; MessagesFile: compiler:Languages\ChineseTrad-2-4.2.2.isl
;Name: en; MessagesFile: compiler:Default.isl
[Dirs]
Name: {app}\tcl
[Run]
Filename: {app}\main.exe; WorkingDir: {app}; Description: "立刻啟動程序"; Flags: nowait postinstall skipifsilent

