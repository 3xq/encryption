# encryption
&nbsp;&nbsp;&nbsp;&nbsp;a simple encryption algorithm coded in python,
&nbsp;&nbsp;&nbsp;&nbsp;that only uses preinstalled python modules.

&nbsp;&nbsp;&nbsp;&nbsp;generating the same thing with the same password  
&nbsp;&nbsp;&nbsp;&nbsp;will result in different responses each time that will  
&nbsp;&nbsp;&nbsp;&nbsp;decode to the same thing.  

## usage

**main.py** > **encrypt(string, password)**:  
&nbsp;&nbsp;&nbsp;&nbsp;**input**: ``hello, world``   
&nbsp;&nbsp;&nbsp;&nbsp;**output 1**: ``FE1N731KFE1IC31G3B2G241MFE1O831O341V393``  
&nbsp;&nbsp;&nbsp;&nbsp;**output 2**: ``D02L731GFE1NC31K241KD02K831M341V535``  

   same arguments will yield different reponses  
   if generated more than once as said before.  
  
**main.py** > **decrypt(string, password)**:  
&nbsp;&nbsp;&nbsp;&nbsp;**input**: ``FE1N731KFE1IC31G3B2G241MFE1O831O341V393, world``  
&nbsp;&nbsp;&nbsp;&nbsp;**output**: ``hello``  
    
&nbsp;&nbsp;&nbsp;&nbsp;**input**: ``D02L731GFE1NC31K241KD02K831M341V535, world``  
&nbsp;&nbsp;&nbsp;&nbsp;**output**: ``hello``  
  
&nbsp;&nbsp;&nbsp;&nbsp;if the wrong password is entered it will output  
&nbsp;&nbsp;&nbsp;&nbsp;a random heap of characters depending on how long  
&nbsp;&nbsp;&nbsp;&nbsp;your encryption string was.  
    
&nbsp;&nbsp;&nbsp;&nbsp;**input**: ``FE1N731KFE1IC31G3B2G241MFE1O831O341V393, wrodl``  
&nbsp;&nbsp;&nbsp;&nbsp;**output**: `` `Zgl_  ``
  
### happy encrypting :^)
