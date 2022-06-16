import numpy as np

def calc_outliers(var):
    Q3 = np.percentile(var, 75) 
    Q1 = np.percentile(var, 25)

    print("upper quartile:", Q3,  
        "\nlower quartile:", Q1)
  
    IQR = 1.5*(Q3 - Q1)

    LB = Q1 - IQR
    UB = Q3 + IQR

    print("Lower Bound of outliers:", round(LB, 2), "\nUpper Bound of outliers:", round(UB, 2)) 

    return LB, UB