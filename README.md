# Auto_Judge
##Introduction
This is a tool built for judging the difficulty levels and alloting scores for coding problems.
Online programming platforms categorize problems by difficulty level and assign difficulty scores, which are typically determined through human judgment and user feedback. 
This project proposes AutoJudge, an automated system that predicts the difficulty class (Easy, Medium, Hard) and a numerical difficulty score for programming problems using only their textual descriptions.
This project demonstrates the complete ML pipeline, including preprocessing, feature extraction, classification, regression, evaluation, and deployment via a web UI.

##Dataset Used
```text
The dataset consists of programming problems collected from online competitive programming platforms. Each data sample contains the following fields:
•	“title”                                   Problem name
•	“description”                      Detailed textual description of the problem
•	“input_description”          Textual Description of the input
•	“output_description”       Textual Description of the output
•	“sample_io”                        Sample for how input/output will be entered
•	“problem_class”                Problem classification into easy/medium/hard
•	“problem_score”               Score allotted based on difficulty
•	“url”                                     Link to the problem
```
