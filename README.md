# Electoral Bond Analysis 

### Method:
##### Conversion of pdf to csv 
- Run [pdf_to_csv.py](./pdf_to_csv.py) file.
-Then covert csv to tables of sql database.

> The above steps are already done, and files can be found in [data](./data/) folder.

#### Steps to run locally.
##### Adding to the database
- Import the sql file in MySQL Workbench. ![](https://i.imgur.com/I8Q0Jhv.png)
- Choose the sql dump and start import. ![](https://i.imgur.com/IdHYRDo.png)
- Run the following command in SQL File:<br>
  `CREATE USER 'Test'@'%' IDENTIFIED BY 'Test';`<br>
  `GRANT ALL PRIVILEGES ON *.* TO 'Test'@'%' WITH GRANT OPTION;`

##### Activate a virtual environment (Optional)
- `pip install virtualenv`
- `virtualenv venv`
- `cd venv/Scripts`
- `activate`
- `cd ../..`

##### Run the main.py
- `pip install -r requirements.txt`
- `python main.py`
- Navigate to [(http://127.0.0.1:8080)]

  ### Video of Working
  ![](https://youtu.be/I4Pb1_JGbpE)<br>

#### Home:

![](https://i.ibb.co/0MPPh0h/Home.png)<br>

#### Q2:

![](https://i.ibb.co/p0tq2TK/Question2.png)<br>

#### Q3:

![](https://i.ibb.co/W396j8V/Question3.png)<br>

#### Q4:

![](https://i.ibb.co/LSPfjCF/Question4.png)<br>


#### Q5:

![](https://i.ibb.co/Rgwyryd/Question5.png)<br>

#### Q6:

![](https://i.ibb.co/KN29nms/Question6.png)<br>



## The readme part is inspired from Jaskirat Singh Maskeen (23110146)
