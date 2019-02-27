# This is "R to Py" Repo
> Driving_score_estimation_project (18. 12. 26 ~)  
  + Related Paper : [A Genetic Programming Approach for Driving Score Calculation in the Context of Intelligent Transportation Systems](https://ieeexplore.ieee.org/document/8410904)

## Table of Contents
- [Information about these files](#information-about-these-files)  
  + [.csv files](#csv-files)  
  + [.py files](#py-files)

### Information about these files
##### .csv files
  - `driving_score_180ea.csv`
    + Search by google images, 182ea
  - `driving_score_new.csv`
    + Search by google images, 12ea
  - `Tmap_data.csv`
    + Data given by Professor, 15ea
    
##### .py files
  - `DSI.py`
    + Safety Index model ( = Linear model )
      * Input data : .csv file ( compliance, acceleration, deceleration )
      * Output : RSME ( Root Square Mean Error )
  - `RF.py`
    + Random Forest model
      * Input data : .csv file ( compliance, acceleration, deceleration )
      * Output : RSME ( Root Square Mean Error )
  - `SVM.py`
    + Support Vector Machine
      * Input data : .csv file ( compliance, acceleration, deceleration )
      * Output : RSME ( Root Square Mean Error )
