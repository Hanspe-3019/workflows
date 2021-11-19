Workflow defines two File Actions to create File in the current directory.

1. _Create in this Folder_  for folders will create file in the selected folder.
2. _Create here_ for data files (public.content) will create file in the current folder.

Script Filter display template files in $templatefolder.
```
	template.`file-extension´
```

$templatefolder is relative to user's home folder.

You can provide corresponding icon file in $templatefolder with
```
    `file-extension´.png.
```

### Example 
Provide template and icon for python file:

```
   template.py
   py.png
```
