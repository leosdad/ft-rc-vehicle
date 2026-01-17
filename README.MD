
# fischertechnik RC vehicle with ESP32 gamepad

This project uses a fischertechnik TXT 4.0 controller to drive an RC vehicle, controlled by an ESP32-based gamepad. The gamepad communicates with the TXT controller over WiFi using UDP protocol.

I'm also starting to update the fischertechnik library sources by replacing the auto-generated comments with descriptive ones that can actually help coding. This is being done with the help of GitHub Copilot (My Python expertise is near zero) using the GPT-5 mini and Raptor mini models which are free for non-paying customers and have unlimited use for paying users (my case).

My sincere thank David Adams for his great book on the TXT 4.0 controller.

## References

- [TXT 4.0 controller book](https://forum.ftcommunity.de/viewtopic.php?t=8521) thread at the ftcommunity forum
- [TXT 4.0 and VSC server](https://forum.ftcommunity.de/viewtopic.php?f=8&t=9333&p=70026#p70026) thread at the ftcommunity forum
- [Robot with remote control](https://forum.ftcommunity.de/viewtopic.php?f=8&t=8694&start=20) thread at the ftcommunity forum
- [Using VSCode to program the TXT 4.0](https://forum.ftcommunity.de/viewtopic.php?f=8&t=9588)

## Instructions

1. In the TXT 4.0, enable Settings / Services / SSH.
2. In the TXT 4.0, enable Settings / Remote access / SSH.
3. To avoid entering passwords each time, generate an SSH key pair (on Windows, save it at `%USERPROFILE%\.ssh`) and copy the public key to the `/opt/ft/.ssh/authorized_keys` file in the TXT4.
3. Create the folder `/opt/ft/workspaces/RC_vehicle` in the TXT4.
4. Run the task at `.vscode\tasks.json` to upload the files to the TXT4.

## Remote server data

- File protocol: SFTP
- Host name: 192.168.15.30 (wifi) or 192.168.7.2 (USB). (Use your actual controller IP here)
- Port number: 22
- User: ft
- Password: fischertechnik
