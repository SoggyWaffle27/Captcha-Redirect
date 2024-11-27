**Usage:**

Name_Set:
- INPUT: Folder where you add inputs
  - Inputs should be a folder named after what you want the captcha test to say.
     - The format will look like this: 'Please click on all instances of sandwiches
       - EX: Folder: "cars__" --> 'Please click on all instances of cars'
     - Note: all instances of "_" in the folder name will be replaced with a space. This is to let multiple folders have the same name, while keeping the same message
     - after run, all folders will still be in input, but each will have their images named image1 --> image9, required for code to work

Image_Splitter:
- takes input images in INPUT, outputs a folder with that image(s) split into 9 parts

Folder_Names.py:
