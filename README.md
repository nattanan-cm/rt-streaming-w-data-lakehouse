# Realtime Streaming With Data Lakehouse
This project demonstrates a robust and scalable architecture for real-time data streaming using a Data Lakehouse approach. Leveraging Python, Minio, Kafka, Spark, and Docker, the setup allows for efficient ingestion, processing, and storage of streaming data.

## Getting Started
To get this project up and running on your local machine, follow these steps

#### Clone the repository
```sh
git clone https://github.com/nattanan-cm/rt-streaming-w-data-lakehouse.git
cd rt-streaming-w-data-lakehouse
```

#### Docker
###### Start docker
```sh
docker compose up -d
```
###### Stop docker
```sh
docker compose down
```

#### Create and activate a virtual environment (optional but recommended)
```sh
python -m venv <your_env_name>
$ source <your_env_name>/bin/activate # For macOS/Linux
$ <your_env_name>\Scripts\activate # For Windows
```


#### Install the required packages
```sh
pip install minio pandas pyspark python-dotenv
```
 
## Data Source
UCI Machine Learning Repository. This repository, maintained by the University of California, is commonly used in many online courses.
The key feature of the UCI website is that the data has already been filtered by the site administrators, making it easy to use. Additionally, the data is organized by problem type (e.g., Classification, Regression, Clustering), and the number of rows, columns, and column types (Categorical, Numerical, Mixed) are also provided.

https://archive.ics.uci.edu/

## Contributing
Contributions are welcome! Please fork this repository and submit a pull request for any improvements or bug fixes.

## Contact
<picture> <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/socials/linkedin-dark.svg" /> <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/socials/linkedin.svg" /> <img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/socials/linkedin.svg" width="32" height="32" /> </picture
