from winreg import *

def getAccentColor():  
    """
    Return the Windows 10 accent color used by the user in a HEX format
    """
    registry = ConnectRegistry(None,HKEY_CURRENT_USER)
    key = OpenKey(registry, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Accent')
    key_value = QueryValueEx(key,'AccentColorMenu')
    accent_int = key_value[0]
    accent = accent_int-4278190080
    accent = str(hex(accent)).split('x')[1]
    accent = accent[4:6]+accent[2:4]+accent[0:2]
    return '#'+accent