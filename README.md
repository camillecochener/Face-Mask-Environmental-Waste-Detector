<div align='center'><h1>Disposable Mask Segmentation</h1></div>

Following the coronavirus crisis, many disposable masks are found in the outdoor environment: in the street, in nature. This crisis brings a new type of waste to the environment. In order to complete the research in waste detection in the natural environment, I have decided to build a detection system capable of identifying and segmenting these masks. 

[SAMPLE IMAGES]

This type of detector could be of interest for building automated systems for collecting waste in the streets for example. 

## 1 - Data

**Collection**

For this purpose, 65 images of masks found outdoors were used. For the moment, this dataset is small because I started the project at the beginning of 2021. Nevertheless, my relatives and I are collecting new ones every day in order to complete this dataset. 

My goal is to collect 1000 images. 

If you wish to contribute to this project and strengthen the detection system, please feel free to capture images on your side and send them to me by email: cochenercamille@yahoo.fr !

**Annotation**

The data are annotated and reviewed with <a src="https://labelbox.com/">LabelBox</a> but many other platforms exist. A JSON file is exported and put into the `data/` folder of the repository. 

Fields of interest in the JSON file are : XXX
  
## 2 - Approach 

**Instance segmentation with Mask-RCNN** 
  
To perform instance segmentation on this dataset, I've decided to use the <a src="https://arxiv.org/abs/1703.06870">Mask-RCNN architecture</a> by Kaiming He et al. from Facebook AI Research (FAIR) in 2017. Mask-RCNN is moslty based on Faster-RCNN, which is a two stage detector composed of a region-proposal network, followed by two branches predicting the class and the box offset for each proposed region. The authors extended Faster-RCNN with a *third parallel branch*, outputting a binary mask for the element in each region. Mask-RCNN distinguished itself at the COCO 2017 challenges and is widely used nowadays.  

I've used the <a src="https://github.com/matterport/Mask_RCNN">Matterport implementation of Mask-RCNN</a> to build my detector, which use Python 3, Keras and TensorFlow, and adapted it to my needs. 

**Steps I followed**

- Clone and adapt the Matterport Mask-RCNN repository to my needs
`git clone https://github.com/matterport/Mask_RCNN.git maskrcnn`

- Create a virtual environment
`virtualenv -p /Users/camillecochener/.pyenv/versions/3.7.0/bin/python3 venv`

- Source the virtual environment
`source venv/bin/activate`

- Install the requirements
`pip install -r requirements.txt`

- Download the images from LabelBox  
`python download.py data/annotations.json`  

- Split the dataset into three folder train/val/test
`python split_train_val_test.py data`
