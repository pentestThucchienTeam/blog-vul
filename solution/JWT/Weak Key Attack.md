# Weak Key Attack

After you log in with your account go to the `settings` page where you can edit anything then submit the form. You will receive a message `You don't have permits`.

![image](https://user-images.githubusercontent.com/63194321/133216016-5ddb08c8-6180-436d-8161-541659293121.png)

Check the cookie. You can see `auth` with value in JWT format.

![image](https://user-images.githubusercontent.com/63194321/132486535-0431fdc5-4791-4b69-b16d-0e7a24f653ae.png)

#### Decode `JWT` values

![image](https://user-images.githubusercontent.com/63194321/132480432-00f13ddc-2e19-46b1-bfab-a7ec492fb86c.png)

The JWT uses the `HS256` algorithm with the payload having the `admin:false` field to verify the user's permissions. Somehow change to `true` to elevate to admin

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


