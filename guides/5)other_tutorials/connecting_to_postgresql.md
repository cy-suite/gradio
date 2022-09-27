<script type="module" src="https://gradio.s3-us-west-2.amazonaws.com/3.1.0/gradio.js"></script>

# Connecting to PostgreSQL

Related spaces: https://huggingface.co/spaces/freddyaboulton/chicago-bike-share-dashboard

## Introduction

This guide explains how you can use Gradio to connect your app to a database. We will be
connecting to a PostgreSQL database hosted on AWS but gradio is completely agnostic to the type of
database you are connecting to and where it's hosted. So as long as you can write python code to connect
to your data, you can display it in a web UI with gradio 💪

## Overview 
    
We will be analyzing bike share data from Chicago. The data is hosted on kaggle [here](https://www.kaggle.com/datasets/evangower/cyclistic-bike-share?select=202203-divvy-tripdata.csv)
Our goal is to create a dashboard that will enable our business stakeholders to answer the following questions:

1. Are electric bikes more popular than regular bikes?
2. What are the top 5 most popular departure bike stations?


## Step 1 - Creating your database

We will be storing our data on a PostgreSQL hosted on Amazon's RDS service. Create an AWS if you don't already have one
and create a PostgreSQL database on the free tier. 

**Important**: If you plan to host this demo on HuggingFace spaces, make sure database is on port **8080**. Spaces will
block all outgoing connections unless they are made to port 80, 443, or 8080 as noted [here](https://huggingface.co/docs/hub/spaces-overview#networking).
RDS will not let you create a postgreSQL instance on ports 80 or 443.

Once your database is created, download the dataset from Kaggle and upload it to your database.
For the sake of this demo, we will only upload March 2022 data.
 
## Step 2.a - Connect to your database! 

We will be using the `psycopg2` postgreSQL driver for python.
This is not a hard requirement so you can use your preferred driver, like SQLAlchemy.

The first step is to create a connection to the database. With `psycopg2` you can do so like this:

```python
connection = psycopg2.connect(user=os.environ["DB_USER"],
                              password=os.environ["DB_PASSWORD"],
                              host="gradio-bikeshare.cbz6h4welhtp.us-east-1.rds.amazonaws.com",
                              port="8080",
                              database="bikeshare")
```

We will be passing the database username and password as environment variables.
This will make our app more secure by avoiding storing sensitive information as plain text in our application files.

If you were to run our script locally, you could pass in your credentials as environment variables like so

```bash
DB_USER=<username> DB_PASSWORD=<password> python app.py
```

## Step 2.b - Write your ETL code
We will be querying our database for the total count of rides split by the type of bicycle (electric, standard, or docked)
as well as the total count of rides that depart from each station and take the top 5. 

We will then take the result of our query and visualize it in a matplotlib plot.

We can do this with the following code:

```python
def get_count_ride_type():
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT COUNT(ride_id) as n, rideable_type
        FROM rides
        GROUP BY rideable_type
        ORDER BY n DESC
    """
    )
    rides = cursor.fetchall()
    cursor.close()
    fig_m, ax = plt.subplots()
    ax.bar(x=[s[1] for s in rides], height=[s[0] for s in rides])
    ax.set_title("Number of rides by bycycle type")
    ax.set_ylabel("Number of Rides")
    ax.set_xlabel("Bicycle Type")
    return fig_m


def get_most_popular_stations():
    cursor = connection.cursor()
    cursor.execute(
        """
    SELECT COUNT(ride_id) as n, MAX(start_station_name)
    FROM RIDES
    WHERE start_station_name is NOT NULL
    GROUP BY start_station_id
    ORDER BY n DESC
    LIMIT 5
    """
    )
    stations = cursor.fetchall()
    fig_m, ax = plt.subplots()
    ax.bar(x=[s[1] for s in stations], height=[s[0] for s in stations])
    ax.set_title("Most popular stations")
    ax.set_ylabel("Number of Rides")
    ax.set_xlabel("Station Name")
    ax.set_xticklabels(
        [s[1] for s in stations], rotation=45, ha="right", rotation_mode="anchor"
    )
    ax.tick_params(axis="x", labelsize=8)
    fig_m.tight_layout()
    return fig_m
```

## Step 2.c - Write your gradio app
We will display or matplotlib plots in two separate `gr.Plot` components. We will fetch the latest data from the
database each time the application loads.

```python
with gr.Blocks() as demo:
    with gr.Row():
        bike_type = gr.Plot()
        station = gr.Plot()

    demo.load(get_count_ride_type, inputs=None, outputs=bike_type)
    demo.load(get_most_popular_stations, inputs=None, outputs=station)

demo.launch()
```

## Step 3 - Deployment
We will be deploying our app to HuggingFace spaces. If you wish, you could also run your app locally and get a
shareable link by passing the `share=True` parameter to `launch`.

If you haven't used spaces before, follow the previous guide [here](/using_hugging_face_integrations).
You will have to add the `DB_USER` and `DB_PASSWORD` variables as "Repo Secrets". You can do this in the "Settings" tab.

![secrets](/assets/guides/secrets.png)

## Conclusion
Congratulations! You know how to connect your gradio app to a database hosted on the cloud! ☁️

You can checkout the finished product below

<gradio-app space="freddyaboulton/chicago-bike-share-dashboard"> </gradio-app>

as well as [here](https://huggingface.co/spaces/freddyaboulton/chicago-bike-share-dashboard).
 
As you can see, gradio gives you the power to connect to your data wherever it lives and display however you want! 🔥