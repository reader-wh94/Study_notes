## Virtual DOM

> DOM 이란?

- DOM은 Document Object Model의 약어이다. 즉, **객체로 문서 구조를 표현하는 방법**으로 XML이나 HTML로 작성한다.
- DOM은 트리 형태라서 특정 노드를 찾거나 수정하거나 제거하거나 원하는 곳에 삽입할 수 있다.

![dom1](https://user-images.githubusercontent.com/68210266/158046207-c1485dd8-18b1-45d7-9d0e-45e169c85bfa.PNG)

<br>

> DOM의 문제점

* DOM은 동적UI에 최적화되어 있지 않다. 
  * HTML은 자체적으로 정적이며 자바스크립트를 사용하여 이를 동적으로 만든다.
* DOM 자체는 빠르다. 
  * 웹 브라우저 단에서 DOM에 변화가 일어나면 웹 브라우저가 CSS를 다시 연산하고, 레이아웃을 구성하고, 페이지를 리페인트 하는데 이 과정에서 시간이 오래 걸리는 것이다.
* 해결법
  * DOM을 조작할 때마다 엔진이 웹 페이지를 새로 그리게 되는데, 계속하여 페이지를 업데이트를 하는 것이 아니라 DOM을 최소한으로 조작하여 작업을 처리하는 방법을 사용한다.
    * Virtual DOM을 사용하여 DOM 업데이트를 추상화함으로써 DOM 처리 횟수를 최소화하고 효율적으로 진행한다.

<br>

> Virtual DOM

* Virtual DOM을 사용하면 실제 DOM에 접근하여 조작하는 대신, 이를 추상화한 자바스크립트 객체를 구성하여 사용한다.
* Virtual DOM 업데이트 과정
  * 데이터를 업데이트하면 전체 UI를 Virtual DOM에 리렌더링 한다.
  * 이전 Virtual DOM에 있던 내용과 현재 내용을 비교한다.
  * 바뀐 부분만 실제 DOM에 적용한다.
* 오해
  * Virtual DOM을 사용한다고 항상 빠른 것은 아니다.
    * React나 Vue 등을 사용하지 않더라도 코드 최적화를 열심히 하면 DOM 작업이 느려지는 문제를 개선할 수 있다.
    * 또한 작업이 매우 간단할 때에는 오히려 Virtual DOM을 사용하지 않는 편이 더 나은 성능을 보이기도 한다.

<br>

> 요약

* Virtual DOM은 DOM을 추상화 한 가상의 객체이다. 

* 페이지 업데이트가 있을 경우 실제 DOM에 접근하여 조작하는 것이 아니라 Virtaul DOM에 리랜더링하고, 전과 비교하여 바뀐 부분만 실제 DOM에 적용한다.

* Virtual DOM을 사용한다고 무조건 처리 속도가 빨라지는 것은 아니다.

<br>

<br>

출처 : [Virtual DOM 동작 원리와 이해 (with 브라우저의 렌더링 과정)](https://jeong-pro.tistory.com/210), [리액트를 다루는 기술](http://www.kyobobook.co.kr/product/detailViewKor.laf?mallGb=KOR&ejkGb=KOR&barcode=9791160508796)