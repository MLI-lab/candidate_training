# candidate_training
Reproducible version of the experiments in "Leveraging inductive bias of neural networks for learning without explicit human annotations"

# Downloading the dataset
Use the following [dropbox link](https://www.dropbox.com/sh/eh07jhrwxjugqbb/AAClfTPne3uWlcnjc__FNkKpa?dl=0) to download the numpy files for both the candidate and CIFAR-10 datasets. Provide the directory of the files to the root argument in the `train_reproducible` notebook.

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
