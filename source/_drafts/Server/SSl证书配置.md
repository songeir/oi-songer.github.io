---
title: "SSl证书配置"
tags: 
---

# SSl证书配置

> 最近突然想要给自己的网站配置上ssl证书，今天上网搜了一下，打算先尝试一下Let's Encrypt的免费证书。

<!--more-->

参考网站:

---

在这里，我打算使用官方推荐的[_certbot_](https://certbot.eff.org/)来安装ssl服务。

### 1.安装
安装之前，需要先启用EPEL(Extra Packages for Enterprise Linux)源，我的服务器已经启用了，这里不需要再次输入。命令如下：
```bash
yum install epel-release
```
然后，我们便可以安装certbot了
```bash
yum install certbot-nginx
```

### 2.开始配置
Certbot有一个Nginx的插件，支持许多平台，并且可以自动获取和安装证书:
```bash
sudo certbot --nginx
```
结果因为nginx的配置文件不在默认位置，certbot无法找到(我的锅。。。)，所以我们只能手动安装。
```bash
sudo certbot certonly
```
打开后，选择3，使用文件验证，然后输入网页所在目录。

运行完后，显示证书已存在`/etc/letsencrypt/live/songer.xyz/fullchain.pem`

### 3.自动更新
因为let's encrypt的证书只有90天期限，所以我们可以使用自动更新策略：
```bash
sudo certbot renew --dry-run
```
### 4.Nginx配置
> 已尝试一次，失败

> 感到绝望（；´д｀）ゞ

更改过的配置文件存在了`nginx.conf.bad`，未删除。

