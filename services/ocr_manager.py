#%%
from paddleocr import PaddleOCR
import json


ocr = PaddleOCR(use_angle_cls = True, 
                    lang = 'en', 
                    use_space_char = True,
                    use_dialiation = True,
                    enable_mkldnn = True)
# %%
def get_paddle_ocr(filepath):
    true = True 
    false = False 

    res = ocr.ocr(filepath, cls = True)

    return res 

# /home/phani/Desktop/phanindra-resume-06012024.pdf
# %%

# %%
def get_paddle_ocr_results(filepath):
    dict_ = {}
    inner_dict = {}
    res_ = get_paddle_ocr(filepath)
    
    for i in range(len(res_)):
        result = res_[i]
        allText = ''
        
        for j in range(len(res_[i])):
            allText = allText + res_[i][j][1][0] + ' '
        dict_.update(
            {
                f"page_{i+1}" : {
                    "allText": allText
                }
            }
        )
    return json.dumps(dict_)


def get_ocr_results(filepath: str,
                        ocr_type: str = 'paddle'):
    valid_ocr_types = ['paddle']
    if ocr_type not in valid_ocr_types:
        raise ValueError(f'ocr_type should be one of {valid_ocr_types.split()}')
    else:
        if ocr_type == 'paddle':
            result = get_paddle_ocr_results(filepath)
        return result
# %%
if __name__ == "__main__":
    print(1)
