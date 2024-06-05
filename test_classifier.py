#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/test_classifier.py
#                                                                             
# PROGRAMMER: Jennifer S.                                                    
# DATE CREATED: 01/30/2018                                  
# REVISED DATE:             <=(Date Revised - if any)                         
# PURPOSE: To demonstrate the proper usage of the classifier() function that 
#          is defined in classifier.py This function uses CNN model 
#          architecture that has been pretrained on the ImageNet data to 
#          classify images. The only model architectures that this function 
#          will accept are: 'resnet', 'alexnet', and 'vgg'. See the example
#          usage below.
#
# Usage: python test_classifier.py    -- will run program from commandline

# Imports classifier function for using pretrained CNN to classify images 
from classifier import classifier 
import os
# Defines a dog test image from pet_images folder
# test_image="pet_images/German_shepherd_dog_04890.jpg"

# Defines a model architecture to be used for classification
# NOTE: this function only works for model architectures: 
#      'vgg', 'alexnet', 'resnet'  
model = "vgg"

# Demonstrates classifier() functions usage
# NOTE: image_classication is a text string - It contains mixed case(both lower
# and upper case letter) image labels that can be separated by commas when a 
# label has more than one word that can describe it.
files = os.listdir('pet_images')
    
# Filter files to include only images (if necessary, based on file extensions)
image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp')

for file in files: 
    if file.lower().endswith(image_extensions): 
            file = 'pet_images/'+file
            print(file)
            image_classification = classifier(file, model)

            print(type(image_classification))

            # prints result from running classifier() function
            print("\nResults from test_classifier.py\nImage:", file, "using model:",
                  model, "was classified as a:", image_classification)

            # test_dict = dict() 

            name_lwr_splt = image_classification.lower().split('_')
            pet_label1 = ' '.join([char for char in name_lwr_splt if char.isalpha()]) 

            # for name in image_classification: 
            #         #skip hidden files
            #         if name.startswith('.'):
            #             continue

            #         #Lowercase and split around underscore
            #         name_lwr_splt = name.lower().split('_')
            #         # print(name_lwr_splt, type(name_lwr_splt))
                  
            #         pet_label = ' '.join([char for char in name_lwr_splt if char.isalpha()])
            #         # print(pet_label)
            #         if name not in test_dict:
            #             test_dict[name] = pet_label.strip()

            print('\n', 'label:', pet_label1)#, type(pet_label)) #'Name:',name_lwr_splt,

