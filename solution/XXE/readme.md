## Detect    
The function creates post by upload xml file at `requestpost`  
    
![image](https://user-images.githubusercontent.com/22276823/133217003-7ec7f9a8-16bc-4ba0-bcce-117156798eea.png)

After upload, we can see the post is listed in list pending post  

![image](https://user-images.githubusercontent.com/22276823/133217127-f580acc1-6d3e-42cf-8715-04c4bb284f2d.png)

We can see the post by click to the post's title  

![image](https://user-images.githubusercontent.com/22276823/133217615-473f3810-35ee-4473-8775-a58dd38f5792.png)
 
 The content of xml file  
  
![image](https://user-images.githubusercontent.com/22276823/132802761-e9e1263f-d921-4fbe-8311-7e106d202982.png)  
  
![image](https://user-images.githubusercontent.com/22276823/132802787-65ca6c48-6750-45cb-9cb8-b74ec60ffbc7.png)  
  
Tính năng này nhận vào một file XML và tiến hành tạo một bài post cơ bản với các thông tin có sẵn trong file. Upload một file gọi external entity để kiểm tra XXE  
payload  
  
![image](https://user-images.githubusercontent.com/22276823/132803026-2756d2cd-4eee-4270-b0e3-3aa46480a86b.png)
  
Kết quả  
  
![image](https://user-images.githubusercontent.com/22276823/132803001-daade2a6-f2d0-48e4-b1cc-2050f55d96b6.png)  




