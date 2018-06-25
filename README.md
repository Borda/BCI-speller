# BCI-hack: Mind keyboard

[![Build Status](https://travis-ci.org/Borda/BCI-speller.svg?branch=master)](https://travis-ci.org/Borda/BCI-speller)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/bcd9d6fe109542ddbfa645c1cd9c50fb)](https://www.codacy.com/app/Borda/BCI-speller?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Borda/BCI-speller&amp;utm_campaign=Badge_Grade)

**Authors:**
Jiri Borovec [data processing] &
Łukasz Skarżyński [frontend/backend] &
Jan Toman [design] &
Marcin Matłacz [frontend/backend]

The idea is having liners kaybord and orienting over the keyboard by blinking which appears in the EEG as artifacts. We can set start/stop blink and double blink for a change...
Used device [Brain-Computer Interface](http://www.br41n.io) (BCI) from [g.TEch](http://www.gtec.at/).
See [Writing-with-our-mind](https://devpost.com/software/writing-with-our-mind).


## Applications

The whole workflow:
1. Receiving raw signal from BS interface [blueatooth]
1. Processing & cleaning signals from BCI
1. Detecting commands and sending to backend [sockets]
2. Broadcasting actions from backend to frontend
3. Controlling the keyboard in the frontend application


### Data processing

The data processing application is decoding BCI signal and sending commands to backend.
The used communication to the BCI devise is [labstreaminglayer](https://github.com/sccn/labstreaminglayer).

Minor TODO:
* detect blinking

### BackEnd

![backend](web_speller/logo.png)

### FrontEnd

![keyboard](web_speller/screenshot.jpg)

The layout is located in `landing page`

## Data

The can be streamed from the BCI device in following 17 channels, each as float32.
The repository contains also recording samples of visual artifacts such as blinking and biting in sequences and blinking by both/left/right eye.

**Recorded channels**, in this particular "vision" configuration we were observing 8 eeg channels measuring mainly back part of human scale related to vision perception>.
* 8 EEG
* 3 ACC
* 3 Gyro
* 1 battery
* 1 count
* 1 val IO

**Required pre-processing**, see sample [notebooks](notebooks)
* remove the moise caused by electricity - 50Hz, use Notch filter
* band pass filter on 0.5 to 30Hz