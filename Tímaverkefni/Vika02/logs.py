class Logs():
    def __init__(self):
        self.log_dict = {
                1: ["Aron", 8, 17],
                2: ["Tómas", 9, 12],
                3: ["Logi", 12, 16],
                4: ["Sölvi", 13, 14]
                }

    def add_log(self, time, name, start, end):
        self.log_dict[len(self.log_dict) + 1] = [name, start, end]
        
    def all_logs(self):
        result = ""
        for i, j in self.log_dict.items():
            result += f"{i}: {j}\n"
        del result[-1]
        return result
    
    def specific_time(self, start_time, end_time):
        all_logs = self.all_logs()
        logs = all_logs.split("\n")
        print(logs)
        for log in logs:
            name_time = log.split(",")
            start = int(name_time[-2])
            end = name_time[-1]
            end = int(end[:-1])
            print(start, end)


    def delete_log(self):
        # delete a specific log from the dict
        # successful message
        pass
    
    def newest_log(self):
        # return the newest log as a string
        pass
    
    def __str__(self):
        # print the message
        pass

logs = Logs()
logs.specific_time(12, 24)