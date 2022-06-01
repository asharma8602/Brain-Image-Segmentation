import SimpleITK as sitk
from matplotlib import pyplot as plt


def showNii(img):
    for i in range(img.shape[0]):
        print(i)
        plt.imshow(img[i, :, :], cmap='gray')
        plt.show()


itk_img = sitk.ReadImage("image-loaders\dataset\CAHI01.nii\CAHI01.nii")
img = sitk.GetArrayFromImage(itk_img)
print(img.shape)  # (88, 132, 175) indicates the number of slices in each dimension
showNii(img)