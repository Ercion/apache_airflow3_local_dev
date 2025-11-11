from setuptools import setup, find_packages

setup(
    name="my_project",
    version="0.1.0",
    packages=find_packages(include=["dags", "dags.*"]),  # Include the dags folder
    install_requires=[
        "apache-airflow",
    ],
)
