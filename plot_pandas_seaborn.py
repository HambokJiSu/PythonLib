import numpy as np
from matplotlib import pyplot as plt

# 그래프에서 마이너스 폰트 깨지는 문제에 대한 대처
plt.rcParams['axes.unicode_minus'] = False
# 한글폰트 전역 설정 (한글 꺠짐문제 해결)
plt.rcParams["font.family"] = 'Malgun Gothic'#'NanumGothic'#'UnDotum'#'NanumBarunGothic' #UnDotum
# 이미지의 크기 조정
plt.rcParams["font.size"] = 12         # 그림의 글자크기 조정 11 pt
plt.rcParams["figure.figsize"] = (8,6) # 그림의 크기를 가로 7 in, 세로 5 in

x = np.linspace(-2*np.pi, 2*np.pi, 100) # -2pi과 2pi사이를 100개의 점으로 나타냄
y = np.sin(x) 

#plt.plot(x,y) # 기본 플롯

plt.plot(x, y, 'r:^', label='legend 표시')                                       # color와 symbol marker type ==> 아래 참조
plt.plot(x, 0.5*y, color='blue', marker='o', linestyle=':',label='legend2 표시') # color와 symbol marker type ==> 아래 참조

plt.title('Sine graph')     # 제목, X와 Y축 제목
plt.xlabel(r'$x$')
plt.ylabel(r'$sin(4 \pi x)$')

plt.grid(True) # 그리드 표시
plt.legend(loc='upper left')

#plt.show()

x = np.linspace(0,1,50)
y1 = np.cos(4*np.pi*x)
y2 = np.cos(4*np.pi*x)*np.exp(-2*x)

plt.subplot(2,1,1) # 2행 1열, idnum
plt.plot(x,y1,'r-*',lw=1)
plt.grid(True)
plt.ylabel(r'$sin(4 \pi x)$')


plt.subplot(2,1,2)
plt.plot(x,y2,'bo',lw=1)
plt.grid(True)
plt.xlabel('x')
plt.ylabel(r'$ e^{-2x} sin(4\pi x) $')

plt.show()