# Object Detection on Formula One with PyTorch
 This project uses YOLOv5 to detect 3 objects (F1_Car,  Wheel and Steering), using a mp4 file of a Formula One Race. 


This project was to create a customised object detector using YOLOv5. The were 3 objects which were detected: Formula One Cars, Drivers and Steering Wheels. 

The orginal data for the project was mp4 file of a formula one race. 

The first script saves takes the mp4 file as input, then saves the frames as a jpg at a 5 second interval. To capture the different camera shots of the footage.

The ouput of that script was images which were then labellled using labelImg and data augmentation with Roboflow. 

The labelled data was uploaded to Google Colab. Where a Object Detection Model was created using PyTorch and YOLOv5. 


The task was completed using 3 main technologies: Roboflow, Google Colab and YOLOv5. 


# Recommended Reads and Useful Links

Antonio. (2020). “F1 GP Monaco 2018”. [online] Available at: https://www.youtube.com/watch?v=ZlImFqt3e4c&list=PL-aFWiXKlyKDs5F-bdgnnjRTiuPGdfEw3&index=5 [Accessed 5 May 2021]
Bergstra, J. and Breuleux, O. and Bastien, F. and Lamblin, P. and Pascanu, R. and Desjardins, G. and Turian, J. and Warde-Farley, D. and Bengio, Y. (2010) “Theano: A CPU and GPU Math Compiler in Python” 9th Annual Python In Science Conference, Universite de Montreal
Du, J. (2018) “Understanding of Object Detection Based on CNN Family and YOLO”, Journal of Physics: Conference Series, IOP Publishing, doi 10.1088/1742-6596/1004/1/012029 
Ezgif. (2021) “Animated GIF Maker”. [online] Available at: https://ezgif.com/maker [Accessed 7 July 2021]
Glassner, A. (2021).  “Deep Learning: A Visual Approach”, No Starch Press, ISBN:  1718500726
Google Colaboratory. (2021) [online] “What is Colaboratory?” Available at: https://colab.research.google.com/notebooks/intro.ipynb#scrollTo=5fCEDCU_qrC0 [Accessed 5 May 2021]
Jiang, Y. (2017) “Python - Extracting and Saving Video Frames” [online] Available at: https://stackoverflow.com/questions/33311153/python-extracting-and-saving-video-frames  [Accessed 7 May 2021] 
Kuznetsova A., Maleva T., Soloviev V. (2020) Detecting Apples in Orchards Using YOLOv3 and YOLOv5 in General and Close-Up Images. In: Han M., Qin S., Zhang N. (eds) Advances in Neural Networks – ISNN 2020. ISNN 2020. Lecture Notes in Computer Science, vol 12557. Springer, Cham. https://doi.org/10.1007/978-3-030-64221-1_20
Pysource, (2020) “Train YOLO to Detect a Custom Object (Online with Free GPU)” [online] Available at: https://colab.research.google.com/drive/1gDZ2xcTOgR39tGGs-EZ6i3RTs16wmzZQ [Accessed 10 May 2021]
Roboflow. (2021) “Roboflow Features” [online] Available at: https://roboflow.com/features [Accessed 2 July 2021]
Roboflow. (2021) “How to Train YOLOv5 on Custom Objects” [online] Available at: https://colab.research.google.com/drive/1gDZ2xcTOgR39tGGs-EZ6i3RTs16wmzZQ [Accessed 2 July 2021]
Rumale ,A. (2021) “A Study On Intelligent Video Surveillance Using Yolo Object Detection”, International Research Journal of Modernization in Engineering Technology and Science, Volume 3, Issue 2
TensorFlow, (2021). “GPU Support” [online] Available at: https://www.tensorflow.org/install/gpu [Accessed 5 May 2021] 
Tzutalin. (2021)”Windows_v1.7.0” [online] Available at: https://tzutalin.github.io/labelImg/ [Accessed 10 May 2021]
Vostrikov A., Chernyshev S. (2019) Training Sample Generation Software. In: Czarnowski I., Howlett R., Jain L. (eds) Intelligent Decision Technologies 2019. Smart Innovation, Systems and Technologies, vol 143. Springer, Singapore. https://doi.org/10.1007/978-981-13-8303-8_13
Ultralytics. (2021) “yolov3”. GitHub Repository, Available at: https://github.com/ultralytics/yolov3 [Accessed 10 May 2021]
Ultralytics. (2021) “yolov5”. GitHub Repository, Available at: https://github.com/ultralytics/yolov5  [Accessed 1 July 2021]
Wexler, J., Pushkarna, M. Bolukbasi, T.and  Wilson, J.  "The What-If Tool: Interactive Probing of Machine Learning Models," in IEEE Transactions on Visualization and Computer Graphics, vol. 26, no. 1, pp. 56-65, Jan. 2020, doi: 10.1109/TVCG.2019.2934619
Xu, R.,  Lin, H., Lu, K., Cao, L. and Liu, Y. (2021) A Forest Fire Detection System Based on Ensemble Learning. Forests. 12. 217. 10.3390/f12020217.
