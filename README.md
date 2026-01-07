# Auto_Judge
##Introduction
This is a tool built for judging the difficulty levels and alloting scores for coding problems.
Online programming platforms categorize problems by difficulty level and assign difficulty scores, which are typically determined through human judgment and user feedback. 
This project proposes AutoJudge, an automated system that predicts the difficulty class (Easy, Medium, Hard) and a numerical difficulty score for programming problems using only their textual descriptions.
This project demonstrates the complete ML pipeline, including preprocessing, feature extraction, classification, regression, evaluation, and deployment via a web UI.

##Dataset Used
The dataset consists of programming problems collected from various online competitive programming platforms. Each data sample represents a single problem and includes both textual descriptions and difficulty annotations.

Dataset Fields

title
The name or title of the programming problem.

description
A detailed textual explanation of the problem statement, including background and task requirements.

input_description
A textual description of the expected input format and constraints.

output_description
A textual description of the expected output format.

sample_io
Example input and output illustrating how the problem should be solved.

problem_class
The categorical difficulty level assigned to the problem (Easy, Medium, or Hard).

problem_score
A numerical score representing the relative difficulty of the problem.

url
A link to the original problem source on the competitive programming platform.
