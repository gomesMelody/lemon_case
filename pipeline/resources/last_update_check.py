class CheckCurrentData:
    def __init__(self, current_time_file):
        self.current_time_file = current_time_file

    def check_current_data_time(self):
        import json
        from datetime import datetime
        current_info_time = None
        try:
            with open(self.current_time_file, "r") as f:
                json_data = json.load(f)

            current_info_time = datetime.strptime(json_data['current_info_time'], '%Y-%m-%d %H:%M:%S%z')
        except Exception as e:
            raise Exception(e)
        return current_info_time

    def update_current_time_json(self, last_updated):
        import json
        from datetime import datetime
        new_date_time = {
            "current_info_time": str(last_updated)
        }
        with open(self.current_time_file, "w") as fw:
            json.dump(new_date_time, fw)
