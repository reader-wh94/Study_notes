## REST API

> REST

* REpresentational State Transfer 의 약자이다.
* 자원의 이름으로 구분하여 해당 자원의 상태(정보)를 주고 받는 모든 것을 의미한다.
* 월드 와이드 웹(www)과 같은 분산 하이퍼미디어 시스템을 위한 소프트웨어 개발 아키텍처의 한 형식이다.
* **HTTP URI(Uniform Resource Identifier)를 통해 자원(Resource)을 명시하고, HTTP Method(POST, GET, PUT, DELETE)를 통해 해당 자원에 대한 CRUD Operation을 적용하는 것을 의미한다.**
  * 즉, **REST는 자원 기반의 구조(ROA, Resource Oriented Architecture) 설계의 중심에 Resource가 있고 HTTP Method를 통해 Resource를 처리하도록 설계된 아키텍쳐를 의미한다.**

<br>

> REST 장단점

* 장점
  * HTTP 표준 프로토콜에 따르는 모든 플랫폼에서 사용이 가능하다.
  * 서버와 클라이언트의 역할을 명확하게 분리한다.
  * HTTP 프로토콜의 인프라를 그대로 사용하므로 REST API 사용을 위한 별도의 인프라를 구축할 필요가 없다.
* 단점
  * 표준이 존재하지 않는다.
  * HTTP Method 형태가 제한적이다
  * 구형 브라우저가 아직 제대로 지원해주지 못하는 부분이 존재한다.

<br>

> REST 구성

* 자원(Resource) - URI
  * 모든 자원에 고유한 ID가 존재하고, 이 자원은 Server에 존재한다.
  * 자원을 구별하는 ID는 ‘/groups/:group_id’와 같은 HTTP URI 다.
  * Client는 URI를 이용해서 자원을 지정하고 해당 자원의 상태(정보)에 대한 조작을 Server에 요청한다.
* 행위(Verb) - HTTP METHOD
  * HTTP 프로토콜은 GET, POST, PUT, DELETE 와 같은 메서드를 제공한다.
* 표현(Representations)
  * REST에서 하나의 자원은 JSON, XML, TEXT, RSS 등 여러 형태의 Representation으로 나타내어 질 수 있다.
  * JSON 혹은 XML를 통해 데이터를 주고 받는 것이 일반적이다.

<br>

> REST 특징

1. Server-Client(서버-클라이언트 구조)
   * 자원이 있는 쪽이 Server, 자원을 요청하는 쪽이 Client가 된다.
     * REST Server: API를 제공하고 비즈니스 로직 처리 및 저장을 책임진다.
     * Client: 사용자 인증이나 context(세션, 로그인 정보) 등을 직접 관리하고 책임진다.
   * 서로 간 의존성이 줄어든다.
2. Stateless (무상태성)
   * Client의 context를 Server에 저장하지 않는다.
   * Server는 각각의 요청을 완전히 별개의 것으로 인식하고 처리한다.
3. Cacheable (캐시 처리 가능)
   * 웹 표준 HTTP 프로토콜을 그대로 사용하므로 웹에서 사용하는 기존의 인프라를 그대로 활용할 수 있다.
   * 대량의 요청을 효율적으로 처리하기 위해 캐시가 요구된다.
4. Layered System (계층화)
   * Client는 REST API Server만 호출한다.
   * REST Server는 다중 계층으로 구성될 수 있다.
5. Uniform Interface (인터페이스 일관성)
   * URI로 지정한 Resource에 대한 조작을 통일되고 한정적인 인터페이스로 수행한다.
   * HTTP 표준 프로토콜에 따르는 모든 플랫폼에서 사용이 가능하다

<br>

> REST API

* REST 기반으로 서비스 API를 구현한 것
  * HTTP URI(Uniform Resource Identifier)를 통해 자원(Resource)을 명시하고,
  * HTTP Method(POST, GET, PUT, DELETE)를 통해
  * 해당 자원(URI)에 대한 CRUD Operation을 적용하는 것을 의미한다.

* 특징
  * 사내 시스템들도 REST 기반으로 시스템을 분산해 확장성과 재사용성을 높여 유지보수 및 운용을 편리하게 할 수 있다.
  * REST는 HTTP 표준을 기반으로 구현하므로, HTTP를 지원하는 프로그램 언어로 클라이언트, 서버를 구현할 수 있다.

<br>

> REST API 설계 예시

1. URI은 동사보다는 명사를, 대문자보다는 소문자를 사용하여야 한다.

   ```bash
   👎 http://github.com/reader-wh94/Studying/
   👍 http://github.com/reader-wh67/study/
   ```

   

2. 마지막에 슬래시(/)를 포함하지 않는다.

   ```bash
   👎 http://github.com/reader-wh94/test/
   👍 http://github.com/reader-wh67/test
   ```

   

3. 언더바 대신 하이폰(-)을 사용한다.

   ```bash
   👎 http://github.com/reader-wh94/study_blog
   👍 http://github.com/reader-wh67/study-blog
   ```

   

4. 파일 확장자는 URI에 포함하지 않는다.

   ```
   👎 http://github.com/reader-wh94/picture.png
   👍 http://github.com/reader-wh67/picture
   ```

   

5. 행위를 포함하지 않는다.

   ```bash
   👎 http://github.com/reader-wh94/delete-post/1
   👍 http://github.com/reader-wh94/post/1
   ```

<br>

> RESTful 이란?

RESTful이란 REST의 원리를 따르는 시스템을 의미한다. 하지만 REST를 사용했다 해서 모두가 RESTful 한 것은 아니다. REST API의 설계 규칙을 올바르게 지킨 시스템을 RESTful하다 말할 수 있다.

모든 CRUD 기능을 POST로 처리하는 API 혹은  URI 규칙을 올바르게 지키지 않은 API는 REST API의 설계 규칙을 올바르게 지키지 못한 시스템은 REST API를 사용하였지만 RESTful 하지 못한 시스템이라고 할 수 있다.

<br>

출처 : [REST API 제대로 알고 사용하기](https://meetup.toast.com/posts/92), [[Network] REST란? REST API란? RESTful이란?](https://gmlwjd9405.github.io/2018/09/21/rest-and-restful.html), [[네트워크\] REST API란? REST, RESTful이란?](https://khj93.tistory.com/entry/네트워크-REST-API란-REST-RESTful이란)

