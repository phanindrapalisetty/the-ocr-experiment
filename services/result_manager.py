#%%
import json 

def get_all_text_page_wise(str_dict:str):
    if str_dict.__contains__('allText') == False:
        raise ValueError("Something is off in ocr result. Should contain allText key")
    else:
        result_ = {}
        dict_ = json.loads(str_dict)
        for key_, value_ in dict_.items():
            result_.update({key_: value_['allText']})
        
        return json.dumps(result_)
