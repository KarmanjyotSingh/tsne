## t-SNE 
---

#### An Introduction 

1. A better alternate to the existing visualisation techniques like PCA, etc. for visualising higher dimensional data into 2-D plots.
2. Here we generate a mapping from the higher dimensional data set X = ${x_1,x_2,x_3 ..... x_n}$ to Y = ${y_1,y_2,y_3.......y_n}$ .. while retaining maximum possible structure of the higher dimensional data.

#### SNE ( Stochastic Neighbor Embedding ) 

Glossary - **embedding** : refers to the vector representation of a particular feature.

1. It consverts high-dimensional data points between the points into conditional probabilities that represent the similarities. 
2. The similarity is expressed through the conditional probability $p_i$ $_|$ $_j$ such that the data point $x_i$ would pick the data point $x_j$ as it's neighbour if the neighbours were picked in proportion to their probability density under a Gaussian centered at $x_i$.