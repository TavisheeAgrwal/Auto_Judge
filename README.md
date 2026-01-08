# Auto_Judge
## Introduction
This is a tool built for judging the difficulty levels and alloting scores for coding problems.
Online programming platforms categorize problems by difficulty level and assign difficulty scores, which are typically determined through human judgment and user feedback. 
This project proposes AutoJudge, an automated system that predicts the difficulty class (Easy, Medium, Hard) and a numerical difficulty score for programming problems using only their textual descriptions.
This project demonstrates the complete ML pipeline, including preprocessing, feature extraction, classification, regression, evaluation, and deployment via a web UI.

## Dataset Used
```text
The dataset consists of programming problems collected from online competitive programming platforms. Each data sample contains the following fields:
•	“title”                       Problem name
•	“description”                 Detailed textual description of the problem
•	“input_description”           Textual Description of the input
•	“output_description”          Textual Description of the output
•	“sample_io”                   Sample for how input/output will be entered
•	“problem_class”               Problem classification into easy/medium/hard
•	“problem_score”               Score allotted based on difficulty
•	“url”                         Link to the problem
Only textual fields were used as inputs to satisfy project constraints.
```
## Approach 

1.Data Preprocessing:
```text
Checked for missing values.
Plotted graphs and conducted detailed eda to find hidden trends.
```

2.Feature Extraction:
```text
Dropped unnecessary columns like sample_io andd url.
Combined all the textual columns into one and later on discarded the individual columns.
Constructed addditional features like text_len , math_density etc .
Conducted vectorization usinf TF-IDF for the textual column.
Combined the vectorised and additional features.
```

## Model

### Model 1 : Classification 
```text
Objective: Predict difficulty class (Easy / Medium / Hard)
Model Used: XG Boost Classifier
```

### Model 2: Regression
```text
Objective: Predict numerical difficulty score
Model Used: XG Boost Regressor
```
## Evaluation Metrics
### Classification Performance
Accuracy:
```text
56 %
```

Confusion Matrix:
```text
              precision    recall  f1-score   support

        easy       0.57      0.35      0.43       136
        hard       0.62      0.76      0.68       425
      medium       0.40      0.34      0.37       262
```
### Regression Performance
```text
MAE: 1.65
RMSE: 2.01
```
## Web Interface Description
```text
A Streamlit-based web UI is provided.
Features:
Four input text boxes:
-Problem Title
-Problem Description
-Input Description
-Output Description

A Predict button

Displays:
Predicted difficulty class
Predicted difficulty score
No authentication or database is required.
The application runs entirely locally.
```
## Steps to Run the Project Locally
### 1.Clone the Repository
To clone this repository to your local machine, follow the steps below:
```bash
git clone https://github.com/TavisheeAgrwal/Auto_Judge.git
```
Navigate into the project directory:
```bash
cd Auto_Judge
```
Install the required dependencies:
```bash
pip install -r requirements.txt
```
### 2.Launch the AutoJudge web interface
```bash
streamlit run app.py
```
The application will open in your default web browser.
## Saved models
```text
The following trained models are included in the repository:
tfidf_vectorizer.pkl
difficulty_classifier.pkl
score_regressor.pkl
label_encoder.pkl
These are loaded directly by the web interface for inference.
```
## Demo Video
### Demo Video Link:
```text
Click on the link below to watch the demo video for the project:
```

https://drive.google.com/file/d/12ktZYdbsRy8F-yLiin-zWsmxGVaxm1rj/view?usp=sharing
The video demonstrates:
```text
Project overview
Model pipeline
Running the web UI locally
Sample predictions
```
