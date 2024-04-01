#%%
from paddleocr import PaddleOCR
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
path_ = '/home/phani/Desktop/phanindra-resume-06012024.pdf'
result_ = get_paddle_ocr(path_)
# %%
def get_entire_text(filepath: str,
                        ocr_type: str = 'paddle'):
    valid_ocr_types = ['paddle']
    if ocr_type not in valid_ocr_types:
        raise ValueError(f'ocr_type should be one of {valid_ocr_types.split()}')
    else:
        if ocr_type == 'paddle':
            dict_ = {}
            res_ = get_paddle_ocr(filepath)
            for i in range(len(res_)):
                entireText = entireText + f"page_{i}\n"
                for j in range(len(res_[i])):
                    pass