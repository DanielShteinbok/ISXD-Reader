import numpy as np

def load_image(filename, index=0, dimensions=(400,640)):
    with open(filename, 'rb') as file:
        # get metadata size
#         file.seek(-8)
#         metadata_size = int(file.read(8))
#         file.seek(0)
#         all_data = file.read()
        file.seek(2*(dimensions[0]+8)*dimensions[1]*index)
        img_data = np.frombuffer(file.read(2*(dimensions[0]+4)*dimensions[1]), 
                                 dtype=np.uint16)[2*dimensions[1]:(dimensions[0]+2)*dimensions[1]].reshape(dimensions)
    return img_data