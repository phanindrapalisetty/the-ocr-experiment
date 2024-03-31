#%%
status_dict = {
    1: "Pending",
    2: "Approved",
    3: "Rejected"
}

status_values = [y for x, y in status_dict.items()]
status_keys = [y for y in status_dict]

class StatusManager:
    def __init__(self, status):
        if not isinstance(status, int):
            raise TypeError("Status must be an integer.")

        self._status_dict = status_dict

        if status not in self._status_dict:
            raise ValueError("Invalid status value. Must be one of 1, 2, or 3.")

        self.status = status

    def get_status_value(self):
        return self._status_dict[self.status]
    
    def get_status_key(self):
        return self.status
# %%
