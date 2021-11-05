# Loan_Prediction
This Machine Learning project is to choose the best model that will classify how much loan the user can take.

<h3> 1. Getting the system ready and loading the data </h3>

Required packages are imported and data is loaded into the workplace (Spyder) 

<h3> 2. Understanding the data</h3>

First, data is copied and assigned to different variable otherwise dataset changes due to applications.
Then every column that has object variables are changed into float and integer variables and get information about dataset.

<h3> 3. Visualizing the data</h3>

Variables in the data and their correlation with each other are shown and this process helps us to understand the variables and their relations with each other better.

![image](https://user-images.githubusercontent.com/59616968/140579493-8a74031d-7181-4d5e-8e49-8482a15d1f83.png)

Such as this graph data visualization helps us to understand intercourse between loan emount and income of the applicant

<h3> 4. Model Building </h3>

A function to gather all algorithms into a list is created, functions help to keep code clean so i try to use functions everytime possible, then a for loop is composed 
in order to try every model algorithms in the models list and print out the Mean Squared Error, Root Mean Squared Error, Mean Absolute Error and R Squared values of the each
algorithms. 

Results are shown below:

1. Linear Regression Model<br>
LR's MSE:3277.0949657063275<br>
LR's RMSE:57.245916585432774<br>
LR's MAE:38.109637212511636<br>
LR's R2 Score:0.32028914298496636<br>
***********************

2. Decision Tree Regressor Model<br>
DTR's MSE:5043.142857142857<br>
DTR's RMSE:71.01508893990669<br>
DTR's MAE:46.6530612244898<br>
DTR's R2 Score:-0.04601147948087925<br>
***********************

3. Lasso Model<br>
Lasso's MSE:3232.1538516788005<br>
Lasso's RMSE:56.852034718898146<br>
Lasso's MAE:38.00929523530968<br>
Lasso's R2 Score:0.32961049724858227<br>
***********************

4. Support Vector Regression Model<br>
SVR's MSE:4830.0192688922<br>
SVR's RMSE:69.49834004414926<br>
SVR's MAE:48.2317415787011<br>
SVR's R2 Score:-0.0018069573855754584<br>
***********************

<h2> Result </h2>

it seems Lasso model is the best algorithm for this prediction problem. However everytime i run my code it gives different results if you know the reason please comment or 
contact me. 


 


  

  
