class AneelSourceCrawler:
    def __init__(self, webdriver, options, homepage):
        self.homepage = homepage
        self.webdriver = webdriver
        self.options = options

    def get_last_updated_source_time(self):
        from selenium.webdriver.common.by import By
        from datetime import datetime
        last_updated = None
        try:
            driver = self.webdriver.Chrome(options=self.options)
            driver.get(self.homepage)

            additional_info = driver.find_element(By.CLASS_NAME, "additional-info")
            info_list = additional_info.find_elements(By.TAG_NAME, "tr")

            for info in info_list:
                label = info.find_element(By.TAG_NAME, 'th').text

                if label == 'Última Atualização':
                    value = (info.find_element(By.TAG_NAME, 'span')).get_attribute('data-datetime')
                    last_updated = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S%z')
                    break

            driver.close()
            return last_updated
        except Exception as e:
            driver.close()
            raise Exception(e)

    def download_latest_data_source(self, url, save_folder):
        import os
        import requests
        import time

        # Create the save folder if it doesn't exist
        os.makedirs(save_folder, exist_ok=True)

        # Send a GET request to the download page
        response = requests.get(url, stream=True)

        if response.status_code == 200:
            # Extract the filename from the URL
            filename = url.split('/')[-1]

            # Construct the file path where the CSV will be saved
            save_path = os.path.join(save_folder, filename)

            # Save the CSV file
            with open(save_path, 'wb') as file:
                total_size = int(response.headers.get('Content-Length', 0))
                downloaded_size = 0
                start_time = time.time()
                for chunk in response.iter_content(chunk_size=4096):
                    if chunk:
                        file.write(chunk)
                        downloaded_size += len(chunk)
                        # Calculate the download progress
                        progress = (downloaded_size / total_size) * 100
                        # Print the progress
                        print(f"Download progress: {progress:.2f}%")
                elapsed_time = time.time() - start_time
            print(f"Download complete! File saved to {save_path}")
            print(f"Total time elapsed: {elapsed_time:.2f} seconds")

            return True
        else:
            print("Error: Failed to download the CSV file")
            return False





