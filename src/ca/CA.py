#!/usr/bin/env python
# coding=utf8

import os

GEN_CA_KEY = 'openssl genrsa -aes128 -passout pass:%(caPass)s 4096 > %(caKeyFile)s'

GEN_CA_REQ = 'openssl req -new -key %(caKeyFile)s -passin pass:%(caPass)s -config %(opensslConfFile)s -subj "/C=CN/ST=GuangDong/L=ShenZhen/O=UProject/OU=UProject/CN=UProject-CA" -batch -out %(caCsrFile)s'

SIGN_CA = 'openssl ca -config %(opensslConfFile)s -create_serial -out %(caCertFile)s -days 365 -keyfile %(caKeyFile)s -key %(caPass)s -selfsign -in %(caCsrFile)s'


class CA:
    def __init__(self, caPass, caRoot, opensslConfFile):
        self.caPass = caPass
        self.caKeyFile = os.path.join(caRoot, 'ca_key.pem')
        self.caCsrFile = os.path.join(caRoot, 'ca_csr.pem')
        self.caCertFile = os.path.join(caRoot, 'ca_cert.pem')
        self.opensslConfFile = os.path.join(os.getenv('APP_ROOT'), 'etc/openssl.conf')

    def generateKey(self):
        pass

    def generateCSR(self):
        pass

    def selfSign(self):
        pass
