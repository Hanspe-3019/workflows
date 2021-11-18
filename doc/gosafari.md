# gosafari: Safari tabgroups implemented as workflow

This workflow let you open group of URLs in Tabs in new Safari window.

![Start workflow](https://user-images.githubusercontent.com/55148527/142421149-ee53af37-d9de-4d43-922a-05d9efbdff42.png)


## Tab Group Files
Each group is represented by a tab group file, a txt-file with the urls in separate lines. Line which starts with # or > is used as title of the group: 

 * __#__ marks it for private browsing, 
 * __>__ marks for normal browsing.

Other lines not starting with 'http' are ignored.

If the tab group file does not contain any url, a new empty safari window will be created.
 
The txt-files are searched 

1. in URLDIR (relative to $HOME or absolute path). You create your own tab group.
2. in Workflow-dir (contains sample file group "Visit Alfred") 

The tab group files are simple txt-files and are editable with any text editor.

You can generate a tab group file by opening some tabs in a Safari window, start this workflow and select the predefined entry Configure.

![Config menu](https://user-images.githubusercontent.com/55148527/142421251-1ad6ec40-25fa-47d1-971e-edd9289f16f4.png)


### Sample tab group file:
````
# Visit Alfred
https://www.alfredapp.com/help/
https://www.alfredforum.com
this line is ignored, because it does not start with http
````


## Installation
[Go here and hit Download](../gosafari.alfredworkflow), then open the file at your mac to install.
Then set URLDIR to a suitable directory.

The Applescript in this workflow uses keystroke from System Events to start a new window in Safari.

 
