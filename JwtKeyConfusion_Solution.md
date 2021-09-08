# JWT - RSA Key Confusion Attack

## Solution

Resgister an account and access the [Setting Page](https://blog-vul.herokuapp.com/setting/). Then carry out submit the form below, I receive an notification.

` You don't have permission`

![image](https://user-images.githubusercontent.com/83699106/132470059-2e1ac5e9-b39f-4f94-a58d-e5ba714d67d3.png)

Check the cookie. You can see `auth` with value in JWT format.

![image](https://user-images.githubusercontent.com/83699106/132470786-35fbd491-bdd8-4b66-8a0c-f1c9f9f62fd4.png)

### Decode the auth's value 

![image](https://user-images.githubusercontent.com/83699106/132471583-7e028d69-55e9-4b72-9c7b-efe4dd7557be.png)

The JWT is using RS256 algorithm to verify the token with public key is directly embedded in `publickey`.
It contain two field `admin :false` to consider permission of user. So you must change it into `true` to privilege escalation to admin.

__*Use [jwt_tool](https://github.com/ticarpi/jwt_tool) to check whether it vulnerable*__

### Step 1. Copy the value of public key and save it in file name ` public.key `

![image](https://user-images.githubusercontent.com/83699106/132473838-8c0d1faa-2933-4b57-9d7a-fc311708c122.png)

__Attention__: Public key format end with a newline

### Step 2. Generate a new JWT with jwt_tool.

__command__: 

```
$ python3 jwt_tool.py JWT_HERE -X k -pk public.key 
-X : Exploit
k: Key Confusion mode
-pk: specific the publickey.

More information: $ python3 jwt_tool.py --help

```

![image](https://user-images.githubusercontent.com/83699106/132474574-2205cbaa-3bb2-43ff-898d-055e64e29329.png)

Replace it into old token and submit form again.

![image](https://user-images.githubusercontent.com/83699106/132476453-a6bdb530-a975-4940-a4a3-8e52f5a97f14.png)

*it still don't have per but the token was accept because the tool only change the algorithm from RS256 to HS256 and sign it by Public Key without 
change the `admin`*

### Change your permission into admin and generate new token again.

Change `admin` to True.

![image](https://user-images.githubusercontent.com/83699106/132477345-ce7ad964-3e83-4cc2-be62-d5309aa169bd.png)

Replace old payload section.

![image](https://user-images.githubusercontent.com/83699106/132479268-9b3b1c9d-6d7b-41d3-9a32-bc22b307ac67.png)

Replace old JWT with new own JWTand submit

![image](https://user-images.githubusercontent.com/83699106/132479179-d79ab5fc-8888-4cd9-930c-d3535b8e48a0.png)

Successfully, Happy hacking!
 
