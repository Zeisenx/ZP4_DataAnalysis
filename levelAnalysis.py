from zplib import zp4

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

from datetime import datetime

"""레벨 통계

플레이어의 레벨이 어느정도 분포되있는지 분석하여
'대중성'을 분석

너무 적은 유저층, 레벨이 높은 게이머들을 대상으로 패치하여
레벨이 낮은 플레이어들을 배척하는것은 아닌지 검토하기 위함

그 반대도 마찬가지
"""

font_name = fm.FontProperties(fname="C:\\Windows\\Fonts\\malgun.ttf").get_name()
matplotlib.rc('font', family=font_name)


def getColorByRank(rank):
    color_kv = {0: "blue",
                1: "red",
                2: "purple",
                3: "green"}
    return color_kv[rank]


data_list = {}
for kv in zp4.get_players_keyvalues():
    if not ("level" in kv):
        continue

    level = int(kv["level"])

    rank = int(kv["rank"]) if "rank" in kv else 0
    rank_color = getColorByRank(rank)

    if not (rank_color in data_list):
        data_list[rank_color] = {}

    if level in data_list[rank_color]:
        data_list[rank_color][level] += 1
    else:
        data_list[rank_color][level] = 1

for k, v in data_list.items():
    plt.bar(v.keys(), v.values(), color=k)

plt.xlabel('레벨')
plt.ylabel('플레이어 수')
plt.savefig('export/level/result_{0}.png'.format(datetime.now().strftime("%Y%m%d")))
plt.show()
