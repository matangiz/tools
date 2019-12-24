Roof Of Factories CLI Tool
======================================================

## Basic Usage
Directories structure under secure_factory_latest.tar downloaded file:

```
<secure_factory_latest.tar>
├── rof
│   ├── src
│   ├── hsm-luna
│   ├── hsm-db
│   └── version.properties
│   └── docker-compose.yml
│   └── rof.py
├── workstation
└── prod
└── docs
```

The root of factories services are dependent on secure-room running database and therfore you need to set the `FACTORY_HOME_DIR`

## Usage

This section describes detailed usages for each operation.
* [Start](#Starts-root-of-factories-services)
* [Create](#Creates-root-of-factories-certificate-authority)
* [Sign](#Creates-signed-certificate-using-roof-of-factory-certificate)
* [Stop](#Stops-root-of-factories-services)
* [Status](#Outputs-status-of-the-roof-of-factories-services)



### Starts root of factories services

When running root of factories services for the fiest time you are required to configure basic authentication username and password.


```
$ python3 rof.py start --username exampleUser --password 12345678

==================================================
Root Of Factories
==================================================
Crating basic auth env file
Generating JWT credentials for rof-hsm-service
Creating network "pelion_root_of_factories_default" with the default driver
Creating rof-hsm-db.postgres ... done
Creating root-of-factories   ... done
Creating rof-hsm-service     ... done

```
 You can check the root of factories services status using the [Status](#Outputs-status-of-the-roof-of-factories-services) command



###  Creates root of factories certificate authority

```
$ python3 rof.py create --company ExampleCompany

==================================================
Root Of Factories
==================================================
Please enter UI username:
exampleUser
Please enter UI password:
12345678
User: exampleUser Authenticated successfully

ROF certificate authority created successfully

-----BEGIN CERTIFICATE-----
MIIBwzCCAWmgAwIBAgIQRj+YZC6ySd+VuhJ2iYXJ/zAKBggqhkjOPQQDAjA5MR4w
HAYDVQQDDBVQZWxpb25Sb290T2ZGYWN0b3JpZXMxFzAVBgNVBAoMDkV4YW1wbGVD
b21wYW55MB4XDTE5MTIxOTA5MzYyMloXDTQ5MTIxOTA5MzYyMlowOTEeMBwGA1UE
AwwVUGVsaW9uUm9vdE9mRmFjdG9yaWVzMRcwFQYDVQQKDA5FeGFtcGxlQ29tcGFu
eTBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABG5BltxEhbYhYO3SEkb4ExJLdpKY
kqFMJFV3wGvwBIo8rco+7srolKKFLfOe+3v/wuGAMwgnWmGv9iFCNgOp5AKjUzBR
MB8GA1UdIwQYMBaAFNh+Jau5Ce26ECWfrXczRKGMPyv4MB0GA1UdDgQWBBTYfiWr
uQntuhAln613M0ShjD8r+DAPBgNVHRMBAf8EBTADAQH/MAoGCCqGSM49BAMCA0gA
MEUCIAGAHYq0oxo+9jUN96726rhce2FFkwvfKofFbvWYVptZAiEA4BFxeio9WnsJ
qMaHO/Nv/8vbu8vY1VwDeMkgeYWSKvg=
-----END CERTIFICATE-----

```

You can use the `-o` or `--output` argument to write roof of factories certificate to specific file
Note that you can use the --username and --password argument for authentication instead of the user input


### Creates signed certificate using roof of factory certificate


```
$ python3 rof.py sign --csr csr.pem

==================================================
Root Of Factories
==================================================
Please enter UI username:
exampleUser
Please enter UI password:
12345678
User: exampleUser Authenticated successfully

CSR Signed successfully by root of factories

Root of factories CA certificate:

-----BEGIN CERTIFICATE-----
MIIB7zCCAZagAwIBAgIRAP4frk13zkS1l8rzIOL9UpYwCgYIKoZIzj0EAwIwOTEe
MBwGA1UEAwwVUGVsaW9uUm9vdE9mRmFjdG9yaWVzMRcwFQYDVQQKDA5FeGFtcGxl
Q29tcGFueTAeFw0xOTEyMTkwOTQwMzdaFw00OTEyMTkwOTM2MjJaMGUxFDASBgNV
BAMMC2ZhY3RvcnktMjM1MQwwCgYDVQQKDANBUk0xETAPBgNVBAsMCEFSTV9VTklU
MRIwEAYDVQQHDAlURVNUX0NJVFkxCzAJBgNVBAgMAlNUMQswCQYDVQQGEwJJTDBZ
MBMGByqGSM49AgEGCCqGSM49AwEHA0IABNj7GD1n8f+FEz/fRcdhGJDB38d8qZW4
77hyRHw84EeB3g+RRGQATyjeMwybxF3ynEbtkDYtt5u+6BnpyCJfNTSjUzBRMB8G
A1UdIwQYMBaAFNh+Jau5Ce26ECWfrXczRKGMPyv4MB0GA1UdDgQWBBTKwkBJq4sc
HoPDEfC/wcGsrY6eITAPBgNVHRMBAf8EBTADAQH/MAoGCCqGSM49BAMCA0cAMEQC
IDh77PXOi0fX+b25YkhZILXi7l1dqUhid1Msib6fcWCHAiBmtkgRXalcTfMQrvRr
xw5vvVxnow3/NVGbPYrxqRuFHA==
-----END CERTIFICATE-----

Factory certificate:

-----BEGIN CERTIFICATE-----
MIIBwzCCAWmgAwIBAgIQRj+YZC6ySd+VuhJ2iYXJ/zAKBggqhkjOPQQDAjA5MR4w
HAYDVQQDDBVQZWxpb25Sb290T2ZGYWN0b3JpZXMxFzAVBgNVBAoMDkV4YW1wbGVD
b21wYW55MB4XDTE5MTIxOTA5MzYyMloXDTQ5MTIxOTA5MzYyMlowOTEeMBwGA1UE
AwwVUGVsaW9uUm9vdE9mRmFjdG9yaWVzMRcwFQYDVQQKDA5FeGFtcGxlQ29tcGFu
eTBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABG5BltxEhbYhYO3SEkb4ExJLdpKY
kqFMJFV3wGvwBIo8rco+7srolKKFLfOe+3v/wuGAMwgnWmGv9iFCNgOp5AKjUzBR
MB8GA1UdIwQYMBaAFNh+Jau5Ce26ECWfrXczRKGMPyv4MB0GA1UdDgQWBBTYfiWr
uQntuhAln613M0ShjD8r+DAPBgNVHRMBAf8EBTADAQH/MAoGCCqGSM49BAMCA0gA
MEUCIAGAHYq0oxo+9jUN96726rhce2FFkwvfKofFbvWYVptZAiEA4BFxeio9WnsJ
qMaHO/Nv/8vbu8vY1VwDeMkgeYWSKvg=
-----END CERTIFICATE-----

```

You can use the `-o` or `--output` argument to write roof of factories certificate to specific file
Note that you can use the --username and --password argument for authentication instead of the user input



### Stops root of factories services


```
$ python3 rof.py stop

==================================================
Root Of Factories
==================================================
Stopping root-of-factories
Stopping rof-hsm-service     ... done
Stopping root-of-factories   ... done
Stopping rof-hsm-db.postgres ... done
Removing rof-hsm-service     ... done
Removing root-of-factories   ... done
Removing rof-hsm-db.postgres ... done
Removing network pelion_root_of_factories_default


```



### Outputs status of the roof of factories services

```
$ python3 rof.py status

==================================================
Root Of Factories
==================================================
Secure-factory installed under:
        /usr/local/arm/secure_factory
Secure-factory docker containers:
  Factory tool service status:
        version: 2019.12.848
        status: healthy

  Hsm client service:
        version: 398
        status: healthy

Basic authentication:
        username: exampleUser
        password: ********

```
