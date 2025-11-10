# Imgcon
A Command line image format converter for common file types for windows.

It uses Pillow under the hood.

Currently Supported file types

- png
- jpg/jpeg
- webp

## Navigation

- ### [How to install](#how-to-install-1)
- ### [How to use](#how-to-use-1)



## How to install

Download imgcon.zip from the [releases](https://github.com/Zap-09/Imgcon/releases) page.

Unzip it where you don't need admin privileges. Put it somewhere like D:/your folder/imgcon.exe

Copy the path where you put the file. Example D:/your folder. And add it to the PATH in your System Environment Variables.

If you don't know how to add to PATH in System Environment Variables
<details>
 <summary>Click here</summary>
 1. <img src="Assets/Images/guide_1.jpg">
 <br>
 2. <img src="Assets/Images/guide_2.jpg">
 <br>
 3. <img src="Assets/Images/guide_3.jpg">
 <br>
 4. <img src="Assets/Images/guide_4.jpg">
 <br>
 5. <img src="Assets/Images/guide_5.jpg">
 <br>
 6. <img src="Assets/Images/guide_6.jpg">
 <br>


</details> 

## How to use

Open command prompt and cd into your folder where you have your images that you want to convert.

Then type

` imgcon -i your_file_name -e png -o converted  `

Here the 3 arguments are 
- -i is for input
- -e is for the extension you want to convert to
- -o is for the output folder

You can also do ender a folder like this

`imgcon -d "path_to_your/folder" -e webp -o converted`
<br>

-d flag will find all the files ending with png, jpg, jpeg and webp.<br> It will also look for images in the sub folders as well. <br>

You can also enter the current folder with -d flag with "/".<br> Example:

`imgcon -d "/" -e png `

It will find all the images in the current folder and subfolder too.

If -o was not given the files will be saved where the script was run from.

-o argument folder doesn't need to already exist. As long as the entered folder name is valid, it will make these folder.
<br>

There are other flags for different type of image format use "--help" for more info.

Note: If your file has space in the file name you need to surround it with double quotes.<br>Example : 
` imgcon -i "your file name" -e png -o "converted folder" `<br>
<br>

## Todo
### Stuff I want to add in the future

- Add a filter to include and exclude file type when batch conversion

- Add a settings config. Currently all default values are hardcoded.
- Add the option only to get images from the selected folder and not subfolders 

- Want to add more file types and functions