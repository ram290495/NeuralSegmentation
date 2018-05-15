import niftiStream as ns

# set up constants
nFiles = 10
# path to inputs and labels
images_path = "C:\\Users\\ram8\\Desktop\\NiftiData\\images\\"
labels_path = "C:\\Users\\ram8\\Desktop\\NiftiData\\labels\\"

image_loader = ns.NiftiStream()
label_loader = ns.NiftiStream()
for i in range(nFiles):
    image_loader.load_file(images_path + "training_axial_crop_pat" + str(i) + ".nii.gz")
    label_loader.load_file(labels_path + "training_axial_crop_pat" + str(i) + "-label.nii.gz")


