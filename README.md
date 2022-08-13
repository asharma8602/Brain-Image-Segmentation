<br />
<p align="center">
  <h1 align="center">Brain Segmentation</h1>
</p>

<b><h2>Getting Started</h2></b>

To get a local copy up and running follow these simple steps.

<b><h2>Prerequisites</h2></b>

The requirements.txt must be installed if you run on a local system; otherwise, installing libraries is not required if you run on Google Collab.

<b><h2>Installation</h2></b>

1. Clone the project
   ```sh
   git clone https://github.com/asharma8602/Brain-Image-Segmentation
   ```

2. Before running the Python Notebook on your local system.
   ```sh
   pip install -r requirements.txt
   ```

<b><h2>Directory Structure</h2></b>

```
├───Train_Images
└───Train_Labels
    ├───Contours
    ├───Distance_Maps
    └───Masks
```

<b><h2>Model Details</h2></b>

<b><h3>Data-set</h3></b>

<b>Indian Brain Segmentation Dataset</b> (IBSD) consists of high-quality 1.5T T1w MRI data of 114 subjects generated under fixed imaging protocol along with corresponding manual annotation data of 14 sub-cortical structures done by expert radiologists. The number of MR scans in the dataset consists of an approximately equal number of male and female subjects belonging to a young age group (20-30 years). This data has been used to create a template for the young Indian population.

<b><h3>Data Preprocessing</h3></b>

1. Reading MRI data of 113 subjects in the form of NiFti Images.

2. Combining 14 labels to establish a binary classification Psi-net.

3. Saving 192 slices per subject to adjust the data corresponding to Psi-net architecture.

4. Conversion of labels to Binary Masks which further being converted to Contours and finally obtaining Distance Maps for them.

<b><h3>Data Loader</h3></b>

A custom data-loader function is designed with following functions.

1. loadimage - Loading input image
2. loadmask - Loading mask of corresponding label
3. loadcont - Loading contour of corresponding label
4. loaddist - Loading distance map of corresponding label

<b><h2>Citations</h2></b>

```
@article{Murugesan2019PsiNetSA,
  title={Psi-Net: Shape and boundary aware joint multi-task deep network for medical image segmentation},
  author={Balamurali Murugesan and Kaushik Sarveswaran and Sharath M. Shankaranarayana and Keerthi Ram and Mohanasankar Sivaprakasam},
  journal={ArXiv},
  year={2019},
  volume={abs/1902.04099}
```

```
Jayanthi Sivaswamy, Alphin J Thottupattu, Mythri V, Raghav Mehta, R Sheelakumari, & Chandrasekharan Kesavadas. (2021, November 8). 
Indian Brain Segmentation Dataset(IBSD). 
Zenodo. https://doi.org/10.5281/zenodo.5656776
```

