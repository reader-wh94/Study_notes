## Life cycle in React

> Life Cycle method

라이프 사이클 메서드 종류는 총 9가지 이다. **Will**이 붙은 메서드는 어떤 작업을 작동하기 **전**에 실행되는 메서드이고, **Did**가 붙은 메서드는 어떤 작업을 작동한 **후**에 실행되는 메서드이다.

라이프 사이클은 마운트, 업데이트, 언마운트 세 가지의 카테고리로 나눈다.

![life_react1](https://user-images.githubusercontent.com/68210266/158113712-4418963e-3401-48c1-ae3d-ee2bfa0fba48.PNG)

<br>

> 마운트(Mount)

* DOM이 생성되고 웹 브라우저 상에 나타나는 것을 마운트(mount)라고 한다.

![life_react2](https://user-images.githubusercontent.com/68210266/158114176-12463ad6-0a3b-453d-b640-8796e3bbf566.PNG)

* 마운트할 때 호출하는 메서드
  * constructor : 컴포넌트를 새로 만들 때마다 호출되는 클래스 생성자 메서드
  * getDerivedStateFromProps
    * props에 있는 값을 state에 넣을 때 사용하는 메서드
    * 컴포넌트가 마운트될 때와 업데이트될 때 호출
  * render
    * 우리가 준비한 UI를 렌더링하는 메서드
    * 라이프 사이클 메서드 중 유일한 필수 메서드
    * 이벤트 설정이 아닌 곳에서 setState를 사용하면 안되며, 브라우저의 DOM에 접근해서도 안된다.
    * DOM 정보를 가져오거나 state에 변화를 줄 때에는 componentDidMount에서 처리해야 한다.
  * componentDidMount
    * 컴포넌트가 웹 브라우저 상에 나타난 후 호출하는 메서드
    * 비동기 작업을 처리한다.

<br>

> 업데이트(Update)

* 업데이트 하는 상황
  * props가 바뀔 때
  * state가 바뀔 때
  * 부모 컴포넌트가 리렌더링 될 때
  * this.forceUpdate로 강제로 렌더링을 트리거할 때

![life_react3](https://user-images.githubusercontent.com/68210266/158115421-9fff1c27-4555-4a6d-ac89-91239c8f7bd1.PNG)

* 업데이트할 때 호출하는 메서드
  * getDerivedStateFromProps
    * 마운트 과정에서도 호출
    * 업데이트가 시작하기 전에도 호출
    * props의 변화에 따라 state 값에도 변화를 주고 싶을 대 사용
  * shouldComponentUpdate
    * 컴포넌트가 리렌더링을 해야 할지 말아야 할지를 결정하는 메서드
    * true 혹은 false를 반환
    * true를 반환하면 다음 라이프 사이클 메서드를 실행, false를 반환하면 작업을 중지(리렌더링 하지 않음)
  * render : 컴포넌트를 리렌더링
  * getSnapshotBeforeUpdate
    * 컴포넌트 변화를 DOM에 반영하기 바로 직전에 호출하는 메서드
    * 주로 업데이트하기 직전의 값을 참고할 일이 있을 때 활용
  * componentDidUpdate
    * 컴포넌트의 업데이트 작업이 끝난 후 호출
    * DOM 관련 처리를 해도 무방하다

<br>

> 언마운트(Unmount)

* 마운트의 반대 과정, 컴포넌트를 DOM에서 제거하는 것을 언마운트(unmount)라고 한다

![life_react4](https://user-images.githubusercontent.com/68210266/158116212-fed743bd-dc50-48e6-803c-977e58ffb976.PNG)

* 언마운트 할 때 호출하는 메서드
  * componentWillUnmount
    * 컴포넌트가 웹 브라우저상에서 사라지기 전에 호출하는 메서드
    * 컴포넌트를 DOM에서 제거할 때 사용

<br>

<br>

출처 : [리액트를 다루는 기술](http://www.kyobobook.co.kr/product/detailViewKor.laf?mallGb=KOR&ejkGb=KOR&barcode=9791160508796)