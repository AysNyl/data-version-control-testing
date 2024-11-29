import pandas as pd
import requests


def bhav_data_imp(start_date: str, end_date: str, destination: str = ".") -> list:
    """Dates should be in dd/mm/yyyy format."""

    open_dates = pd.bdate_range(start_date, end_date)
    open_dates
                        
    dowloaded_files = []
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
    }

    for open_date in open_dates:

        link = "https://nsearchives.nseindia.com/products/content/sec_bhavdata_full_{}.csv".format(
            open_date.strftime("%d%m%Y")
        )
        file_name = link.split("/")[-1]

        try:
            r = requests.get(link, headers=headers, timeout=3)
            print(link)
        except requests.ReadTimeout:
            continue

        with open("{}/{}".format(destination, file_name), "wb") as csv_file:
            csv_file.write(r.content)
            dowloaded_files.append(file_name)

    return dowloaded_files
