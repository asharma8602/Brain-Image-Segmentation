import matplotlib

matplotlib.use('TKAgg')
from matplotlib import pylab as plt
import nibabel as nib
from nibabel import nifti1
from nibabel.viewers import OrthoSlicer3D

filename = 'image-loaders\dataset\CAHI01.nii.gz'
img = nib.load(filename)
print('img:\n', img)
print('img.header:\n', img.header['db_name'])  # Output header information

# It is determined by the dimension of the file itself, which may be 3D or 4D
width, height, queue = img.dataobj.shape
print(width, height, queue)  # 175 132 88

OrthoSlicer3D(img.dataobj).show()

num = 1
for i in range(0, queue, 11):
    img_arr = img.dataobj[:, :, i]
    plt.subplot(2, 4, num)
    plt.imshow(img_arr, cmap='gray')
    num += 1
plt.show()