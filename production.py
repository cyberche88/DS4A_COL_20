from fastai.vision import load_learner, ImageList, DatasetType
import numpy as np
import os
import pickle

print("---importando production---")

# Detecting and/or making the current image path
CURRENT_FOLDER = os.path.dirname(os.path.realpath(__file__))
DIRECTORY = os.path.join(CURRENT_FOLDER, 'models')

ARQUITECTURE = "resnet18" # Select the arquitecture to load

if ARQUITECTURE == "resnet18":
    modelo_file = "export-cells ResNet18.pkl"
    features_file = 'deep_features_training_resnet18.pkl'
elif ARQUITECTURE == "effB4":
    features_file = 'deep_features_training_effB4.pkl'
    modelo_file = "export-cells_EfficientNet.pkl"


learn = load_learner(DIRECTORY, modelo_file) # Load the full model

with open( os.path.join(DIRECTORY,features_file), 'rb' ) as f:
    tipos_train, features_train = pickle.load(f)


class SaveFeatures():
    features=None
    def __init__(self, m): 
        self.hook = m.register_forward_hook(self.hook_fn)
        self.features = None
    def hook_fn(self, module, input, output): 
        self.features = output.detach().cpu().numpy()
    def remove(self): 
        self.hook.remove()


class predictor():
    """Class to store the info about the prediction in a global way 
    and also include info about the train sample to plot and to predict"""
    def __init__(self):
        self.predictions_dict = None
        self.arquitecture = ARQUITECTURE
        self.features = None
        self.features_train = features_train
        self.labels = None
        self.tipos_train = tipos_train
        self.figure = None
        self.tx = None
        self.ty = None

    def prediction(self, directorio, num_batch = 8):
        
        data = ImageList.from_folder(directorio) # build the ImageList from the folder
        learn.data.add_test(data) # add data to the test set of learn
        
        learn.to_fp32() # pass the model and data to FP16 

        if self.arquitecture == 'resnet18':
            sf = SaveFeatures(learn.model[1][4])
        elif self.arquitecture == 'effB4':
            sf = SaveFeatures(learn.model._avg_pooling)

        # get the probabilities of images
        preds,_ = learn.get_preds(ds_type=DatasetType.Test, n_batch=num_batch)
        
        # Get the predictions (intenger indexes)
        y_pred = preds.argmax(dim=1).tolist() # using the arguments of the max probabilities
        
        self.predictions_dict = {n.name:learn.data.classes[y] for n,y in zip(data.items, y_pred)} 
        self.features = sf.features.squeeze()
        self.labels = list(set(self.predictions_dict.values()))

        # # To avoid problem with 1D array
        # if features.ndim == 1:
        #     features = features.reshape(1,-1)
        # features = np.concatenate( (features_train, features))
