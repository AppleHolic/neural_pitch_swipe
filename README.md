# neural_pitch_swipe

Make an simple pytorch module to approximate pitch. 

- reference (https://pysptk.readthedocs.io/en/latest/generated/pysptk.sptk.swipe.html)

## Single Process

1. Preprocess audio files to extract pitch values for training speed 
2. Training a case (Hop Length, Window ...)
3. Add an case

## Why this model is handled with pytorch?

1. Use it as a submodule of other models. 
2. Do jit trace and use it on mobile devices


---

- author : Appleholic, choiilji@gmail.com
