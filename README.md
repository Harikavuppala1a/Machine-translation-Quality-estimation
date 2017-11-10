# Quality-estimation:

Machine translation quality estimation

### quaityvector
Using a parallel corpora, trains the neural machine translation (encoder-decoder-attention-bidirectional) model. Training data for quality estimation are then run through this model to obtain the quality vectors as input to qualityscore. 

### qualityscore
The 2nd step to training the quality estimation model. Takes the quality vector from qualityvector, runs a GRU RNN on it and use last hidden state to predict the HTER score.

### svr
Get the baseline score using Support Vector Regression on baseline features. Hyperparameters are optimized using particle swarm optimization.
