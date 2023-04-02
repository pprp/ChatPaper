
import numpy as np
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer

demo = """Introduction Deep convolutional neural networks (CNNs) have achieved great success in various computer vision tasks. However, as of today we still know little about what makes a CNN suit- able for analyzing natural images, i.e., what is its inductive bias. The inductive bias of a learning algorithm specifies constraints on the hypothesis space, and a model can only be instantiated from the hypothesis space that satisfies these constraints. It is easy to reveal the inductive bias of certain learning algorithms (e.g., a linear classifier specifies a linear relationship between the features and the target variable). But, the inductive bias of complex CNNs is still hidden in the fog (Cohen and Shashua 2017). Successfully identifying CNN’s inductive bias will not only deepen our theoretical un- derstanding of this complex model, but also lead to potential important algorithmic progresses. Objects are the key in most natural images, and CNNs are good at recognizing, detecting and segmenting objects. For in- stance, weakly supervised object localization (WSOL) (Zhou et al. 2016; Selvaraju et al. 2017; Zhang, Cao, and Wu 2020) and unsupervised object localization (USOL) methods (Wei et al. 2017, 2019) can even localize objects without training *J. Wu is the corresponding author. This research was supported by the National Natural Science Foundation of China under Grant 61772256 and 61921006. Copyright © 2022, Association for the Advancement of Artificial Intelligence (www.aaai.org). All rights reserved. CUB200 ImageNet VOC2007 Figure 1: Visualization of localization heatmaps using SCDA (Wei et al. 2017) for a randomly initialized ResNet-50. Best viewed in color when zoomed in. on bounding box annotations. All these methods, however, rely on ImageNet (Russakovsky et al. 2015) pretrained models and non-trivial learning steps. In this paper, we first show that focusing its attention to objects is a born gift of CNNs even without any training, i.e., it is CNN’s inductive bias (or one inductive bias out of many) from an empirical perspective! A randomly initialized CNN has surprisingly good localization ability, as shown in Figure 1. We name this phenomenon “The object is at sight”, or “Tobias” for short. The object(s) miraculously pop out (“at sight”) without any need for learning. Our conjecture is: the background is relatively texture-less compared to the objects, and texture-less regions have higher chances to be deactivated by activation functions like ReLU. Tobias then lends us ‘free’ (free of labels and pretrained models) and relatively accurate supervision for where objects are. Hence, a natural application of Tobias is self-supervised learning (SSL), which aims to learn useful representations without requiring labels. After the emerging of the InfoNCE loss (van den Oord, Li, and Vinyals 2018) and the contrastive learning paradigm, many SSL algorithms have been pub- lished, such as MoCo (He et al. 2020), SimCLR (Chen et al. 2020a), BYOL (Grill et al."""

# wash 
## delete the contents in the brackets
def wash_demo(demo):
    demo = demo.replace('(','')
    demo = demo.replace(')','')
    demo = demo.replace('[','')
    demo = demo.replace(']','')
    return demo
wash_demo(demo)

# Define the corpus
corpus = [line for line in demo.split('.') if line]

# Create a TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Fit the vectorizer on the corpus
X = vectorizer.fit_transform(corpus)

# Create a Singular Value Decomposition (SVD) object
svd = TruncatedSVD(n_components=2)

# Apply the SVD on the TF-IDF matrix
lsa = svd.fit_transform(X)

# Compute the sentence scores
scores = np.linalg.norm(lsa, axis=1)

# Sort the sentences by score in descending order
sorted_indices = np.argsort(scores)[::-1]

# Select the top n sentences
n = 30
selected_indices = sorted_indices[:n]

# Print the selected sentences
for idx in selected_indices:
    print(corpus[idx])