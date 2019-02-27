# This is "R to Py" Repo
> Driving_score_estimation_project (18. 12. 26 ~)

## Table of Contents
- [Information about these files](#information-about-thest-files)

### Information about these files
> .csv files
  - driving_score_180ea.csv
    + Search by google images, 182ea
  - driving_score_new.csv
    + Search by google images, 12ea
  - Tmap_data.csv
    + Data given by Professor, 15ea
    
> .py files
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
