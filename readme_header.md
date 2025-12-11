# Hikvision firmware archive

- [How it works](#how-it-works)
- [Download guide](#download-guide)
- [Contributing](#contributing)
- [Issues](#issues)
- [Get notified of new firmwares](#get-notified-of-new-firmwares)
- [Firmwares](#firmwares)

This is an unofficial and incomplete collection of Hikvision firmware download links.

I made this for a few reasons:

- I like having a firmware history that I can upgrade/downgrade to
- might help in case of reverse engineering
- only the latest firmware for a product is displayed on Hikvision's download center, for some reason
- this means that in case a new firmware causes issues for you, you can't even rollback unless you kept the previous one or manage to find a link to it somewhere on the internet
- I think it's easier than their website and it shows everything in one place
- I've seen a fair amount of people asking "Do I have the latest firmware for my device?"
- allows users not to have to search or ask for a specific firmware
- easier than using the Wayback Machine

## How it works

Twice a day at around 4:20 AM and PM UTC, information about the devices and their firmwares is pulled from Hikvision's website. New items are merged into the existing `devices.json` and `firmwares_live.json` files. Then, for each new firmware, details about the firmware file are retrieved and added to `firmware_info.json`. If there are new firmwares, the readme is recreated and a new release is made.

## Download guide

**Disclaimer: a small number of links have not been provided by Hikvision**

Most of the links are original ones, that point to files hosted by Hikvision. They mainly come from the live website, and archives of old website pages (like their support pages). There is also a certain amount of official links from Google Drive or other sources, which they sometimes use for beta firmwares. The rest are links that are either shared by Hikvision, or by users who have been sent links (via email after contacting support for example). When the link comes from an archived page, the source is available in the notes.

The non-original links are files hosted by third-party users. A few are hosted by myself on Google Drive. These are files that were provided by Hikvision but that we don't have the original link to anymore. When there is no original link for a firmware, a warning is shown in the notes. You are free to not trust these files and ignore them. If you want to play it safe, simply go to the [Download Center](https://www.hikvision.com/en/support/download/firmware/).

Be careful as some firmwares are beta. You should not apply a beta firmware unless you are a beta tester and/or know what you're doing. Check the notes and sources before updating. A warning will appear for beta firmwares.

As long as you make sure to check that the firmware you're looking at matches your device's model AND hardware version, you should have no problem updating\*. Usually the hardware version here will be the exact same as shown in your device's info, but sometimes one or the other will have a few characters missing at the end. This is normal and can be ignored.

A few things:

- models are sorted in alphanumeric order
- firmwares are sorted by date first and then by version, in descending order
- the date shown is not the release date of the firmware but its build date
- a firmware file targets a single combination of device model/hardware version. Sometimes you can install a firmware on another device and it will "work" (because they have very similar hardware) but it is obviously not recommended
- most download links are direct download
- any link might die at any time

Install at your own risk. I do not (and cannot) go out of my way to check if every firmware is stable. If a firmware is unstable you can use the [discussions](https://github.com/YOUR_USERNAME/hikvision-fw-archive/discussions) to report it. If enough people report the same problem and it is not an isolated case, an issue can be opened and a note could be added to the firmware to warn future users.

I offer no guarantee, and I am not Hikvision support, so please do not open issues related to the firmwares themselves. If you encounter a problem after a firmware update you can discuss it but you should [submit a request](https://www.hikvision.com/en/support/download/). You can also check the official forums to see if other users are reporting a similar issue.

\* I have read about cases where even with the right firmware, the device rejects the file. I am not sure if this is user error or a bug in the device's current firmware. Some users report success after renaming the file. If you encounter this issue, please describe it in the discussions as I would like to know more about it.

## Contributing

If you see a problem or something missing, feel free to open an issue/PR to add/fix things.

- do not directly edit `README.md`, it is auto-generated from `readme_header.md` and the list of firmwares. Edit `readme_header.md` instead
- `devices.json` can be modified to include a model or hardware version that does not appear yet on the live website (this must be done before adding a firmware for a new device). Pick a unique id > 100000 for each model and hardware version
- `firmwares_manual.json` can be modified to manually add a firmware, for example a beta firmware. It can also be used to add additional info to an existing firmware like its changelog
- the main reason to edit `firmware_info.json` is to manually add info for a firmware when an error occurs. It could also be used to mark a firmware as beta and/or unstable
- there shouldn't be anything to fix in `firmwares_live.json`
- if you want to manually add a firmware for a PR, clone the repo and run `python main.py add <url>` (see `python main.py add -h` for help)

Hikvision support can provide firmwares when contacted. If you have a firmware (or just a mirror link) that does not appear here, you can open a PR or put in in the [discussions](https://github.com/YOUR_USERNAME/hikvision-fw-archive/discussions) so that it can be added. This can help other users who won't have to contact Hikvision. If you can give details about what changes have been made to the firmware, it would be a nice bonus.

## Issues

- Some firmware links may require login or may be behind a paywall
- Firmware availability varies by region

## Get notified of new firmwares

This requires a GitHub account.

In the top right of the page click `Watch`, then `Custom`, tick `Releases` and apply.

You should receive an email next time new firmwares are published by Hikvision.

## Firmwares

\* means the device is discontinued.

Total: 0
