## 동기 VS 비동기

> 동기 (Synchronous)와 비동기(Asynchronous)

![sys_asyn1](https://user-images.githubusercontent.com/68210266/157812735-54ed23ce-25b4-4219-a370-40ac250af95c.PNG)

* 동기(Synchronous)
  * 동기 방식은 서버에서 요청을 보냈을 때 응답이 돌아와야 다음 동작을 수행할 수 있다.
  * 즉, 어떤 일이 완료될 때까지 코드의 실행을 멈추고 기다리는 프로그래밍 방식을 **동기식 프로그래밍(synchronous programming)**이라고 부릅니다.
  * 다른 작업은 앞선 작업이 끝나야 수행이 된다.
* 비동기(Asynchornous)
  * 비동기 방식은 반대로 요청을 보냈을 때 응답 상태와 상관 없이 다음 동작을 수행할 수 있다.
  * 즉, 어떤 일이 완료되기를 기다리지 않고 다음 코드를 실행해 나가는 프로그래밍 방식이다. (**비동기 프로그래밍 asynchronous programming**)

<br>

> 비동기 - callback

* 백그라운드에서 코드 실행을 실행할 함수를 호출할 때 인수로 지정된 함수이다.
* 백그라운드 코드 실행이 끝나면 callback 함수를 호출하여 작업이 완료됐음을 알리거나, 다음 작업을 실행하게 할 수 있다.

<br>

파라미터 값이 주어지면 1초 뒤에 10을 더해서 반환하는 함수가 있고, 해당 함수고 처리된 직후 1초에 걸쳐서 10, 20, 30, 40과 같은 형태로 콜백 함수를 사용해서 여러 번 순차적으로 처리하는 코드

```javascript
function increase(number, callback) {
	setTimeout(() => {
        const result = number +10;
        if (callback) {
            callback(result);
        }
    }, 1000);
}

console.log('작업 시작');
increase(0, result => {
    console.log(result);
    increase(result, result => {
    	console.log(result);
    	increase(result, result => {
    		console.log(result);
    		increase(result, result => {
    			console.log(result);
    			console.log('작업 완료');
			});
		});
	});
});
```

결과

```bash
작업 시작
10
20
30
40
작업 완료
```

<br>

콜백 안에 또 콜백을 넣어서 구현할 수 있는데, 너무 여러 번 중첩되어 가독성이 떨어지고 복잡한 비동기 데이터 흐름을 표현하기가 어렵다. 이렇게 데이터 흐름이 조금만 복잡해져도 코드가 복잡해지는데 이를 **'콜백 지옥'**이라고도 부른다.

<br>

<br>

> 비동기 - Promise

* Promise는 콜백 지옥 같은 코드가 형성되지 않게 하는 방안으로 ES6에 도입된 기능이다.
* Promise는 '언젠가 끝나는 작업'의 결과 값을 담는 통과 같은 객체이다. 그 통 안에 무엇이 들어갈 지 모를 수도 있지만 `then` 메소드를 통해 콜백을 등록해서 작업이 끝났을 때 결과 값을 가지고 추가 작업을 할 수 있다.

<br>

callback과 같은 기능을 하는 코드이다.

```javascript
function increase(number) {
	const promise = new Promise((resolve, reject) => {
		// resolve는 성공, reject는 실패
		setTimeOut(() => {
			const result = number + 10;
			if (result > 50) {
				// 50 보다 높으면 에러 발생
				const e = new Error('NumberTooBig');
				return reject(e);
			}
			resolve(result);
		}, 1000);
	});
	return promise;
}

increase(0)
	.then(number => {
    // Promise에서 resolve된 값은 .then을 통해 받아올 수 있음
    console.log(number);
    return increase(number); //Promise를 리턴하면
})
.then(number => {
    // 또 .then으로 처리 가능
    console.log(number);
    return increase(number);
})
.then(number => {
    console.log(number);
    return increase(number);
})
.then(number => {
    console.log(number);
    return increase(number);
})
.then(number => {
    console.log(number);
    return increase(number);
})
.catch(e => {
    // 도중에 에러가 발생한다면 .catch를 통해 알 수 있음
    console.log(e);
});
```

<br>

* `then` 메소드는 Promise 객체를 반환하므로, 콜백을 중첩하지 않고도 비동기 작업을 연이어 할 수있다.
* 비동기 작업이라는 동작 자체를 값으로 다룰 수 있게 한다.

<br>

<br>

> 비동기 - async/await

* async/await는 Promise를 더욱 쉽게 사용할 수 있도록 해 주는 ES2017(ES8) 문법이다.
* 함수 앞에 async 키워드를추가하고, 해당 함수 내부에서 Promise의 앞부분에 await 키워드를 사용한다.

<br>

```javascript
function increase(number) {
	const promise = new Promise((resolve, reject) => {
		// resolve는 성공, reject는 실패
		setTimeOut(() => {
			const result = number + 10;
			if (result > 50) {
				// 50 보다 높으면 에러 발생
				const e = new Error('NumberTooBig');
				return reject(e);
			}
			resolve(result);
		}, 1000);
	});
	return promise;
}

async function runTask() {
	try { // try/catch 구문을 사용하여 에러를 처리
		let result = await increase(0);
		console.log(result);
		result = await increase(result);
		console.log(result);
		result = await increase(result);
		console.log(result);
		result = await increase(result);
		console.log(result);
		result = await increase(result);
		console.log(result);
		result = await increase(result);
		console.log(result);
	} catch (e) {
		console.log(e);
	}
}
```

<br>

* 비동기 함수는 항상 Promise 객체를 반환한다는 특징을 가지고 있다. 이 Promise의 결과 값은 비동기 함수 내에서 무엇을 반환하느냐에 따라 결정되며, `then` 메소드와 똑같은 방식으로 작동한다.
* `await`는 Promise의 `then` 메소드와 유사한 기능을 하는데, `await` 키워드 위에 오는 Promise가 결과 값을 가질 때까지 비동기 함수의 실행을 중단시킨다.
  * '중단'은 비동기식이며, 브라우저는 Promise가 완료될 때까지 다른 작업을 처리할 수 있다.
* `await`는 연산자이기도 하며, `await` 연산의 결과 값은 뒤에 오는 Promise 객체의 결과 값이 된다.
* `await` 키워드는 `for`, `if`와 같은 제어 구문 안에서도 쓰일 수 있기 때문에, `then` 메소드를 사용할 때보다 **복잡한 비동기 데이터 흐름을 아주 쉽게 표현할 수 있다**는 장점이 있다.

<br>

<br>

출처 : [동기, 비동기 처리](https://velog.io/@daybreak/%EB%8F%99%EA%B8%B0-%EB%B9%84%EB%8F%99%EA%B8%B0-%EC%B2%98%EB%A6%AC), [Introducing asynchronous JavaScript](https://developer.mozilla.org/ko/docs/Learn/JavaScript/Asynchronous/Introducing), [비동기 프로그래밍](https://helloworldjavascript.net/pages/285-async.html), [리액트를 다루는 기술](http://www.kyobobook.co.kr/product/detailViewKor.laf?mallGb=KOR&ejkGb=KOR&barcode=9791160508796)

