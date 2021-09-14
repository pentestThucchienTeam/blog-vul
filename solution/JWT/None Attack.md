# None Attack

After you log in with your account go to the `settings` page where you can edit anything then submit the form. You will receive a message `You don't have permits`.

![image](https://user-images.githubusercontent.com/63194321/133215758-de2cf0c3-f2f2-4f01-9886-90212714dbdb.png)

Check the cookies you will see `auth` with a value of 1 code `jwt`

![image](https://user-images.githubusercontent.com/63194321/132473506-9f92487f-0f79-4c5d-9ce4-73d8edb3ec47.png)

#### Decode the `jwt` values.
![image](https://user-images.githubusercontent.com/63194321/132473084-64c2f766-cf71-490c-9c34-6c70b36bfdd1.png)

The JWT uses the `HS256` algorithm with the payload having the `admin:false` field to verify the user's permissions. Somehow change to `true` to elevate to admin

### Solution
 B1. First, after we have the content, we will proceed to edit the algorithm to `alg:none`.Next, change your job title to `admin`
 
 ![image](https://user-images.githubusercontent.com/63194321/132475306-72bb43bc-266b-48aa-9e70-e6a33d436ffd.png)

 B2. Then convert them to JWT with `jwt.io` and remove the signature until the 3rd `.` stops.
 
 ![image](https://user-images.githubusercontent.com/63194321/132475727-b2c7ef02-246a-409d-ada8-5ac15b0c71e5.png)

 B3. Changing the cookie value in the web page with the value we just created is reloaded the page and we can change its values.
 !![image](https://user-images.githubusercontent.com/63194321/132477265-93f0c4d0-f01b-4d37-9736-d493149be6aa.png)


 
 

