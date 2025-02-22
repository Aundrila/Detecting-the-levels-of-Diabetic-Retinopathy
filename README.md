# Detecting-the-levels-of-Diabetic-Retinopathy
This project aims to automate the classification of Diabetic Retinopathy (DR) using deep learning techniques. The model uses ResNet-50 for feature extraction and is trained on fundus (retinal) images to categorize DR into different severity levels. The project also applies image enhancement techniques to improve classification accuracy.

## Objectives
- Develop a Convolutional Neural Network (CNN) to classify DR severity.
- Use image preprocessing and enhancement techniques to improve model performance.
- Evaluate the effectiveness of transfer learning (ResNet-50) in medical image classification.
- Analyze model performance using accuracy, precision, recall, and confusion matrix.

## Tools and Libraries
- **Programming Language:** Python
- **Deep Learning Frameworks:** TensorFlow, Keras
- **Image Processing Libraries:** OpenCV, PIL
- **Data Science Libraries:** NumPy, Pandas, Matplotlib, Seaborn
- **Model Architecture:** ResNet-50 (Transfer Learning)

## Dataset
- The dataset consists of retinal fundus images, categorized into:
  1. No DR
  2. Mild DR
  3. Moderate DR
  4. Severe DR
  5. Proliferative DR
- Images are preprocessed using contrast adjustment, resizing, and normalization before feeding into the model.

## Methodology
**1. Data Preprocessing & Augmentation**
- **Image enhancement**: Improves visibility for retinal features
- **Data augmentation**: Rotation, flipping and zooming to improve model generalization
- **Normalization & resizing**: Standardizes image dimensions for model input

**2. Model Development (ResNet-50)**
- **Feature extraction:** Uses a pre-trained RresNet-50 model
- **Full connected layers:** Added on top for classification into DR severity levels
- **Loss function:** Categorical Cross-entropy
- **Optimizer:** Adam/SGD for efficient convergence



