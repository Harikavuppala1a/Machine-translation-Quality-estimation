# Quality-estimation:

Sentence Level Machine translation quality estimation

### Quaityvector
Using a parallel corpora, trains the neural machine translation (encoder-decoder-attention-bidirectional) model. Training data for quality estimation are then run through this model to obtain the quality vectors as input to qualityscore. 

To create the model:

python qualityvector/qualvec.py --data_dir < directory containing parallel corpora> --traindir trainingdirectory

To get the quality vectors:

python qualityvector/qualvec.py --data_dir < directory  containing quality estimation data > --traindir trainingdirectory --qualvec

### Qualityscore
The 2nd step to training the quality estimation model. Takes the quality vector from qualityvector, runs a GRU RNN on it and use last hidden state to predict the HTER score.

To create the model:

python qualityscore/qescore.py --data_dir < directory contain quality vectors and labels > --traindir trainingdirectory

To get the quality scores:

python qualityscore/qescore.py --data_dir < directory containing training vectors  > --traindir trainingdirectory --qescore

To get the scores:

To get final result run:

python result.py

### SVR
Get the baseline score using Support Vector Regression on baseline features. Hyperparameters are optimized using particle swarm optimization.


