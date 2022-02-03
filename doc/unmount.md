# Alfred-Workflow-unmountDisk
Alfred workflow to help ejecting devices with multiple volumes.

![start](https://user-images.githubusercontent.com/55148527/142225004-c5b21a4f-8c5c-461e-a43e-b9bd5d365321.png)

![list](https://user-images.githubusercontent.com/55148527/142225099-e516947e-8865-4b1c-b4ee-d086333ee778.png)

Show external devices connected to your Mac and unmount selected physical disk with 
```
     diskutil unmountDisk
```
Using modifier key ⌘ (cmd) will issue

```
     diskutil unmountDisk force 
```

This workflow was created to overcome some shortcomings with Alfred's system command _Eject_, which today does not handle well drives with multiple partitions and snapshots in APFS containers, e.g. time machine volumes with Big Sur.

You can place icon files into directory $ICONDIR to be placed before a device.
Name of icon file is <volumename>.png and $ICONDIR is relative to your home directory, that is ICONDIR=Pictures/icons will point to /Users/userid/Pictures/icons.

If no icon file exits, a default icon 💾 will be used. If there are mutliple partions in the disk, the first icon file found from the disk's volume names will be taken.



## Requirements
 - MacOs
 - [Alfred](https://www.alfredapp.com) 4.+

Workflow is implemented in Python and provides two versions:

 - Recommended and default: /usr/bin/python3, that is python 3.x
 - /usr/bin/python, that is python 2.7. Use it, if python3 is not available on your mac. ☹️

## Installation

Open file __unmount.alfredworkflow__ with Alfred from Finder.
