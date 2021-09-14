## Overview  
BLog có chức năng upload file để tạo post cho phép ta upload một file xml để tạo ra một bài post tại đường dẫn `/requestpost`  
  
![image](https://user-images.githubusercontent.com/22276823/132802693-a174ebd2-ce9a-41d3-b225-d649dc98ec88.png)  
  
Nội dụng file xml  
  
![image](https://user-images.githubusercontent.com/22276823/132802761-e9e1263f-d921-4fbe-8311-7e106d202982.png)  
  
![image](https://user-images.githubusercontent.com/22276823/132802787-65ca6c48-6750-45cb-9cb8-b74ec60ffbc7.png)  
  
Tính năng này nhận vào một file XML và tiến hành tạo một bài post cơ bản với các thông tin có sẵn trong file. Upload một file gọi external entity để kiểm tra XXE  
payload  
  
![image](https://user-images.githubusercontent.com/22276823/132803026-2756d2cd-4eee-4270-b0e3-3aa46480a86b.png)
  
Kết quả  
  
![image](https://user-images.githubusercontent.com/22276823/132803001-daade2a6-f2d0-48e4-b1cc-2050f55d96b6.png)  




