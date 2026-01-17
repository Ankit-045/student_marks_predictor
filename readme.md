## 🧠 Project Models Used



This project uses multiple **regression models** to predict student exam scores based on academic and lifestyle features.



### Models Implemented

• **Linear Regression**  
Used as the baseline model.  
It performed best because the data shows strong linear relationships between features and exam scores.



• **Decision Tree Regressor**  
A tree-based model capable of learning non-linear patterns.  
It was tuned using hyperparameters like `max_depth` and `min_samples_split`.



• **Random Forest Regressor**  
An ensemble model made of multiple decision trees.  
It provides more stable predictions and reduces overfitting compared to a single tree.



After comparison using RMSE and R² score, **Linear Regression was selected as the final model**.



---

## 📚 Libraries Used



The following Python libraries are used in this project:



• pandas – data loading and manipulation  
• numpy – numerical operations  
• matplotlib – basic data visualization  
• seaborn – advanced visualizations (heatmaps, plots)  
• scikit-learn – machine learning models and evaluation  
• joblib – saving and loading trained models



## 🚀 How to Use This Project


1. Clone the repository  
2. Install required libraries  
3. Load the dataset (CSV file)  
4. Run the notebook or Python script  
5. Train models and compare results  
6. Use the saved model to make predictions


