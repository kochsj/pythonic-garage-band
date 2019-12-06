# Madlib CLI Game

**Author**: Stephen Koch
**Version**: 1.0.0

## Overview
Have you ever wanted to start a band? Or maybe get the band back together? This file set is defining a set of classes and subclasses that allow the user to create a "Band"! Hense the title "Pythonic Garage Band".

## Getting Started

First, make sure that you have python3 installed:
```
$ python3 --version
Python 3.7.5
```
If you do not:
```
$ brew install python
```
You need to have the files locally. Click on the green clone or download button and Download ZIP:

![Click_to_download](/assets/Click_to_download_x6c0g16lz.png)


In your command line, navigate to this directory:
```
$ cd ~  ##this is your root directory
$ cd Downloads  ##by default: Downloads is a directory inside of your root; and where your file will be downloaded
$ cd pythonic-garage-band ##and now you are in this directory
```
This module is running tests on given data imputs. Install [pytest](https://docs.pytest.org/en/latest/getting-started.html) to get started:
Installing pytest:
```
$ pip install -U pytest
```
Running tests:
```
$ pytest
```
## Functionality/Architecture
The garage_band file has Band, Musician, Singer, Bassist, Guitarist, Drummer, format_data_for_bands classes and methods.
Creating a new instance of Band is as simple as invoking Band with two parameters, the band's name, and a list of the band's members.
It is important for the functionality that the list of band members **must be a list**. Even if there is only one member.
Assigining a new instance of a musician can also be done by using subclasses -- what instrument do they play? New instances can be created for Guitarist, Bassist, Singer, or Drummer at the moment.
For example, A guitarist can be assigned by invoking Guitarist with two parameters, artist_name and band_name.

## Change Log
Thu Dec 05 2019 23:45:10<br>Added functionality to create instances of a band and instances of musicians.

