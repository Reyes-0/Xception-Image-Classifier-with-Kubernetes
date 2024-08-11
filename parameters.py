#parameters 
INPUT_FILE_PETS = 'CAIEsubmission\raw_data\pets_prepared.csv'
# INPUT_FILE_BREED=CAIEsubmission\raw_data\breed_labels.csv
# PROCESSED_FILE=CAIEsubmission\raw_data\pets_cleaned.csv
# MAX_DEPTH=4
# N_ESTIMATORS=50
# TEST_SIZE=0.2


# data paths
# raw_train_path = 
# raw_test_path = 
# uploaded_image_path = 

# image processing parameters
target_size = (71,71, 3)
shuffle = True
batch_size = 128
rescale = 1./255
rotation_range = 20
width_shift_range = 0.15
height_shift_range = 0.15
shear_range = 0.1

# model training/fine tunning parameters
