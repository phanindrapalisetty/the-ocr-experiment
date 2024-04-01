#%%
import os 
def get_file_extension(file_path):
    if os.path.isfile(file_path):
        file_name, file_extension = os.path.splitext(file_path)
        return file_extension[1:].lower()


# %%
