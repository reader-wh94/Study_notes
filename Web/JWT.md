## JWT

> JWT

* JWT는 JSON Web Token의 약자로, 데이터가 JSON으로 이루어져 있는 토큰을 의미한다.

* JWT는 웹 표준(RFC 7519)으로, 전자 서명 된 URL-safe (URL로 이용할 수 있는 문자만 구성된)의 JSON이다.
* JWT는 자가 수용적(self-contained)이다.
  * 필요한 모든 정보를 자체적으롤 지니고 있으며, JWT 시스템에서 발급된 토큰은 토큰에 대한 기본 정보, 전달 할 정보 그리고 토큰이 검증됐다는 것을 증명해주는 signature를 포함하고 있다.
* 웹 서버의 경우 HTTP의 헤더에 넣어서 전달 할 수도 있고, URL의 파라미터로도 쉽게 전달할 수 있다.

<br>

> JWT을 사용하는 곳

* 권한 부여 : JWT를 사용하는 가장 일반적인 시나리오이다. 사용자가 로그인하면 각 후속 요청에 JWT가 포함되어 사용자가 해당 토큰으로 허용되는 경로, 서비스 및 리소스에 액세스할 수 있다.
* 정보 교환 : JSON 웹 토큰은 당사자 간에 정보를 안전하게 전송하는 좋은 방법이다. 예를 들어 공개/개인 키 쌍을 사용하여 JWT에 서명할 수 있디 때문에 발신자가 누구인지 확인할 수 있다.

<br>

> JWT 구조

JSON 웹 토큰은 점(`.`)으로 구분된 세 부분으로 구성된다.

![jwt](https://user-images.githubusercontent.com/68210266/157453380-730e59bd-906f-4e40-b1e2-811fbd0d88ad.PNG)

* 헤더

  * Header는 두가지 정보를 지니고 있다.
  * typ: 토큰의 타입을 지정한다. (JWT)
  * alg : 해싱 알고리즘을 지정한다. 이 알고리즘은 토큰을 검증할 때 사용되는 signature 부분에서 사용된다.

  ```bash
  {
    "typ": "JWT",
    "alg": "HS256"
  }
  ```

  위 JSON은 JWT의 첫 번째 부분을 형성하도록 인코딩된 Base64Url이다.

<br>

* 내용
  * payload에는 토큰에 담을 정보가 들어가있다. 이 정보에 담기는 정보의 한'조각'을 클레임(claim)이라고 부르고, 이는 name / value의 한 쌍으로 이루어져 있다.
  * 토큰에는 여러 개의 클레임들을 넣을 수 있다.
  * 토큰에는 크게 세 분류로 나뉘어져있다.
    * 등록된(registered) 클레임 - 토큰 발급자(iss), 토큰 제목(sub), 토큰 대상자(audience), 토큰 만료 시간(exp), 토큰이 발급된 시간(iat), JWT의 고유 식별자(jti)
    * 공개(public) 클레임 - 충돌이 방지된 (collision-resistant) 이름을 가지고 있어야 한다. 충돌을 방지하기 위해서는, 클레임 이름을 [URI](https://en.wikipedia.org/wiki/Uniform_resource_identifier) 형식으로 짓는다.
    * 비공개(private) 클레임 - 양 측간에 (보통 클라이언트 <->서버) 협의하에 사용되는 클레임 이름들이다.

<br>

* 서명

  * signature에는 헤더의 인코딩 값과, 정보의 인코딩 값을 합친 후 주어진 비밀키로 해쉬를 하여 생성한다.

  ```bash
  HMACSHA256(
    base64UrlEncode(header) + "." +
    base64UrlEncode(payload),
    secret)
  ```

<br>

<br>

출처 : [[JWT\] JSON Web Token 소개 및 구조](https://velopert.com/2389), [JSON 웹 토큰 소개](https://jwt.io/introduction)