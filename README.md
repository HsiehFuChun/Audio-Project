# Audio Reverse-engineering Project
This is a project done by FuChun Hsieh and Stephen Zhong. We aimed to find the original audio of the converted audio converted using AGAIN-VC. 
Stephen built the CNN classifier to classifiy original and converted audio. And it shows that the CNN model has 80% accuracy.
FuChun built the random forest decision tree model and CNN model to determine if machine learning model can find the original audio of the converted audio.
In the early experiment of random forest classifier, it cannot accurately classify the original audio so we drop this method.
In CNN model, we delivered .82 as our highest accuracy and it shows that we can effectively find the orginal audio even it is converted to other sound.
