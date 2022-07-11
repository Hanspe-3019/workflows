# workflows
This is a collection of my public Alfred Workflows.

## Requirements: 
 - macOS with [Alfred 4.+](https://www.alfredapp.com) Powerpack Licence.
 - Some workflows use python3 scripts, so they require macOS Version 10+ or separately installed python3 (anaconda, homebrew, macports).  

## The Workflows
<table><caption><small>Generated at 2022-07-11</small></caption><table><tr><th><th>Workflow<th>Version<th>contains
<tr>
<td><img src="./doc/alarmclock.png" width="128">
<td><strong>alarmclock</strong><br>&nbsp;&nbsp;&nbsp;&nbsp;alarmclock using launchd<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="doc/alarmclock.md">Read more...</a>
<td>1.1.1
<td>action.script : 4<br>input.keyword : 2<br>output.largetype : 1<br>output.notification : 1<br>trigger.external : 3
<tr>
<td><img src="./doc/createfile.png" width="128">
<td><strong>createfile</strong><br>&nbsp;&nbsp;&nbsp;&nbsp;Create File in selected Folder or current Folder<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="doc/createfile.md">Read more...</a>
<td>1.1.1
<td>action.browseinalfred : 1<br>action.script : 2<br>input.keyword : 1<br>input.scriptfilter : 1<br>output.notification : 1<br>trigger.action : 2<br>utility.argument : 3
<tr>
<td><img src="./doc/createfolder.png" width="128">
<td><strong>createfolder</strong><br>&nbsp;&nbsp;&nbsp;&nbsp;Two File Actions to create Folder in selected Folder or in current Folder.
<td>1.1.2
<td>action.browseinalfred : 1<br>action.script : 2<br>input.keyword : 1<br>output.notification : 1<br>trigger.action : 2<br>utility.argument : 1
<tr>
<td><img src="./doc/fileref.png" width="128">
<td><strong>fileref</strong><br>&nbsp;&nbsp;&nbsp;&nbsp;Generate/Follow File Reference
<td>0.0.9
<td>action.actioninalfred : 1<br>action.script : 2<br>trigger.action : 1<br>trigger.external : 1
<tr>
<td><img src="./doc/frontmostdoc.png" width="128">
<td><strong>frontmostdoc</strong><br>&nbsp;&nbsp;&nbsp;&nbsp;Show frontmost document's file of frontmost application<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="doc/frontmostdoc.md">Read more...</a>
<td>1.2.1
<td>action.actioninalfred : 1<br>action.script : 2<br>input.keyword : 1<br>output.playsound : 1<br>trigger.hotkey : 1<br>utility.argument : 1<br>utility.conditional : 1<br>utility.transform : 1
<tr>
<td><img src="./doc/Going with alt.png" width="128">
<td><strong>Going with alt</strong><br>&nbsp;&nbsp;&nbsp;&nbsp;Safari alt-hot keys
<td>1.0.1
<td>action.script : 2<br>trigger.hotkey : 3<br>utility.argument : 1
<tr>
<td><img src="./doc/gosafari.png" width="128">
<td><strong>gosafari</strong><br>&nbsp;&nbsp;&nbsp;&nbsp;open list of tabs<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="doc/gosafari.md">Read more...</a>
<td>1.4.0
<td>action.browseinalfred : 1<br>action.script : 2<br>input.keyword : 1<br>input.listfilter : 1<br>input.scriptfilter : 2<br>output.callexternaltrigger : 5<br>output.writefile : 1<br>trigger.external : 5<br>trigger.hotkey : 1<br>utility.argument : 3<br>utility.conditional : 2
<tr>
<td><img src="./doc/mdhelper.png" width="128">
<td><strong>mdhelper</strong><br>&nbsp;&nbsp;&nbsp;&nbsp;Markdown Helper
<td>1.0.2
<td>action.script : 1<br>input.listfilter : 1<br>output.clipboard : 1<br>trigger.hotkey : 4<br>trigger.universalaction : 1<br>utility.argument : 4<br>utility.junction : 1
<tr>
<td><img src="./doc/TMUX.png" width="128">
<td><strong>TMUX</strong><br>&nbsp;&nbsp;&nbsp;&nbsp;Attach to TMUX<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="doc/TMUX.md">Read more...</a>
<td>1.0.2
<td>action.applescript : 1<br>action.script : 1<br>action.terminalcommand : 1<br>input.keyword : 1<br>utility.conditional : 1
<tr>
<td><img src="./doc/unmount.png" width="128">
<td><strong>unmount</strong><br>&nbsp;&nbsp;&nbsp;&nbsp;unmount<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="doc/unmount.md">Read more...</a>
<td>1.2.0
<td>action.script : 3<br>input.scriptfilter : 2<br>output.largetype : 1<br>output.notification : 1
<tr>
<td><img src="./doc/vimtool.png" width="128">
<td><strong>vimtool</strong><br>&nbsp;&nbsp;&nbsp;&nbsp;Start vim as File Action, Universal Text Action or with Keyword in Terminal
<td>1.2.3
<td>action.script : 2<br>action.terminalcommand : 2<br>input.keyword : 1<br>output.clipboard : 1<br>trigger.action : 1<br>trigger.universalaction : 1</table>


## Installation

After download of `file'.alfredworkflow do a fearless doubleclick. Alfred will open it and ask to install it.
