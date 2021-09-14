## Detect    
The function creates post by upload xml file at `requestpost`  
    
![image](https://user-images.githubusercontent.com/22276823/133217003-7ec7f9a8-16bc-4ba0-bcce-117156798eea.png)

After upload, we can see the post is listed in list pending post  

![image](https://user-images.githubusercontent.com/22276823/133217127-f580acc1-6d3e-42cf-8715-04c4bb284f2d.png)

We can see the post by click to the post's title  

![image](https://user-images.githubusercontent.com/22276823/133217615-473f3810-35ee-4473-8775-a58dd38f5792.png)
 
 The content of xml file  

![image](https://user-images.githubusercontent.com/22276823/133217909-60fcf48d-4153-449b-8821-0e0e331c8d58.png)
  
When I upload the file with specical character  

![image](https://user-images.githubusercontent.com/22276823/133218169-eb47c502-2c2a-4c9f-9157-3223a4f90296.png)  

The server returns 500 error code  

![image](https://user-images.githubusercontent.com/22276823/133218335-3ebad8c1-2b42-4c1a-9a7d-d493c18b032f.png)  
  
Try with another character, the result is just 500 error.  When the content is processed by xml processor, it returns error we don't escape special character  

Try to esacpe character  

![image](https://user-images.githubusercontent.com/22276823/133221464-7b60b8d5-456d-488e-b7d4-df359d796080.png)

![image](https://user-images.githubusercontent.com/22276823/133221517-0a406583-9505-4917-9ade-1a550f6da983.png)  

## Exploit  
Upload the file with DTD declaration  

![image](https://user-images.githubusercontent.com/22276823/133221841-695f7640-51b0-442e-a009-cd72c2a41530.png)  

The payload read `/etc/passwd` and print entity to `content` element  

![image](https://user-images.githubusercontent.com/22276823/133222643-dff32b0b-4121-4ab0-bc77-3c1c5e6e2b6d.png)  




