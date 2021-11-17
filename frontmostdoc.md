# Alfred-Workflow-frontmostdoc
Alfred-Workflow: Show frontmost document's file of frontmost application in Alfred File Action

I build this Workflow to launch Alfred File Action by keyword or keyboard shortcut. This is lot faster than hovering the mouse to the top of a window and do ctrl-click the proxy icon.

## Installation

Open file frontmostdoc.alfredworkflow with [Alfred 4.+](https://www.alfredapp.com)

## Description

<img width="758" alt="Entering workflow keyword aa" src="https://user-images.githubusercontent.com/55148527/124760264-da5ec400-df30-11eb-99c3-eadba0617d29.png">

<img width="623" alt="Alfred's file action menu pops up" src="https://user-images.githubusercontent.com/55148527/124760292-e2b6ff00-df30-11eb-8861-f67cef9a6810.png">

<img width="714" alt="Screenshot" src="https://user-images.githubusercontent.com/55148527/124922579-ea8ea600-dff9-11eb-8772-5e0802aa11ba.png">

In "run script" Apple Script queries the application for the path to the active document window.
Having gotten the path finally "Action in Alfred" for it is scheduled.

In order to work, the active application must
- be scriptable
- be document based
- provide the path to its documents by property named file or path
- have at least one document open

If anything goes wrong, e.g. active App is Affinity Photo (not scriptable) or Safari (not document based), this workflow plays a sound.

It works with Preview, BBEdit, Quicktime Player, Pages, OmniGraffle, OmniOutliner…
