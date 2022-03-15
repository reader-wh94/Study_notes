## Array & Object

> 배열

* 배열의 선언 방법

  ```javascript
  let arr = [];
  arr = [1, 3, 5, 7, 9];
  console.log(arr); // [1, 3, 5, 7, 9]
  ```

* 배열의 각 요소(item)는 `[]` 기호와 0에서 시작하는 인덱스를 이용하여 접근한다.

* 각각의 요소들은 쉼표(comma / ,)로 구분해준다.

* 키(key)가 없고, 값(item)들만 순서대로 나열되어 있다.

<br>

> 객체

* 객체의 선언 방법

  ```javascript
  let user = {}; // 빈 객체 선언
  
  user = {
  	name: "MyName",
  	email: "name@gmail.com",
  	city: "Seoul"
  }
  
  console.log(user);
  // {name: "MyName", email: "name@gmail.com", city: "Seoul"}
  ```

* 객체에는 키(key)와 값(value)가 있으며, 이를 묶어서 속성(Property)라 한다.

* 항상 키와 값을 쌍으로 넣어야한다.

* 한 쌍당 구분은 쉼표로 구분한다.

* 중괄호 `{}`를 통해 객체를 만든다.

<br>

> 공통점

1. 둘 다 Object data type을 가진다.

   ```javascript
   const array = [1,2,3,4,5];
   const object = { name : 'yunkuk', age : 20, numberOfFinger : 10};
   
   typeof array; // =>  object
   typeof object; // =>  object
   
   typeof arr === typeof object // => true !! 
   ```

   * Array와 Object를 구분하려면 `Array.isArray()`를 사용해서 구분해야한다.

<br>

> 차이점

1. Object는 index의 개념이 존재하지 않는다.

   ```javascript
   object.length // => undefined
   ```

   index가 length를 결정하므로 object.index는 `undefined`가 나온다.

   ```javascript
   let object = new Object();
   object[0] = 'value01';
   
   console.log(object); // => {0: 'value01'}
   ```

   key에 0이 들어가고 value에 'value01'이 들어간다.

<br><br>

출처: [object 와 array의 공통점과 차이점](https://velog.io/@yunkuk/TIL-03objectVSarray), [배열과 객체의 개념과 차이 (Array vs Object)](https://spicycookie.me/JavaScript/arrvsobj/)