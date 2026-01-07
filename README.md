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
Checked for missing values.
Plotted graphs and conducted detailed eda to find hidden trends.

2.Feature Extraction:
Dropped unnecessary columns like sample_io andd url.
Combined all the textual columns into one and later on discarded the individual columns.
Constructed addditional features like text_len , math_density etc .
Conducted vectorization usinf TF-IDF for the textual column.
Combined the vectorised and additional features.


This converted raw text into numerical feature vectors suitable for machine learning models.

## Model

### Model 1 : Classification 
```text
Objective: Predict difficulty class (Easy / Medium / Hard)
Model Used: XG Boost Classifier
```

### Model 2: Regression-
```text
Objective: Predict numerical difficulty score
Model Used: XG Boost Regressor
```
## Evaluation Metrics
### Classification Performance
Accuracy:
56 %
Confusion Matrix:
```text
              precision    recall  f1-score   support

        easy       0.57      0.35      0.43       136
        hard       0.62      0.76      0.68       425
      medium       0.40      0.34      0.37       262
```
