# None Attack

Log in with any user account. View cookies of the website, here we see the web authenticated by JWT.
![image](https://user-images.githubusercontent.com/63194321/132473506-9f92487f-0f79-4c5d-9ce4-73d8edb3ec47.png)

And here we have a "Settings" page that needs admin rights to be able to change everything.
![image](https://user-images.githubusercontent.com/63194321/132474580-2add05e1-f9d7-4983-a9dd-22b0063e8ffa.png)


I then take this JWT code to decode and read the contents inside it. We see `alg:HS256` and of course I don't have the secret key. So I came up with one possibility that is `None attack`.

![image](https://user-images.githubusercontent.com/63194321/132473084-64c2f766-cf71-490c-9c34-6c70b36bfdd1.png)

### Solution
 B1. First, after we have the content, we will proceed to edit the algorithm to `alg:none`. Next I will change my job title to `admin`
 
 ![image](https://user-images.githubusercontent.com/63194321/132475306-72bb43bc-266b-48aa-9e70-e6a33d436ffd.png)

 B2. Then I will convert them to JWT with `jwt.io` and remove the signature until the 3rd `.` stop.
 
 ![image](https://user-images.githubusercontent.com/63194321/132475727-b2c7ef02-246a-409d-ada8-5ac15b0c71e5.png)

 B3. Changing the cookie value in the web page with the value we just created is reloaded the page and we can change its values.
 !![image](https://user-images.githubusercontent.com/63194321/132477265-93f0c4d0-f01b-4d37-9736-d493149be6aa.png)


 
 

