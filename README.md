<img src="/images/mop-black.png" alt="drawing" width="100"/>

**Melbourne Open Data Playground**
==================================
Last Updated: 9-Dec-2021

An initiative of the [Deakin University Industry Student Capstone (DISC) Program](https://www.discprojects.com/) for the [City of Melbourne](https://data.melbourne.vic.gov.au/).

# About

Welcome to the Melbourne Open Data Playground GitHub community page.

Melbourne Open Data Playground (MOP) is a capstone project sponsored by Deakin University.

Since Covid there is more demand for data by the business community to support their decision making. This project is meant to align to two strategic documents from Melbourne City Council:

- **The Economic Development Strategy to be a digitally-connected city.**
- **The 2021-2025 Council Plan which outlines the specific objective of delivering programs that will build digital literacy skills and capabilities.**

The City of Melbourne is an Australian leader in Open Data since 2014. The latest research and local user engagement has identified a gap where users would like to learn more abut how to access the Open Data and how to gain insights from the data to build apps and solve city problems.

This project aims to deliver proof-of -concept examples on how calls to Open Data API can be made to deliver a variety of solutions.

In this GitHub repository you can access a wide variety of example Jupyter notebooks that let you explore, visualise and analyse Open Data published by the City of Melbourne.

By publishing these notebooks, we aim to increase adoption and use of City of Melbourne Open Data to support the business, research and development community. 

---


What is in this repository?
=====

This repository contains :
- [Example Jupyter Notebooks](example_notebooks/)


---

How do I start analysing Open Data?
=======================

The first step in analysisng open data is to clearly define the question you are aiming to answer or the problem you are trying to solve.

Data Analysts can often begin with a brainstorming session with relevant stakeholders.
In this activity you should aim to answer the following:

1. What is the question you want to answer or hypothesis you wish to test.
2. What type of data do you think you will need.
3. How will you communicate your results or insights ie. what type of visualisation do you wish to use.
   
The type of visualisation will depend on the question you’re trying to answer and the nature of the data used.

In the diagram below, we have shown different visualizations for different categories of problems.
These categories explore common questions and types of data you may want to display in a visualization.

![Image](https://content.codecademy.com/programs/dataviz-python/unit-3/pickachart.svg?sanitize=true)



---




## 1. Reading a dataset



Showing summary table of 222 datasets (By Sodapy)




```python
>>> from sodapy import Socrata
>>> client = Socrata(
        "sandbox.demo.socrata.com",
        "FakeAppToken",
        username="fakeuser@somedomain.com",
        password="mypassword",
        timeout=10
    )
```




---
## 2. Manipulation

* [Click here to see example code](/example_notebooks/tutorials/001-UsingSodapyandBuildingETL.ipynb) for **Data Description**.


---

![image](/images/demo.png)

THIS SECTION IS INCOMPLETE FROM LAST TRIMESTER!
>Create EDA Code:
Plz create file with your EDA code.
Do not merge your code into **example.ipynb** file)



## 3. Analysis  

* [Click here](/example_notebooks/tutorials/001-UsingSodapyandBuildingETL.ipynb) to see example code for **EDA**

Open the link ["Geo_Map.html"](/images/Geo_Map.html) with your browser to check the parking status. 

Different colored icons are used to distinguish the availability of parking Spaces.Red means the parking space is occupied, and blue means the parking space is available. 

When you select a specific icon, you can see the specific status of the parking space.
Bay_id:The unique ID of the parking bay where the parking sensor is located.If you encounter any situation on the street, the Bay ID will be able to quickly locate you.
Status:The status will either display: Occupied – A car is present in the parking bay at that time. Unoccupied – The parking bay is available at that time.Help you quickly find available parking.
Description:A compact, semi-human-readable description of the overall restrictions.If you're interested in free parking time, then this is perfect for you.
Duration:The time (in minutes) that a vehicle can park at this location.
Disability:For bays that aren't limited to disabled permits, how much time (minutes) a vehicle with disabled permit can spend in the spot. Usually twice the regular amount of time.

The screenshot below:

![image](/images/geo.PNG)


