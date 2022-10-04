# GNOME-sync

Syncs GNOME settings between multiple devices.

## Rationale

[If you search online](https://www.google.com/search?q=gnome+settings+sync),
you'll find no existing solution to sync GNOME preferences between multiple
devices.

The general, correct, advice is to use `dconf load` and `dconf dump` to export
some keys from the GNOME settings database. However, it seems like nobody made a
tool to simplify the process of exporting and loading the correct keys.

There are a LOT of settings stored in this database, and you don't want to sync
most of them, such as the path of the last folder accessed in the Files app, your
commands history, the position of the windows on the desktop, etc.

The common workflow if you ever attempted to sync your GNOME settings is to dump
everything using `dconf dump /` on the source device, then look over each of the
settings, remove the ones you don't want, and `dconf load / <` them on the target
device.

I started having to do this process often, and thus started maintaining a text
file with the actually relevant keys in it. Then I realized I could automate the
process of dumping the configuration, and filtering out everything not present in
the whitelist file. This is GNOME-sync.
