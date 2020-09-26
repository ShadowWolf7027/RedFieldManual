# Password Attacks

## Hashcat
### Attack Modes
`-a` flag

| Type  | ID  | Description |
|---|---|---|
| Dictionary  | 0  | Generate hashes from a text file to compare |
| Combination  | 1  | Uses two dictionaries |
| Mask  | 3  | Brute force all characters specified |
| Hybrid | 6 or 7 | Dictionary and mask attack |

### Wordlists
Common wordlists to use
* [Seclists](https://github.com/danielmiessler/SecLists)
* [Rockyou](https://wiki.skullsecurity.org/Passwords)
    * Maybe already on your system if using Kali or Parrot
        * Locate rockyou
* [Crunch](https://tools.kali.org/password-attacks/crunch)


#### Brute Force
```
?l = abcdefghijklmnopqrstuvwxyz
?u = ABCDEFGHIJKLMNOPQRSTUVWXYZ
?d = 0123456789
?s = «space»!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
?a = ?l?u?d?s
?b = 0x00 - 0xff
```
?l?d is the same as `abcdefghijklmnopqrstuvwxyz0123456789`

Each ? indicates a character lenght (i.e. ?l?l?l tests all lowercase combinations up to a length of 3)

### Examples
#### Dictionary Attack
```
hashcat -a 0 -m 0 md5_hashes.txt password_list.txt
```
#### Combination attack
```
hashcat -a 1 -m 0 md5_hashes.txt password_list.txt password_list_2.txt -k "$!"
```
`-k` adds the specified character at the end of each word for that file
#### Mask Attack
```
hashcat -a 3 -m 0 md5_hashes.txt ?u?l?l?l?d?d?d?d
```
#### Hybrid Attack
```
hashcat -a 6 -m 0 md5_hashes.txt password_list.txt ?d?d?d?d
```


## John
Crack password
```
john hash_file -w=WORDLIST
```

Show password once cracked
```
john hash_file --show
```

## Common Hashes
*Obtained from Hashcat's documentation click [here](https://hashcat.net/wiki/doku.php?id=example_hashes) for the full list*

`-m` flag for hashcat

### Linux
| ID   | Name  | Example |
|------|-----|------------- |
| 500  | md5crypt | $1$28772684$iEwNOgGugqO9.bIz5sk8k/ |
| 3200 | bcrypt, Blowfish(Unix)    | $2a$05$LhayLxezLhK1LhWvKxCyLOj0j1u.Kj0jZ0pEmm134uzrQlFvQJLF6 |
| 1600 | Apache | $apr1$71850310$gh9m4xcAn3MGxogwX/ztb. |
| 1800 | sha512crypt, SHA512(Unix) | $6$52450745$k5ka2p8bFuSmoVT1tzOyyuaREkkKBcCNqoDKzYiJL9RaE8yMnPgh2XzzF0NDrUhgrcLwg78xs1w5pJiypEdFX/ |

### Windows
| ID   | Name | Example                          |
|------|------|----------------------------------|
| 1000 | NTLM | b4b9b02e6f09a9bd760f388b67351e2b |
| 3000 | LM   | 299bd128c1101fd6                 |

### Database
| ID    | Name | Example |
|-------|------------|----------|
| 12    | PostgreSQL | a6343a68d964ca596d9752250d54bb8a:postgres |
| 131   | MSSQL (2000) | 0x01002702560500000000000000000000000000000000000000008db43dd9b1972a636ad0c7d4b8c515cb8ce46578 |
| 132   | MSSQL (2005)  | 0x010018102152f8f28c8499d8ef263c53f8be369d799f931b2fbe |
| 1731  | MSSQL (2012, 2014) | 0x02000102030434ea1b17802fd95ea6316bd61d2c94622ca3812793e8fb1672487b5c904a45a31b2ab4a78890d563d2fcf5663e46fe797d71550494be50cf4915d3f4d55ec375 |
| 200   | MySQL323  | 7196759210defdc0 |
| 300   | MySQL4.1/MySQL5  | fcf7c1b8749cf99d88e5f34271d636178fb5d130 |
| 3100  | Oracle H: Type (Oracle 7+)  | 7A963A529D2E3229:3682427524 |
| 112   | Oracle S: Type (Oracle 11+) | ac5f1e62d21fd0529428b84d42e8955b04966703:38445748184477378130 |
| 12300 | Oracle T: Type (Oracle 12+) | 78281A9C0CF626BD05EFC4F41B515B61D6C4D95A250CD4A605CA0EF97168D670EBCB5673B6F5A2FB9CC4E0C0101E659C0C4E3B9B3BEDA846CD15508E88685A2334141655046766111066420254008225 |

### General
| ID    | Name     | Example |
|-------|----------|---------|
| 900   | MD4      | afe04867ec7a3845145579a95f72eca7 |
| 0     | MD5      | 8743b52063cd84097a65d1633f5c74f5 |
| 5100  | Half MD5 | 8743b52063cd8409 |
| 100   | SHA1     | b89eaac7e61417341b710b727768294d0e6a277b |
| 10800 | SHA-384  | 07371af1ca1fca7c6941d2399f3610f1e392c56c6d73fddffe38f18c430a2817028dae1ef09ac683b62148a2c8757f42 |
| 1400  | SHA-256  | 127e6fbfe24a750e72930c220a8e138275656b8e5d8f48a98c3c92df2caba935 |
| 1700  | SHA-512  | 82a9dda829eb7f8ffe9fbe49e45d47d2dad9664fbb7adf72492e3c81ebd3e29134d9bc12212bf83c6840f10e8246b9db54a4859b7ccd0123d86e5872c1e5082f |
