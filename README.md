# BCI-hack

[![Build Status](https://travis-ci.org/Borda/BCI-hack.svg?branch=master)](https://travis-ci.org/Borda/BCI-hack)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/13370f2cbed3432c91eda68954f15288)](https://www.codacy.com/app/Borda/BCI-hack?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Borda/BCI-hack&amp;utm_campaign=Badge_Grade)

**Authors:**
Łukasz Skarżyński &
Jan Toman &
Jiri Borovec &
Marcin Matłacz

## Blinking keyboard

The idea is having liners kaybord and orienting over the keyboard by blinking which appears in the EEG as artifacts. We can set start/stop blink and double blink for a change...
Used device Brain-Computer Interface (BCI) from [g.TEch](http://www.gtec.at/).

## Data

The can be streamed from the BCI device in following 17 channels, each as float32.
The repository contains also recording samples of visaul artifacts such as blinking and biting in sequences and blinking by both/left/right eye.

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

### Data processing

The data processing application is decoding BCI signal and sending commands to backend.
The used communication to the BCI devise is [labstreaminglayer](https://github.com/sccn/labstreaminglayer).

Minor TODO:
* real time filtering to speed up the app, now it is filterd by frames
* integrate the event from detection app
* detect blinking

### BackEnd

### FrontEnd
