#!/usr/bin/env python
# coding=utf8

caOpensslConf = '''
#http://www.phildev.net/ssl/opensslconf.html
[ ca ]
default_ca = CA_default

[CA_default]
caroot = %(caroot)s
certs       = $caroot/certsdb
new_certs_dir   = $certs
database    = $caroot/index.txt
certificate = $caroot/%(cn)s.cer
private_key = $caroot/%(cn)s-key.pem
serial      = $caroot/serial
#crldir     = $caroot/crl
#crlnumber  = $caroot/crlnumber
#crl        = $crldir/crl.pem
RANDFILE    = $caroot/private/.rand

x509_extensions = usr_cert

#copy_extensions    = copy

name_opt        = ca_default
cert_opt        = ca_default

default_days    = 365
#default_crl_days= 30

default_md      = sha256
preserve        = no

policy          = policy_match

[ policy_match ]
countryName             = match
stateOrProvinceName     = match
localityName            = supplied
organizationName        = match
organizationalUnitName  = optional
commonName              = supplied
emailAddress            = optional

[ policy_anything ]
countryName             = optional
stateOrProvinceName     = optional
localityName            = optional
organizationName        = optional
organizationalUnitName  = optional
commonName              = supplied
emailAddress            = optional

[ req ]
default_bits            = 4096
default_keyfile         = privkey.pem
distinguished_name      = req_distinguished_name
attributes              = req_attributes
x509_extensions     = v3_ca
req_extensions      = v3_req

string_mask = nombstr

[ req_distinguished_name ]
C = %(c)s
ST = %(st)s
L = %(l)s
O = %(o)s
OU = %(ou)s
CN = %(cn)s
#emailAddress = $ENV:REQ_EMAIL

[ req_attributes ]

[ usr_cert ]
basicConstraints = CA:false
subjectKeyIdentifier = hash
authorityKeyIdentifier = keyid,issuer
subjectAltName = $ENV::SUBJECT_ALT_NAME

[ v3_req ]
#subjectAltName = %(subjectAltName)s

[ v3_ca ]
subjectKeyIdentifier=hash
authorityKeyIdentifier=keyid:always,issuer:always
basicConstraints = CA:true
'''

certOpensslConf = '''
#http://www.phildev.net/ssl/opensslconf.html

x509_extensions = usr_cert

#copy_extensions    = copy

default_days    = 365
#default_crl_days= 30

default_md      = sha256
preserve        = no

policy          = policy_match

[ policy_match ]
countryName             = match
stateOrProvinceName     = match
localityName            = supplied
organizationName        = match
organizationalUnitName  = optional
commonName              = supplied
emailAddress            = optional

[ policy_anything ]
countryName             = optional
stateOrProvinceName     = optional
localityName            = optional
organizationName        = optional
organizationalUnitName  = optional
commonName              = supplied
emailAddress            = optional

[ req ]
default_bits            = 4096
default_keyfile         = privkey.pem
distinguished_name      = req_distinguished_name
attributes              = req_attributes
x509_extensions     = v3_req
req_extensions      = v3_req

string_mask = nombstr

[ req_distinguished_name ]
C = %(c)s
ST = %(st)s
L = %(l)s
O = %(o)s
OU = %(ou)s
CN = %(cn)s
#emailAddress = $ENV:REQ_EMAIL

[ req_attributes ]

[ usr_cert ]
basicConstraints = CA:false
subjectKeyIdentifier = hash
authorityKeyIdentifier = keyid,issuer

[ v3_req ]
subjectAltName = %(subjectAltName)s

'''
