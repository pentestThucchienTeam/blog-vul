# Weak Key Attack

Log in with any user account. View cookies of the website, here we see the web authenticated by JWT.
![image](https://user-images.githubusercontent.com/63194321/132486535-0431fdc5-4791-4b69-b16d-0e7a24f653ae.png)

And here we have a "Settings" page that needs admin rights to be able to change everything.
![image](https://user-images.githubusercontent.com/63194321/132480298-0eb24f61-6abf-4320-9b45-5261255af4bd.png)

Then get this JWT code to decode and read the contents inside it. Noticed the `alg:HS256` and of course no secret key. We will proceed to crack the Key if the developer sets the key is not strong enough
![image](https://user-images.githubusercontent.com/63194321/132480432-00f13ddc-2e19-46b1-bfab-a7ec492fb86c.png)
### Solution
Our essential tool is `jwt_tool` (Install: https://github.com/ticarpi/jwt_tool)

B1. We will copy the JWT in the website cookie and open the downloaded jwt_tool and run it with the command:

`python3 jwi_tool.py <jwt_token> -C -d <file dictionary>`

![image](https://user-images.githubusercontent.com/63194321/132486811-509e0483-05ed-4227-a129-549117911fa6.png)

B2. After we have cracked the key, we will use the command:

`python3 jwi_tool.py <jwt_token> -S hs256 -p "<key>" -I -pc admin -pv True`

![image](https://user-images.githubusercontent.com/63194321/132487588-31efc701-693a-4a9a-bedf-6a1cb2e4b6a0.png)

B3. Use the JWT code just generated replace the value in the page reload cookie and enjoy `admin`
![image](https://user-images.githubusercontent.com/63194321/132487954-bf7bce63-5c9b-4224-8c26-d8d37c0688bb.png)


