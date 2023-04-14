# xBD-with-YOLOv8

<summary>Install</summary>
Pip install the ultralytics package including all [requirements](https://github.com/ultralytics/ultralytics/blob/main/requirements.txt) in a [**Python>=3.7**](https://www.python.org/) environment with [**PyTorch>=1.7**](https://pytorch.org/get-started/locally/).

```bash
pip install ultralytics
```

check installation path with:

```bash
pip show ultralytics
```

swap ultralytic folder with the folder provided in this repo, to get the 6 channel input support for the network

<summary>Data</summary>
download the model: https://1drv.ms/u/s!ApM4bGJ9IAIegehRqnB5JqUysO9DDw?e=UmY8od

a few test images are provided, additional images need to be downloaded from the xview2 website: https://xview2.org/download 
or choose your own images

data and labels must be saved in the structure as shown in this repo

<summary>Usage</summary>

if environment variables are setup correctly you can use yolo in the Command Line Interface

yolo predict model=path\to\the\theModel.pt source='path\to\images'

or otherwise

python path\to\python\ultralytics\yolo\v8\segment\predict.py --model path\to\theModel.pt --source 'path\to\images'

use 'val' for validation metrics
yolo val model=path\to\the\theModel.pt data=path\to\xBD.yaml
xBD.yaml provided in this repo, dataset root dir need to be edited


get further information here:
https://github.com/ultralytics/ultralytics
https://docs.ultralytics.com/

contact me if bugs appear
