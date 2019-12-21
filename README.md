# ASCON

American Sign Language to Speech Converter, completed for [Pragyan 2017](https://drive.google.com/file/d/0B_C16gaD3iInWF9DSzFmcEF2Z3hLVTZsZjh0Tm5qaHo4cGJJ/view?ts=580798e8).

## Description

We believe that communication is a basic right. The better we communicate and share ideas, the faster we progress as a society. The project aims to bridge the gap between people who are speech impaired and the people who don’t know sign language.

The hand gestures, as defined in the American Sign language, are converted to speech output based on the input from the Inertial Measurement Unit and the flex sensors.

A three layered Artificial Neural Network has been implemented with keras as the front end and theano as back end for classification of gestures. The processing has been done on a Beagle Bone Black.

The project is an effort to try and assist the 70 million people who can't communicate vocally.

### Code Organisation

```
Neural Nets Folder -- Contains codes for training and testing.
Feature Exraction  -- Contains codes for feature extraction.
Pragyan Final      -- Contains the final trained model and weights used for display during Pragyan 2017.
Documentation      -- Contains a link to the working video for our project.
```




