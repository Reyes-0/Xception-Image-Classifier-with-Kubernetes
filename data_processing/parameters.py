# image processing parameters
target_size = (71,71)
shuffle = True
batch_size = 128
rescale = 1./255
rotation_range = 20
width_shift_range = 0.15
height_shift_range = 0.15
shear_range = 0.1
pv_directory = '/data/processed_data'
# raw_train_path = '/mnt/c/School/Year3 Sem1/AI Solution Dev/train_data'
# raw_test_path = '/mnt/c/School/Year3 Sem1/AI Solution Dev/test_data'
raw_train_path = 'raw_data/train'
raw_test_path = 'raw_data/test'
processed_test_path = '/app/preprocessed/data/processed_test_data'
processed_train_path = '/app/preprocessed/data/processed_train_data'
color_mode ='rgb'