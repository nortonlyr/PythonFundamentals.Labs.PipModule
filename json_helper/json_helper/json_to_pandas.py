#jason to pandas
import pandas as pd
import json
import os
from typing import Dict


def read_all_json_files(JSON_ROOT):
    for dirpath, dirname, filenames in os.walk(JSON_ROOT):
        result = []
        for f in filenames:
            if f.endswith('.json'):
                json_content = read_json(os.path.join(JSON_ROOT, f))
                for i in json_content['results']:
                    #i['source'] = f 
                    result.append(i)
    df = pd.DataFrame(result)
    return df