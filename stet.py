from valve_keyvalues_python.keyvalues import KeyValues
import glob
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from zplib import zp4

from datetime import datetime

font_name = fm.FontProperties(fname="C:\\Windows\\Fonts\\malgun.ttf").get_name()
matplotlib.rc('font', family=font_name)

pdDataList = []
stetList = ["health", "power", "speed", "armor"]

for kv in zp4.get_players_keyvalues():
    dataList = []
    if not ("stet" in kv):
        continue

    # if not ("class" in kv) or kv["class"] != "supporter":
    #     continue

    dataList.append(int(kv["level"]))
    for keyName in stetList:
        try:
            dataList.append(int(kv["stet"][keyName]))
        except:
            dataList.append(0)
    pdDataList.append(dataList)

df = pd.DataFrame(pdDataList, columns=["level"] + stetList)

data = df[df['health'] != 0]
plt.scatter(data['level'], data['health'], c='blue', label='체력')

data = df[df['power'] != 0]
plt.scatter(data['level'], data['power'], c='r', label='근력')

data = df[df['speed'] != 0]
plt.scatter(data['level'], data['speed'], c='g', label='민첩')

#data = df[df['armor'] != 0]
#plt.scatter(data['level'], data['armor'], c='purple', label='방어력')

plt.xlabel('레벨')
plt.ylabel('스텟')
plt.legend()
plt.savefig('export/stet/result_{0}.png'.format(datetime.now().strftime("%Y%m%d")))
plt.show()