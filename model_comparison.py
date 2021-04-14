from fomlads.data.external import import_for_classification
import pandas as pd
from logistic import fit_evaluate_logistic
from RandomForest import rf_main
from preprocessing import pre_process


def main(ifname, input_col = None,  target_col=None, experiment = None):
     """
     TO CALL: python model_comparison.py Churn_Modelling.csv Exited Logistic_Regression CreditScore,Geography,Gender,Age,Tenure,Balance,NumOfProducts,HasCrCard,IsActiveMember,EstimatedSalary    ----------

    Imports the data-set and generates exploratory plots
    ifname -- filename/path of data file.
    input_cols -- list of column names for the input data
    target_col -- column name of the target data
    classes -- list of the classes to plot
    experiment -- name of the model you want to test (Logistic_Regression, Random_Forest, Fisher, KNN)
    """
     data, inputs, targets, field_names, classes = import_for_classification(ifname, target_col=target_col)
     

     test_ratio = 0.2
     X_train, y_train, X_test, y_test = pre_process(data, field_names, target_col, test_ratio)

     if experiment == "Logistic_Regression":
        fit_evaluate_logistic(X_train, y_train, X_test, y_test)
     elif experiment == "Random_Forest":
        rf_main(X_train, y_train, X_test, y_test)
    #elif experiment = "Fisher":
    #elif experiment = "KNN":



if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        main() # calls the main function with no arguments
    else:
        # assumes that the first argument is the input filename/path
        if len(sys.argv) == 2:
            main(ifname=sys.argv[1])
        else:
            target_col = sys.argv[2]
            if len(sys.argv) == 3:
                main(
                    ifname=sys.argv[1],
                    target_col=target_col)
            # assumes that the fourth argument is the list of input columns
            else:
                experiment = sys.argv[3]
                main(
                    ifname=sys.argv[1], 
                    target_col=target_col, experiment=experiment)
                if len(sys.argv) == 4:
                    input_cols = sys.argv[4].split(',')
                    main(
                        ifname=sys.argv[1], input_col= input_cols,
                        target_col=target_col, experiment=experiment)