## Overview  
Tại page `requestpost`. Blog cung cấp 2 kiểu tạo post là crawl từ URL hoặc upload file XML. Với loại crawl URL, khi submit một đường link có trong danh sách nó sẽ crawl nội dung 
của blog và tạo thành một post mới. Post này sẽ nằm trong chế độ `pending`. Khi admin duyệt sẽ chuyển thành `active`  
![image](https://user-images.githubusercontent.com/22276823/132515793-b9c66c59-fab3-4219-9ed9-f1bd41a0de1f.png)  
Khi thay đổi gọi vào chính nó thì báo lỗi. Tuy nhiên trang web vẫn được tạo ra  
![image](https://user-images.githubusercontent.com/22276823/132802119-713b00a7-d979-4a54-9389-552fb8baa6ac.png)  
![image](https://user-images.githubusercontent.com/22276823/132802168-010b89c8-466b-4dd2-850c-c8ad1c3611f5.png)  

Như vậy, ứng dụng vẫn cho phép gọi về chính nó, tuy nhiên có thể vì quá trình xử lý ở backend xử lý đúng theo định dạng nên bị báo lỗi. Tuy nhiên với việc không lọc các URL gọi ngược về chính nó có thể tạo ra lỗ hổng SSRF


