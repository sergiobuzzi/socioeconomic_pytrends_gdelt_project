# Socioeconomic Pytrends project.

Google Trends is a Google tool that analyses the popularity of top search queries in Google Search across various regions and languages. Basically, what people are looking for in Google.

The project consist on the following:

- Pytrends:
    1. Monitoring a concrete keywords along time in Spain: "empleo","desempleo","crisis","corrupcion","centro de salud", "hospital" (employment, unemployment, crisis, corruption, clinic, "hospital")

    2. Find the top keywords related to the ones above in time.  

- Bash:
    - Execute periodically the Python script.

- GCP:
    - Connect the script to Google Cloud Storage
    - Connect stored info to Google Datastudio. The graph will be fed automatically along time.
    - Display the graphs fo **1** and **2** for last years and also for last month.

This is something that worths doing with the Gdelt Project and BigQuery https://www.gdeltproject.org/ , but from the point of what people are looking for, not just what appears in the news.


# Documentation:

- What is Google Trends (no code)   https://www.karinakumykova.com/2019/03/calculate-search-interest-with-pytrends-api-and-python/

- List of categories: https://github.com/pat310/google-trends-api/wiki/Google-Trends-Categories

- Official documentation: https://pypi.org/project/pytrends/
- Info about how it works: https://www.karinakumykova.com/2019/03/calculate-search-interest-with-pytrends-api-and-python/
- The "real" Google Trends: https://towardsdatascience.com/google-trends-api-for-python-a84bc25db88f
- A great tutorial https://searchengineland.com/learn-how-to-chart-and-track-google-trends-in-data-studio-using-python-329119


