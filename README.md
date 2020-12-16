# ZP4_DataAnalysis
제이센 프로젝트 4의 RPG 데이터에 대한 분석
# 1. 분석 목적
```
- Project ★ : 유지보수의 문제로 인한 실패
- Project -1 : 모듈화로 유지보수 향상, 그러나 운영의 문제로 인한 실패
```
<br></br>
## 1.1 Project -1의 운영 실패 원인
```
- 적극적인 피드백 수용
```
<br></br>
## 1.2 적극적인 피드백 수용으로 실패했다?
게임 디자이너가 부정적인 피드백을 경청해야 할까?(https://www.youtube.com/watch?v=P05ONfLOqmY)
```
- 유저들의 피드백은 주관적임
- 온라인과 포럼에서 본 의견들이 반드시 다수의 관점을 대변하는것은 아님
```
<br></br>
**실제 유저들에게 듣고 수용하였던 피드백**
```
- RPG 레벨 업이 느려서 지루하다. 레벨 업이 빨랐으면 좋겠다.
- 레벨 업을 하더라도 스텟치가 너무 적게 올라가서 스텟치가 높았으면 좋겠다.
```
-> 인플레이션 가속화 및 저렙과 고렙의 격차 유발
<br></br>
## 1.3 결론
```
- 유저들의 피드백을 수용하려면 객관적인 증거가 있어야 함
- 해결책이 아닌 문제를 식별해야한다
```
-> 데이터 분석과 통계를 통해 객관적인 데이터를 도출, 분석이 필요
<br></br>
# 2. 데이터 수집 목표
객관적인 데이터를 토대로 안정적이고 지속적인 운영 및 콘텐츠 개발
<br></br>
# 3. 데이터 수집
```
- 레벨 분포도 > 컨텐츠가 너무 고레벨 유저에게 취중되지 않기 위함
- 직업 분포도
- 무기 구매 선호도
- 맵별로 보스의 사망률
- 맵 난이도별 승률
```
<br></br>
# 4. 데이터 분석 결과
```
- 여러 스텟을 다양하게 제공하여 여러 선택을 하게끔 하고 싶었던것이 목표였으나, 의도되지않게 한 스텟에 취중되어 선택하는 게임 메타가 형성됬다는것을 포착.
- 무기는 타입별로 분류결과 선호도가 매우 높은 무기들이 있다는것을 발견
```
## 4.1 스텟
***
![image](https://github.com/Zeisenx/ZP4_DataAnalysis/blob/master/export/stet/result_20201203.png)
<br></br>
**분석 후 게임 패치 결과**
<br></br>
![image](https://github.com/Zeisenx/ZP4_DataAnalysis/blob/master/export/stet/result_20201217.png)
<br></br>
## 4.2 무기
***
![image](https://github.com/Zeisenx/ZP4_DataAnalysis/blob/master/export/weapon_buy/result_20201217.png)
![image](https://github.com/Zeisenx/ZP4_DataAnalysis/blob/master/export/weapon_buy/Rifle/result_weapon_buy_Rifle_20201217.png)
<br></br>
# 5. 결론

주관적인 유저들의 피드백만을 수집하여 반영하는것보다, 객관적인 데이터와 유저들의 피드백을 적절히 활용하면
의도하고자 했던 설계에 가까워질 수 있는것을 알수 있었음.

추가적으로 느낀점은, 데이터 분석에 있어서
데이터에 좌우되지 않고 **데이터가 어떻게 나왔을까에 대한 이해**가 필요하다 생각되었음.
