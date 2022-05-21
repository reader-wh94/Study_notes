## Q. DFS에서 x,y를 뒤집어서 인자로 받는 이유?

### A. 배열과 좌표 평면은 좌표 측에서 차이가 있기 때문이다.

배열은 x좌표를 위에서 아래로, y좌표를 왼쪽에서 오른쪽으로 값을 증가시킨다.

하지만 좌표 평면에서는 x좌표는 왼쪽에서 오른쪽으로, y좌표를 아래에서 위로 값이 증가된다.

즉, 일반 좌표 평면에서 x축이 열이고, y축이 행이라 생각해야한다.

<br>

![Screenshot_20220521-154042_Samsung Notes](https://user-images.githubusercontent.com/68210266/169639395-e2f41e5c-bbb0-4f17-9d8c-67f22d567584.jpg)



2차원 배열을 사용하여 좌표 평면처럼 문제를 풀 수 있지만 좌표와 2차원 배열 사이에서 x,y 인자가 증감되는 방식이 다르기 때문에 (x,y)를 (y,x)로 받아 dfs를 풀 수 있다.

<br>

<br>

참고

https://velog.io/@peanut_/boj-s1-1743-%EC%9D%8C%EC%8B%9D%EB%AC%BC-%ED%94%BC%ED%95%98%EA%B8%B0

https://velog.io/@hongcheol/210422TIL