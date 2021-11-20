Workflow implements alarm clock
![Bildschirmfoto 2021-11-20 um 15 08 54](https://user-images.githubusercontent.com/55148527/142729362-5ce401cd-9e7e-4864-a9ab-eb30cbe65f18.png)

## Argument examples:
 
 - 14:30 Alert me for coffee time
 - +1h   Remind me: 1 hour is gone
 - +13   Remind me that 13 minutes are gone
 - +45s  Start to breeze, 45 seconds gone! 
 - +2h   Pause after 2 hours work        

## Technical notes:

Workflow uses launchd to raise the alarm.

Name of used plistfile in ~/Library/LaunchAgents is 
```
	wecker_${HOUR}_${MINUTE}.plist'
```
This plist is build from template in template.plist

External Files contained in the workflow:

- template.plist

- wecker1.py: Builds plist-file from template.plist

- wecker.sh: invoked by launchd, runs trigger\_finished.scpt

- trigger\_finished.scpt: Applescript which invokes 'finished' external trigger.  Attention: The name of this bundle is hardcoded here!
