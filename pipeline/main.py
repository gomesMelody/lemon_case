from selenium import webdriver
import json
from resources.aneel_source_crawler import AneelSourceCrawler
from resources.last_update_check import CheckCurrentData
from resources.data_processing import AneelDataProcessing

with open("./conf.json", "r") as conf:
    config = json.load(conf)

ccd = CheckCurrentData(config["current_update_file"])
current_info_time = ccd.check_current_data_time()

## Retrieve last updated time from source
homepage = config["aneel_homepage"]
options = webdriver.ChromeOptions()
options.add_argument('--headless')

sdc = AneelSourceCrawler(webdriver,options, homepage)
last_updated = sdc.get_last_updated_source_time()

## Check if there is update on the source

if last_updated <= current_info_time:
    print("info ja esta atualizada")

else:
    print("Atualizacao encontrada!")

    sdc.download_latest_data_source(config["aneel_download_page"], "./source_files")

    adp = AneelDataProcessing()
    adp.process_updated_data(config["updated_file_name"])

    ccd.update_current_time_json(last_updated)
