Counter-Strike 1.6 for Nintendo Switch (Xash3D FWGS)
====================================================

A homebrew port of Counter-Strike 1.6 built on the modern Xash3D FWGS engine and
the cs16-client project. Touch, controller and gyro controls, bots, voice chat.

This package contains NO game data. You need your own copy of Counter-Strike 1.6
(the "cstrike" and "valve" folders from a legitimate Steam install).

Install
-------
1. Copy this whole folder to  sd:/switch/cstrike-global/  on your SD card.
2. Copy your own "cstrike" and "valve" game folders into it and merge when asked
   (this package adds files inside cstrike/ and valve/, it does not replace your data).
3. Launch "Counter-Strike 1.6" from the homebrew menu.
   Run it through the Album (applet) only if you must: title takeover gives more memory.

Controls (defaults, edit cstrike/userconfig.cfg to change)
----------------------------------------------------------
R2 fire, L2 secondary fire, A use, B jump, L1 crouch, R1 reload, X weapon impulse,
Y last weapon, D-pad Up buy menu, D-pad Down drop, D-pad Left/Right previous/next weapon,
Left stick click walk, Right stick hold voice chat (headset microphone needed),
Minus scoreboard, Plus cancel/select. Gyro aiming is on; type "gyro" in the console to toggle it.

Notes
-----
- Tested on a Switch Lite only. Other models and firmware versions are unverified.
- Text fields open the system keyboard when you press A or tap them.
- Voice chat needs a headset and a server with voice enabled.

Source and licenses
-------------------
The engine and the game code are free software. The changes made for this port are in source/*.patch,
to be applied on the upstream projects at these commits:
  FWGS/xash3d-fwgs 03a396e (submodule FWGS/mainui_cpp bb47191)
  Velaron/cs16-client 9778fec (ReGameDLL_CS 7be9d59, yapb 4967a22)
  fgsfdsfgs/libsolder 36e5f31
Xash3D FWGS is licensed under the GNU GPL v3. See each upstream repository for the full license text.
Counter-Strike and Half-Life are trademarks of Valve Corporation. This project is not affiliated with or endorsed by Valve.
