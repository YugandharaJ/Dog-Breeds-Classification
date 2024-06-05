#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#                                                                             
# PROGRAMMER: Yuga
# DATE CREATED: 06/02/2024                              
# REVISED DATE: 
# PURPOSE: Create a function classify_images that uses the classifier function 
#          to create the classifier labels and then compares the classifier 
#          labels to the pet image labels. This function inputs:
#            -The Image Folder as image_dir within classify_images and function 
#             and as in_arg.dir for function call within main. 
#            -The results dictionary as results_dic within classify_images 
#             function and results for the functin call within main.
#            -The CNN model architecture as model within classify_images function
#             and in_arg.arch for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           classifier label as the item at index 1 of the list and the comparison 
#           of the pet and classifier labels as the item at index 2 of the list.
#
##
# Imports classifier function for using CNN to classify images 
from classifier import classifier 
import os
import re 
# TODO 3: Define classify_images function below, specifically replace the None
#       below by the function definition of the classify_images function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
# 
def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with classifier function, compares pet labels to 
    the classifier labels, and adds the classifier label and the comparison of 
    the labels to the results dictionary using the extend function. Be sure to
    format the classifier labels so that they will match your pet image labels.
    The format will include putting the classifier labels in all lower case 
    letters and strip the leading and trailing whitespace characters from them.
    For example, the Classifier function returns = 'Maltese dog, Maltese terrier, Maltese' 
    so the classifier label = 'maltese dog, maltese terrier, maltese'.
    Recall that dog names from the classifier function can be a string of dog 
    names separated by commas when a particular breed of dog has multiple dog 
    names associated with that breed. For example, you will find pet images of
    a 'dalmatian'(pet label) and it will match to the classifier label 
    'dalmatian, coach dog, carriage dog' if the classifier function correctly 
    classified the pet images of dalmatians.
     PLEASE NOTE: This function uses the classifier() function defined in 
     classifier.py within this function. The proper use of this function is
     in test_classifier.py Please refer to this program prior to using the 
     classifier() function to classify images within this function 
     Parameters: 
      images_dir - The (full) path to the folder of images that are to be
                   classified by the classifier function (string)
      results_dic - Results Dictionary with 'key' as image filename and 'value'
                    as a List. Where the list will contain the following items: 
                  index 0 = pet image label (string)
                --- where index 1 & index 2 are added by this function ---
                  NEW - index 1 = classifier label (string)
                  NEW - index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifer labels and 0 = no match between labels
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
     Returns:
           None - results_dic is mutable data type so no return needed.         
    """

    # for key in results_dic: 
    #   image_path = os.path.join(images_dir, key)
    #   classifier_label = classifier(image_path, model).lower().strip()
    #   classifier_labels = re.split(r'[,]', classifier_label)
    #   classifier_labels = [label.strip() for label in classifier_labels]
      
    #   match = 0
    #   pet_label = results_dic[key][0]
      
    #   if pet_label in classifier_labels:
    #       match = 1
      
    #   # results_dic[key].extend([classifier_label, match])

    #   # Ensure that results_dic[key] is a list
    #   if isinstance(results_dic[key], list):
    #       results_dic[key].extend([classifier_label, match])
    #   else:
    #       results_dic[key] = [results_dic[key], classifier_label, match]
    step = 0
    for r in results_dic: 
        step += 1
        val_list = []
        model_label = os.path.join(images_dir, r)
        clfr_lbls = classifier(model_label,model) 

        clfr_lbls = clfr_lbls.lower().strip()
        clsfr_lbl =  re.split(r"[,,_,',]", clfr_lbls)
        clsfr_lbl = [label.strip() for label in clsfr_lbl]
        # print(clfr_lbls, clsfr_lbl)
        # print('Count:',step,'key if:',r,'Results if:',results_dic[r], 'Clsfr lbl:',clsfr_lbl)
        # if(not isinstance((results_dic[r]),list)):
        label = 0
        # val_list = [results_dic[r],clfr_lbls]
        # label_dict[r] = val_list
        # k=0
        # for i in range(len(clsfr_lbl)): 

        if results_dic[r] in clsfr_lbl:
            label = 1
            # val_list.append(1)
            # print('key:',r,'Results:',results_dic[r],'Clsfr lbl:',clsfr_lbl,'label:', label)
            # val_list = [results_dic[r],clfr_lbls, label] 
            # results_dic[r] = val_list
        # else: 
        #     print('Else key:',r,'Else Results:',results_dic[r],'Else Clsfr lbl:',clsfr_lbl,'label:', label)        

        val_list = [results_dic[r],clfr_lbls, label] 
        results_dic[r] = val_list

        # print(val_list)
        

    #Attempt2                
    # for r in results_dic: 
        
    #     val_list = []
    #     model_label = 'pet_images/'+r
    #     clfr_lbls = classifier(model_label,model) 

    #     clfr_lbls = clfr_lbls.lower()
    #     clsfr_lbl =  re.split(r"[,,_,']", clfr_lbls)
    #     if(not isinstance((results_dic[r]),list)):
    #         label = 0
    #         # val_list = [results_dic[r],clfr_lbls]
    #         # label_dict[r] = val_list
    #         # k=0
    #         for i in range(len(clsfr_lbl)): 

    #             if results_dic[r] == clsfr_lbl[i]:
    #                 label = 1
    #                 # val_list.append(1)

            
    #     val_list = [results_dic[r],clfr_lbls, label]
    #     results_dic[r] = val_list
                  




        # print(results_dic[r]) 
# # clfr_frmt_lbl = []
    # files = os.listdir(images_dir)
        
    # # Filter files to include only images (if necessary, based on file extensions)
    # image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp')

    # for file in files: 
    #     if file.lower().endswith(image_extensions): 
                
    #             file = 'pet_images/'+file
                
    #             clfr_lbls = classifier(file,model) 
                
    #             clfr_lbls = clfr_lbls.lower()

    #             clfr_lbls_mod =  re.split(r"[,,_,']", clfr_lbls)

    #             print(file, clfr_lbls, clfr_lbls_mod)

    #             # Remove any empty strings resulting from the split
    #             clsfr_lbl = [item.strip() for item in clfr_lbls_mod if item.strip()] 

                
    #             for r in results_dic: 
              
    #                 if(not isinstance((results_dic[r]),list)):
    #                     # chk = []
    #                     val_list = [results_dic[r],clfr_lbls]
    #                     # label_dict[r] = val_list
    #                     # k=0
    #                     for i in range(len(clsfr_lbl)): 
                        
                            
    #                         if results_dic[r] == clsfr_lbl[i]:
    #                             print('key:',results_dic[r], clsfr_lbl[i])
    #                             val_list.append(1)
    #                         else: 
    #                             print('key:',results_dic[r], clsfr_lbl[i])
    #                             val_list.append(0)
                        
    #                     results_dic[r] = val_list
                              
    #                 print(results_dic[r])    

    
