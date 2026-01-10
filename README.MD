
# fischertechnik RC vehicle with ESP32 gamepad

This project uses a fischertechnik TXT 4.0 controller to drive an RC vehicle, controlled by an ESP32-based gamepad. The gamepad communicates with the TXT controller over WiFi using UDP protocol.

It also serves to build a stub library that references fischertechnik's proprietary libraries, allowing development and testing without being inside RoboPro Code. This library is being built with the help of GitHub Copilot (My Pyhton expertise is more or less zero) using the GPT-5 mini and Raptor mini models which are free for non-paying customers and have unlimited use for paying users (my case).

## References

- TODO

## Quick instructions

1. In the TXT 4.0: Enable Settings / Services / SSH
2. In the TXT 4.0: Enable Settings / Remote access / SSH
3. In WinSCP, open the project, using the data below for remote access.
4. In WinSCP, Use Ctrl+U to keep remote folder up to date automatically. Be sure to check "Existing files only" and use text transfers in transfer settings.¹

¹ A script would be best, I didn't try it yet.

## Remote server data

- ftp://192.168.15.30/ (wifi) or ftp://192.168.7.2 (Use your actual controller IP here)
- User: ft
- Password: fischertechnik
