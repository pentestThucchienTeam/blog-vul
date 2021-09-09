# Path traversal

Observing the URL of the avatar image in the Profile folder, we see that this image is displayed by calling the name of the image directly in the folder. Because of this, I think of a possible vulnerability that is Path Traversal
![image](https://user-images.githubusercontent.com/63194321/132466602-3bee35bd-62d8-4ab1-b019-ec828afa44f3.png)


### Solution

I will use Burp Suite to make the job easy

B1. We use Burp Suite to intercept the request to get the avatar image in the Profile section and send it to the Burp Repeater.  
![image](https://user-images.githubusercontent.com/63194321/132466638-cdd3d4df-b4a4-475a-b9a1-0f884eab281e.png)

B2. We will change the value of the variable "images" instead of returning the name of an image, we can return an arbitrary path. (Depending on how the directory is arranged, the directory path may be different.) 
 ![image](https://user-images.githubusercontent.com/63194321/132466676-c4475297-48d7-4491-b214-c8be26e99ec0.png)

Observe that the returned result is not an image file anymore, but instead will be a result of the etc/passwd file.

Exploit

Once we have identified this as a Path Traversal vulnerability, we can use payloads depending on the backend to deploy appropriately. We can access and read the data depending on the operating system as follows.

#### •	Linux:

`/etc/issue`

`/etc/passwd`

`/etc/mysql/my.cnf`

`/proc/net/tcp`

`/home/$USER/.bash_history`

`/home/$USER/.ssh/id_rsa`

`/run/secrets/kubernetes.io/serviceaccount/certificate`

`/var/run/secrets/kubernetes.io/serviceaccount`

#### •	Windows

`c:/boot.ini`

`c:/inetpub/logs/logfiles`

`c:/inetpub/wwwroot/global.asa`

`c:/sysprep.inf`

`c:/sysprep.xml`

`c:/system volume information/wpsettings.dat`

`c:/system32/inetsrv/metabase.xml`

`c:/unattend.txt`

`c:/windows/repair/sam`

`c:/windows/repair/system`

Besides, the following log files are controllable and can be included with an evil payload to achieve a command execution

`/var/log/apache/access.log`

`/var/log/apache/error.log`

`/var/log/httpd/error_log`

`/usr/local/apache/log/error_log`

`/usr/local/apache2/log/error_log`

`/var/log/vsftpd.log`

`/var/log/sshd.log`

`/var/log/mail`

Reference
•	https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Directory%20Traversa
