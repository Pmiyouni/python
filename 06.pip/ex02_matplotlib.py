import matplotlib.pyplot as plt
from matplotlib import font_manager, rc


#한글 깨짐 방지
plt.rcParams['font.family'] = "Malgun Gothic"
plt.rcParams['axes.unicode_minus'] = False


#plt.plot([1,2,3,4],[3,6,10.12])
x_values=[1,2,3,4]
y_values=[3,6,10,12]
plt.plot(x_values,y_values,"o--")
# o 선없음 / o- 실선/ o-- 점선 각  다르게 표시
plt.xlabel("x 축")
plt.ylabel("y 축")
plt.show()
# show로 그래프 표시


