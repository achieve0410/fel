# This is "R to Py" Repo
> Driving_score_estimation_project (18. 12. 26 ~)  
  + Related Paper : [A Genetic Programming Approach for Driving Score Calculation in the Context of Intelligent Transportation Systems](https://ieeexplore.ieee.org/document/8410904)

## Table of Contents
- [Information about these files](#information-about-these-files)  
  + [.json files](#json-files)
  + [.csv files](#csv-files)  
  + [.py files](#py-files)

### Information about these files

##### .json files
  - `test.json`
    + from csv file

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
      * Input data : .csv file ( compliance, acceleration, deceleration, result )
      * Output : RSME ( Root Square Mean Error )
  - `DSI_json.py`
    + Safety Index model ( = Linear model )
      * Input data : .json file ( header: { number: }, data: { compliance: , acceleration: , deceleration: , result: } )
      * Output : RSME ( Root Square Mean Error )
  - `DSI_sql.py`
    + Safety Index model ( = Linear model )
      * Input data : connection with mysql db
      * Output : RSME ( Root Square Mean Error )
  - `RF.py`
    + Random Forest model
      * Input data : .csv file ( compliance, acceleration, deceleration, result )
      * Output : RSME ( Root Square Mean Error )
  - `RF_json.py`
    + Random Forest model
      * Input data : .json file ( header: { number: }, data: { compliance: , acceleration: , deceleration: , result: } )
      * Output : RSME ( Root Square Mean Error )
  - `RF_sql.py`
    + Random Forest model
      * Input data : connection with mysql db
      * Output : RSME ( Root Square Mean Error )
  - `SVM.py`
    + Support Vector Machine
      * Input data : .csv file ( compliance, acceleration, deceleration, result )
      * Output : RSME ( Root Square Mean Error )
  - `SVM_json.py`
    + Support Vector Machine
      * Input data : .json file ( header: { number: }, data: { compliance: , acceleration: , deceleration: , result: } )
      * Output : RSME ( Root Square Mean Error )
  - `SVM_sql.py`
    + Support Vector Machine
      * Input data : connection with mysql db
      * Output : RSME ( Root Square Mean Error )
  - `toJson.py`
    + Make .json file from csv file(or user data)
      * Input data : .csv file ( compliance, acceleration, deceleration, result )
      * Output : .json file ( data, # of data )
  - `pymyquery.py`
    + Connecting mysql and python Testing code
      * Input data : connection with mysql db
      * Output : db data
