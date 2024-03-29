# Learning from Candidate Examples

This repository provides code for reproducing the figures in the paper:

**"Leveraging inductive bias of neural networks for learning without explicit human annotations"**, by Fatih Furkan Yilmaz and Reinhard Heckel

# Downloading the dataset
Use the following [dropbox link](https://www.dropbox.com/sh/eh07jhrwxjugqbb/AAClfTPne3uWlcnjc__FNkKpa?dl=0) to download numpy files containing test and train sets, specifically, our candidate train set, the CIFAR-10.1 test set, and the original CIFAR-10 test and training datasets. Provide the directory of the files to the root argument in the `train_reproducible` notebook.
- `candidate.npz` Contains the candidate training set (which we constructed from the [TinyImages dataset](https://groups.csail.mit.edu/vision/TinyImages/) from Antonio Torralba, Rob Fergus, William T. Freeman as described in our paper), as well as the [CIFAR 10.1](https://github.com/modestyachts/CIFAR-10.1) test set from Ben Recht, Rebecca Roelofs, Ludwig Schmidt, and Vaishaal Shankar.
- `cifar.npz` Contains the original [CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar.html) dataset from Alex Krizhevsky, Vinod Nair, and Geoffrey Hinton.
- `sims.npz` Contains the similar images excluded from the training set.

# Training on candidate dataset
The code for training models on candidate or CIFAR-10 training sets is given in the `train_reproducible` notebook. The following variables can be adjusted for different experiments:
- *root*: Directory (`pathlib`) where the `.npz` files of the dataset reside.
- *main_file*: Filename for the candidate dataset.
- *sub_file* (optional): Filename for the CIFAR-10 dataset. Primary use is to track the accuracy on a clean subset of candidate dataset.
- *model*: PyTorch model, from \{'resnet', 'densenet', 'vgg', 'shake', 'pyramidnet', 'resnext'\}.
- *outpath*: Output file for storing training logs.
- *epochs*: \# epochs.
- *print_freq*: Frequency for console log.
- *gpu*: GPU for Cuda. If not given, all available Cuda devices will be used.
- *batch_size*: Training batch size. Default values are chosen with respect to maximum 12GiB memory.

# Visualizing results
The code for plotting the training results from the log files is given in the `visualize_train_logs` notebook.

# Inspecting similar images
The code for visually inspecting similar images is given in the `inspecting_similar_images` notebook.
The test image with the index provided to *test_ind* variable is shown along with the top-100 closest images from the candidate set including the eliminated images. 

Images that are eliminated from the candidate set upon manual inspection are marked as 'Excluded'.


## Source codes
Acknowledgements for PyTorch implementations of the models and examples are as follows:

**Training code**
- The code for training has been incorporated and modified from the _official_ PyTorch examples repository [https://github.com/pytorch/examples/...](https://github.com/pytorch/examples/tree/master/imagenet). The default hyperparameters has been used for fair experiments and comparison. 

**Models**
- *ResNet-18*: https://github.com/kuangliu/pytorch-cifar
- *DenseNet-BC-100*: https://github.com/hysts/pytorch_image_classification

## Citation
```
@article{yilmaz_heckel_2019,
    author    = {Fatih Furkan Yilmaz and Reinhard Heckel},
    title     = {Leveraging inductive bias of neural networks for learning without explicit human annotations},
    journal   = {arXiv:1910.09055},
    year      = {2019}
}
```

## Licence

All files are provided under the terms of the Apache License, Version 2.0.

