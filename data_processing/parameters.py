# image processing parameters
target_size = (71,71)
shuffle = True
batch_size = 128
rescale = 1./255
rotation_range = 20
width_shift_range = 0.15
height_shift_range = 0.15
shear_range = 0.1
pv_directory = 'data/processed_data'
raw_train_path = 'data/train'
raw_test_path = 'data/test'
color_mode ='rgb'