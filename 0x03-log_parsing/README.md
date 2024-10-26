# Log Parsing

This project involves parsing log files to extract useful information.

## Table of Contents
- [Description](#description)
- [Requirements](#requirements)
- [Examples](#examples)
- [Author](#author)

## Description
The goal of this project is to read and parse log files, then extract and display specific information such as IP addresses, status codes, and more.

## Requirements
- Python 3.x
- Basic understanding of regular expressions

## Examples
Example log file entry:
```
127.0.0.1 - [2023-10-01 12:00:00] "GET /index.html HTTP/1.1" 200 1024
```

Example output:
```
IP Address: 127.0.0.1
Date: 2023-10-01 12:00:00
Request: GET /index.html HTTP/1.1
Status Code: 200
Size: 1024 bytes
```

## Author
Sandy O.
- GitHub: [your_username](https://github.com/carrier-pigeon-san)
- Email: obaresandy@gmail.com