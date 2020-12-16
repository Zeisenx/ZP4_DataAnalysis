
from zplib import zp4

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

font_name = fm.FontProperties(fname="C:\\Windows\\Fonts\\malgun.ttf").get_name()
matplotlib.rc('font', family=font_name)

data_list = {}
for kv in zp4.get_players_keyvalues():
    if not "class" in kv:
        continue

    if int(kv["level"]) < 40:
        continue

    if kv["class"] in data_list:
        data_list[kv["class"]] += 1
    else:
        data_list[kv["class"]] = 1

data_list = {k: v for k, v in sorted(data_list.items(), key=lambda x: x[1], reverse=True)}

plt.bar(data_list.keys(), list(data_list.values()))
plt.show()