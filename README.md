# BCI-hack

[![Build Status](https://travis-ci.com/Borda/bci-hack.svg?token=HksCAm7DV2pJNEbsGJH2&branch=master)](https://travis-ci.com/Borda/bci-hack)

## Blinking keyboard

The idea is having liners kaybord and orienting over the keyboard by blinking which appears in the EEG as artifacts. We can set start/stop blink and double blink for a change...

## Data

The can be streamed from the BCI device in following 17 channels, each as float32
**Recorded channels**
* 8 EEG
* 3 ACC
* 3 Gyro
* 1 Battery
* 1 count
* 1 val IO

**Required preprocessing**
* remove the moise caused by electricity - 50Hz, use Notch filter
* band pass filter on 0.5 to 30Hz


## Applications

the basic application for decoding BCI sinal is in apps folder

Minor TODOS:
* real time filtering to speed up the app, now it is filterd by frames
* integrate the event from detection app
* detect blinking