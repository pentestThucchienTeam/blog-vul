## Overview  
Chức năng `preview` cho ta xem các bài post đã load lên nhưng chưa được admin duyệt. Để ý đường link, ta nhận thấy nó nhận giá trị là ID của bài post  
![image](https://user-images.githubusercontent.com/22276823/132520737-fd6e1ff4-fa08-4b16-a805-cf84641aabcf.png)  
![image](https://user-images.githubusercontent.com/22276823/132520877-54336061-6882-4613-bbf0-89babaa8cb76.png)  

Thử thay đổi bằng các ID không có trong danh sách. VD ở đây là 15  

![image](https://user-images.githubusercontent.com/22276823/132521004-f2747701-52a0-4366-bfe0-314b04c7c40b.png)  

Ứng dụng vẫn trả về kết quả bình thường. Có thể kết luận ứng dụng đã bị lỗ hổng IDOR, cho phép attacker xem được các bài post đang `pending` của user khác


