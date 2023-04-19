# Text-Classification
Using ML and NLP techniques, text classification is conducted in this notebook to identify relevant reviews from a book review dataset. Kindly note that the ML model is trained using a sample dataset consisting of the first 30 reviews from three books (total 87 datapoints, excluding null values). During the exercise, two models are are developed: a semi-supervised SelfTrainingClassifier and a supervised SVC.

The selected model from the two models is saved as "spam_detector.joblib" and can be loaded/imported for future use.

For effective task execution of the spam detector, it is required to import model_dependency_script into your local machine as it contains libraries and user-defined-functions on which the machine learning model depends.

**Kindly note that:** the **model_dependency_script.py** should be downloaded and situated in the same directory as **spam_detector.joblib** for successful import.


## How to Use

**from** model_dependency_script **import** text_preprocessing, sparse_to_dense

**import** joblib

**model = joblib.load(model_path_on_local_machine/spam_detector.joblib)**

**model.predict(text)**
