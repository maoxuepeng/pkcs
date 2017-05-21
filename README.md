# PKCS 证书工具
PKCS证书工具可以生成自签名的CA，并使用CA签发证书。
如今网络上绝大部分通信都是使用SSL安全协议，证书是SSL协议的基础，初始接触证书的程序员会有些茫然，之前在[运维派](www.yunweipai.com)写过[关于如何生成证书的文章](http://www.yunweipai.com/archives/4513.html)，考虑到文字再多也不如几行代码来的实在，所以就写了这个工具，有需要的人可以获取使用。

## 获取方式
1. 克隆源代码
2. `sudo pip install pkcs` 安装后使用

## 使用方法
安装之后提供 `pkcs` 命令， `pkcs` 命令有两个子命令
1. `pkcs ca` 生成CA
2. `pkcs cert` 使用CA签发证书

### pkcs ca

```
usage: pkcs ca [-h] [-root CAROOT] [-len LEN] [-c C] [-st ST] [-l L] [-o O]
               [-ou OU] [-cn CN]

pkcs tool set

optional arguments:
  -h, --help            show this help message and exit
  -root CAROOT, --ca-root CAROOT
                        ca output path
  -len LEN, --key-len LEN
                        ca key length
  -c C, --country C     country name in subject
  -st ST, --state ST    state or province name in subject
  -l L, --locality L    locality name in subject
  -o O, --organization O
                        organization name in subject
  -ou OU, --organization-unit OU
                        organization unit name in subject
  -cn CN, --common-name CN
                        common name in subject
```

- -root: CA的根路径，默认为 ~/pkcs/ca，可选
- -len: 私钥的长度，默认为 4096，可选
- -c: X509 规范中的证书主体所属国家名称，默认为 CN，可选
- -st: X509 规范中的证书主体所属省名称，默认为 GuangDong，可选
- -l: X509 规范中的证书主体所属市名称，默认为 ShenZhen，可选
- -o: X509 规范中的证书主体所属组织名称，默认为 YunWeiPai，可选
- -ou: X509 规范中的主体所属组织单元（部门）名称，默认为 YunWeiPai，可选
- -cn: X509 规范中的主体名称，默认为 YunWeiPai-CA，可选

### pkcs cert

```
usage: pkcs cert [-h] [-ca-key CAKEY] [-ca-cert CACERT] [-ca-conf CACONF]
                 [-cert-out CERTOUT] [-len LEN] [-c C] [-st ST] [-l L] [-o O]
                 [-ou OU] [-cn CN]

pkcs tool set

optional arguments:
  -h, --help            show this help message and exit
  -ca-key CAKEY, --ca-key CAKEY
                        ca key for sign cert
  -ca-cert CACERT, --ca-cert CACERT
                        ca cert for sign cert
  -ca-conf CACONF, --ca-conf CACONF
                        ca openssl.conf file path
  -cert-out CERTOUT, --cert-out CERTOUT
                        cert output path
  -len LEN, --key-len LEN
                        ca key length
  -c C, --country C     country name in subject
  -st ST, --state ST    state or province name in subject
  -l L, --locality L    locality name in subject
  -o O, --organization O
                        organization name in subject
  -ou OU, --organization-unit OU
                        organization unit name in subject
  -cn CN, --common-name CN
                        common name in subject
```

- -ca-key: CA私钥绝对路径，必选
- -ca-cert: CA证书绝对路径，必选
- -ca-conf: CA的openssl.conf文件绝对路径，必选
- -cert-out: 签发证书输出路径，默认为 ~/pkcs/cert，可选
- -len: 私钥的长度，默认为 4096，可选
- -c: X509 规范中的证书主体所属国家名称，默认为 CN，可选；必须与CA的值保持一致
- -st: X509 规范中的证书主体所属省名称，默认为 GuangDong，可选；必须与CA的值保持一致
- -l: X509 规范中的证书主体所属市名称，默认为 ShenZhen，可选；必须与CA的值保持一致
- -o: X509 规范中的证书主体所属组织名称，默认为 YunWeiPai，可选；必须与CA的值保持一致
- -ou: X509 规范中的主体所属组织单元（部门）名称，默认为 YunWeiPai，可选
- -cn: X509 规范中的主体名称，默认为 YunWeiPai，可选