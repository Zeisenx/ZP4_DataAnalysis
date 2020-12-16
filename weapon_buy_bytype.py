
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

import os

from datetime import datetime
from zplib import data_path
from valve_keyvalues_python.keyvalues import KeyValues

# 총기 분석타입, Pistol이면 피스톨 통계
ANALYSIS_TYPE = "Sniper"

#한글 글꼴 설정
font_name = fm.FontProperties(fname="C:\\Windows\\Fonts\\malgun.ttf").get_name()
matplotlib.rc('font', family=font_name)

kv = KeyValues(filename=data_path.stats)

weapon_buydict = kv["statistics"]["weapon_buy"]

type_dict = {
    "Pistol": ["glock", "hkp2000", "usp_silencer", "p250", "fiveseven", "tec9", "cz75a", "deagle", "revolver"],
    "Shotgun": ["nova", "xm1014", "mag7", "sawedoff"],
    "SMG": ["mp9", "mac10", "mp7", "ump45", "mp5sd", "p90"],
    "Rifle": ["galilar", "famas", "ak47", "m4a1", "m4a1_silencer", "sg556", "aug"],
    "Sniper": ["ssg08"],
    "Heavy Rifle": ["m249", "negev"]
}

grenades_list = ["weapon_hegrenade", "weapon_flashbang", "weapon_smokegrenade",
            "weapon_molotov", "weapon_incgrenade", "weapon_decoy"]

items_list = ["item_defuser", "item_kevlar", "item_assaultsuit"]

delete_list = items_list + grenades_list
for i in delete_list:
    if not (i in weapon_buydict):
        continue
    del weapon_buydict[i]

for i in weapon_buydict.copy():
    ok = False
    for o in type_dict[ANALYSIS_TYPE]:
        if i == "weapon_" + o:
            ok = True
    if not ok:
        del weapon_buydict[i]


for weapon in weapon_buydict.copy():
    weapon_buydict[weapon] = int(weapon_buydict[weapon])

df = pd.DataFrame.from_dict(weapon_buydict, orient='index', columns=['count'])
total = df['count'].sum()

df['percentage'] = df["count"] / total

df.index = pd.Index(i.replace("weapon_", "") for i in df.index.tolist())

# 무기 구매 비율 통계 계산
plot, texts = plt.pie(df['percentage'], normalize=True, radius=1.0)
labels = ['{0} - {1:.2f}％'.format(x, y * 100.0) for x, y in zip(df.index.tolist(), df['percentage'])]
plot, labels, dummy = zip(*sorted(zip(plot, labels, df['percentage']), key=lambda x: x[2], reverse=True))
plt.legend(plot, labels)
plt.title('무기 구매비율 통계')

dir = 'export/weapon_buy/{0}'.format(ANALYSIS_TYPE)
if not os.path.exists(dir):
    os.makedirs(dir)

plt.savefig(dir + '/result_weapon_buy_{0}_{1}.png'.format(ANALYSIS_TYPE, datetime.now().strftime("%Y%m%d")))

plt.show()