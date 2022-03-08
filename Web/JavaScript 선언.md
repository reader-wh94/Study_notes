## JavaScript 선언

JavaScript의 선언에는 3가지 방법이 있다.

* `var`
  * 변수를 선언. 추가로 동시에 값을 초기화
* `let`
  * 블록 범위(scope) 지역 변수를 선언. 추가로 동시에 값을 초기화
* `const`
  * 블록 범위 읽기 전용 상수를 선언

변수의 선언은 위와 같이 `var`, `let`, `const` 키워드로 할 수 있으며, ES6에서 const와 let이 추가되었다.

자바스크립트에서 변수 선언은 `선언 -> 초기화` 단계를 거쳐 수행된다.

* 선언 단계 : 변수 명을 등록하여 자바스크립트 엔진에 변수의 존재를 알린다.
* 초기화 단계 : 값을 저장하기 위한 메모리 공간을 확보하고 암묵적으로 undefined를 할당해 초기화한다.

<br>

> var

* 특징
  * 변수 중복 선언이 가능하며, 예기치 못한 값을 반환할 수 있다.

  ```javascript
  var name = 'JavaScript'
  console.log(name) // JavaScript
  
  var name = 'MyName'
  console.log(name) // MyName
  ```

  * 함수 레벨 스코프로 인해 함수 외부에서 선언한 변수는 모두 전역 변수로 된다.
  * 변수 선언시 초기 값을 주지 않아도 된다.

* 호이스팅
  * var의 경우 호이스팅되면서 초기 값이 없으면 자동으로 undefined를 초기 값으로 하여 메모리를 할당한다. 따라서 선언 전에 해당 변수를 사용하려고 해도 메모리에 해당 변수가 존재하기 때문에 에러가 발생하지 않는다.

<br>

> let

* 특징

  * 변수 중복 선언은 불가능하지만, 재할당은 가능하다.

  ```javascript
  let name = 'JavaScript'
  console.log(name) // JavaScript
  
  let name = 'MyName' // Uncaught SyntaxError
  
  name = 'MyName'
  console.log(name) // MyName
  ```

  * let 키워드로 선언한 변수는 모두 코드 블록(ex. 함수, if, for, while, try/catch 등등)을 지역 스코프로 인정하는 블록 레벨 스코프를 따른다.

  ```javascript
  let a = 1
  
  if (true) {
    let a = 5
  }
  
  console.log(a) // output: 1
  ```

  * 변수 선언 시 초기 값을 주지 않아도 된다.

* 호이스팅

  * 호이스팅이 되면서 초기 값이 없다면 var처럼 자동으로 초기 값을 할당하지 않는다.
  * 값이 할당 전까지 메모리를 할당하지 않기 때문에 값이 할당되기 전에 사용하려고 하면 메모리에 해당 변수가 존재하지 않아서 에러를 발생시킨다.

<br>

> const

* 특징

  * 선언과 초기화가 동시에 진행되어야 한다. (변수 선언 시 초기 값을 주지 않으면 에러가 난다.)
  * let과 같이 코드 블록을 지역 스코프로 인정하는 블록 레벨 스코프를 따른다.
  * 재선언이 불가능하며, 재할당도 불가능하다. ('불변'을 의미하는 것은 아니다.)

  ```javascript
  const obj = { first: 1 }; // 에러 발생
  
  obj = 1; // Uncaught TypeError: Assignment to constant variable.
  
  // 에러 발생하지 않음.
  obj.first = 2;
  obj.second = 2;
  delete obj.first;
  ```

  위와 같이 const 변수가 가리키는 값 자체를 변경하려고 하면 에러가 발생하지만 객체 내의 프로퍼티의 추가, 변경, 삭제를 하는 것은 문제가 없다.

* 호이스팅

  * 호이스팅이 되면서 초기 값이 없다면 var처럼 자동으로 초기 값을 할당하지 않는다.
  * 값이 할당 전까지 메모리를 할당하지 않기 때문에 값이 할당되기 전에 사용하려고 하면 메모리에 해당 변수가 존재하지 않아서 에러를 발생시킨다.

<br>

> 정리

var은 함수 레벨 스코프이며 변수 중복 선언이 가능하고, 변수 선언 시 초기 값을 주지 않아도 된다.

let은 블록 레벨 스코프이며 변수 중복 선언이 불가능하고, 변수 재할당은 가능하며 변수 선언 시 초기 값을 주지 않아도 된다.

const는 블록 레벨 스코프이며 변수 중복 선언이 불가능하고, 변수 재할당도 불가능하며(객체 내의 프로퍼티의 변경은 가능하다.) 변수 선언과 초기화가 동시에 진행되어야 한다.



<br>

출처 : [var, let, const의 차이](https://www.howdy-mj.me/javascript/var-let-const/), [문법과 자료형](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Grammar_and_types), [(JavaScript) var, let, const의 차이점](https://medium.com/@su_bak/javascript-var-let-const%EC%9D%98-%EC%B0%A8%EC%9D%B4%EC%A0%90-9fab5c264c9c)