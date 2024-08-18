# Pruthvi Shortner
**Free URL Shortener for transforming long, ugly links into nice, memorable and trackable short URLs.**

## Features
- [x] Shorten long URLs.
- [X] User Registration / Authentication.
- [x] User can see all created links, along with link creation date and link clicks.

## ToDo 
- [ ] Ability for user to delete created links.
- [ ] Allow user to create custom short link i.e. alias

### Installation
- Install required modules.
```sh
apt install -y git python3
```
- Clone this git repository.
```sh 
git clone https://github.com/pruthvirajpilliwar/Pruthvi-Shortner
```
- Change Directory
```sh 
cd Pruthvi-Shortner
```
- Install requirements with pip3
```sh 
pip3 install -r requirements.txt
```

### Deploy 
```sh 
gunicorn app:app
```

## Credits
- [Pruthviraj Pilliwar](https://github.com/pruthvirajpilliwar)
- [All the Libraries owner](https://github.com/pruthvirajpilliwar/Pruthvi-Shortner/blob/main/requirements.txt)

## Copyright & License
- Copyright (©) 2024 by [Pruthviraj Pilliwar](https://github.com/pruthvirajpilliwar)
- Licensed under the terms of the [GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007](./LICENSE)
