<h1 align ="center"> Snoofer</h1>
<img align="left" width="400" height="405" src="https://imgur.com/EMwljPB.png)">


```python
snoofer = "Version 1.0.0"
print snoofer
```
<h2 align="Left"> Description</h2>

Using rockyou.txt or any .txt files with passwords. Using those and filtering them down to uniqe passwords with 8 characters and up with at least one of each a special character and a number. To then search a targeted directory of all the txt and word docx files to find those vulnerable passwords in them. The larger the directory the longer the scan.
<br />
<br />
#### Current File support
```
.txt, .docx, .cfg, .config, .csv
```
<br />

##
#### Requirements
-------------------
- pip install -r requirements.txt
- Python 3.9 - 3.10.2
<br />

#### Setup
-----------------------------
`Subjected to change as new releases come out to optimize these steps`
1. Open snooferfunctions.py and change the directory **line 19 path = (r"C:\leakedpasswords")** This is where you want to throw all your .txt files with passwords you want to search for like rockyou.txt

2. Open Snoofer.py and change the target location where you want to seach **line 4 path2 = (r"C:\Test")** This is where you want it to do the scan.

#### Known Issues
-------------------
When installing pip package <ins>python-docx</ins> it can error out needing legacy. You will have to down grade to 3.10.2 or lower is whel doesnt support yet the latest version of python.
