# AOP란?
> 관점 지향 프로그래밍(aspect-oriented programming, AOP)은 횡단 관심사(cross-cutting concern)의 분리를 허용함으로써 모듈성을 증가시키는 것이 목적인 프로그래밍 패러다임이다.
## 도대체 무슨 소리일까?
### OOP를 통한 AOP 이해
 객체 지향 프로그래밍(Object-oriented Programming, OOP)은 공통의 목적이 있는 데이터와 동작을 묶어 하나의 객체로 정의하는 것이다. 객체를 적극적으로 활용함으로써 기능을 재사용할 수 있는 것이 가장 큰 장점이다.
 
**장점이 많은 OOP에도 한계점이 있다.** 비즈니스 로직을 기준으로 분리된 클래스에 부가기능(ex. 로깅, 트랙젝션, DB연결)의 소스코드가 중복되어 존재하게 된다.

AOP는 비즈니스 로직은 핵심 관심사(core concern) 부가기능은 횡단 관심사(cross-cutting concern)로 해석한다. 
즉, **비즈니스 로직과 상관 없는 부가기능을 분리하여 모듈화 하는 것을 AOP**라고 한다.
![img](https://user-images.githubusercontent.com/56240505/123369146-27997800-d5b8-11eb-9be7-dfd7a34a4f86.png)
# AOP 구현체
Java 진영에서 AspectJ를 Spring에서는 Spring AOP를 사용한다. 간단한 차이만 알고 넘어가자.
![img](https://velog.velcdn.com/images/ssuh0o0/post/d8f716f5-349f-450a-b0eb-dde8726e629e/image.png)

# AOP의 용어와 이해
AOP 프레임워크에서 통상적으로 쓰이는 용어들이다.
![img](https://gmoon92.github.io/md/img/aop/aop-terms-explanation.png)
## ...천천히 알아가보자
### 용어 - 핵심 관심사 영역
![img](https://gmoon92.github.io/md/img/aop/module-of-core.png)
- Target Object
- JoinPoint
##### Target Object
먼저 `Target Object`는 횡단기능(`Advice`)이 적용될 객체(Object)를 뜻한다. 이 객체는 핵심 모듈(비즈니스 클래스)이라 할 수 있다.Spring AOP에선 실제 적용할 객체 대신  `Runtime Proxy`를 사용하여 구현되기 때문에, Target Object는 항상  `Proxy Object`다.

##### JoinPoint

`JoinPoint`는 Target Object안에서 횡단기능(`Advice`)이 적용될 수 있는 여러 위치를 뜻한다.

![img](https://gmoon92.github.io/md/img/aop/joinpoint.png)

이 위치는 프로그램이 실행될 때 (1) 예외가 발생하거나 (2) 필드(attribute)가 수정되는 시점 또는 (3) 객체가 생성(constructor)되는 시점 그리고 (4) 메소드가 호출되는 시점 등 그 외 프로그램이 실행될 때 발생할 수 있는 모든 시점은 횡단기능이 적용될 수 있는 위치들이다.

일반적으로 AspectJ는 모든 JoinPoint에 접근이 가능하지만 Spring AOP는 기본적으로 메소드 interceptor를 기반으로 하고 있어서 JoinPoint는 항상 메소드 단위다.

#### 용어 - 횡단 관심사 영역

##### Aspect

횡단 관심사 영역에서 가장 먼저 살펴볼 용어는  `Aspect`이다.

AOP는 횡단 관심사를 Aspect라는 독특한 모듈을 기반으로 모듈화를 한다. 이러한 횡단 관심사 모듈화를  `Aspect`라 한다. Java에선 사실상 표준으로 가장 널리 사용되는  `AspectJ`라는 확장 기능을 통해 Aspect를 구현할 수 있다. AsepctJ의 모듈은  `*.aj`라는 확장자를 가진 독특한 파일로 구현된다.

AspectJ는 기본적으로 이클립스에서 확장 기능을 추가하고 그 외 별도의 설정을 해야 한다. 또한, aj는 기존 Java 문법과 비슷하면서도 사뭇 달라서 별도의 학습이 필요하다. (참고 -  [Eclipse DOC - Starting-AspectJ](https://www.eclipse.org/aspectj/doc/next/progguide/starting-aspectj.html),  [블로그 - Eclipse에서 AspectJ 시작하기](https://busy.org/@nhj12311/aop-aspectj-java-aop-5))

반면 Spring AOP에서 제공하는 어노테이션(@AspectJ)을 통한 구현 방식은 AspectJ 보다 쉬운 설정과 기본적으로 클래스로 구현하기 때문에 쉽게 접근할 수 있다는 장점이 있다.

Spring AOP에선 기본적으로 두 가지 방식을 통해 Aspect를 구현할 수 있다.

1.  [XML(스키마 기반 접근)](https://docs.spring.io/spring/docs/4.3.15.RELEASE/spring-framework-reference/html/aop.html#aop-schema)
2.  [@AspectJ(어노테이션 기반 접근)](https://docs.spring.io/spring/docs/4.3.15.RELEASE/spring-framework-reference/html/aop.html#aop-ataspectj)

이 Aspect 모듈은 핵심 모듈에 횡단 코드를 적용하기 위한 최종 목적을 띄고, 횡단 모듈의 관리 유용성을 증가시키기 위한 횡단 관심사의 집합체다. 이 때문에 Aspect에는 횡단 코드와 이 코드가 어디서 언제 적용할지 구현해야 한다.

![img](https://gmoon92.github.io/md/img/aop/module-of-aspect.png)

_Aspect = Advice + Pointcut + Introduction(inter-type)_

-   Advice
-   Pointcut
-   Introduction(Inter-type)

##### Advice

`Advice`는 JoinPoint에 적용할  `횡단 코드`를 의미한다.

![img](https://gmoon92.github.io/md/img/aop/advice.png)

Spring을 포함한 많은 AOP 프레임워크는  [Interceptors](https://docs.oracle.com/javaee/6/tutorial/doc/gkeed.html)로서 Advice을 모델링하고 , JoinPoit 주변의 인터셉터의 결합된 상태의 체인을 유지하고 실제 런타임 시 결합된 코드가 실행된다.

Spring AOP에서 JoinPoint는 항상 메소드 실행을 바라보기 때문에  `org.aspectj.lang.JoinPoint`  Type의 매개 변수를 선언하여 JoinPoint 정보를 Advice에서 사용할 수 있다.

또한, Spring AOP의 Advice는 JoinPoint와 횡단 코드의 각기 다른 결합점을 제어할 수 있도록 다양한 Advice를 제공하고 있다.

![img](https://gmoon92.github.io/md/img/aop/spring-aop-advice.png)

-   @Before : JoinPoint 이전에 실행
    -   단 Exception을 throw 하지 않는 한 실행 흐름이 JoinPoint로 진행되는 것을 방지하는 기능은 없다.
-   @AfterReturning : JoinPoint가 정상적으로 완료된 후 실행
    -   예를 들어 메소드가 Exception을 발생시키지 않고 리턴하는 경우
-   @AfterThrowing : Exception을 throw하여 메소드가 종료된 경우 실행
-   @After(finally) : JoinPoint의 상태(Exception, 정상)와 무관하고 JoinPoint가 실행된 후 실행
-   @Around : Before와 After가 합쳐진 Advice
    -   메소드 호출 전과 후에 실행 또한 JoinPoint로 진행할지 또는 자체 반환 값을 반환하거나 Exception를 throw하여 특정 메소드를 호출할 수 있다.

##### Pointcut

Pointcut은 여러 JoinPoint 중 실제적으로 Advice할 JoinPoint이다.

![img](https://gmoon92.github.io/md/img/aop/joinpoint-pointcut.png)

따라서 Advice는 여러 JoinPoint중에서 Pointcut의 표현식에 명시된 JoinPoint에서 실행된다. 예를 들어 여러 실행 포인트 중에서 특정 이름의 메소드에서 Advice를 하거나 제외하여 실행시킬 수 있다.

이러한 Pointcut 표현식과 일치하는 JoinPoint를 실행한다는 개념은 AOP의 핵심이다. 또한, Spring AOP에선 Pointcut과 Advice를 합쳐  `Advisor`라 불린다. Spring AOP은 기본적으로 AspectJ Pointcut 언어를 사용한다.

##### Introduction(inter-type)

Introduction(inter-type)은 Aspect 모듈 내부의 선언된 클래스 또는 인터페이스, 메소드 그 외 모든 필드를 뜻한다. 이 Introduction의 주된 목적은 기존 클래스에 새로운 인터페이스(및 해당 구현 객체)를 추가하기 위함이다.

이는 OOP에서 말하는 상속이나 확장과는 다른 방식으로 Advice 또는 Aspect를 이용해서 기존 클래스에 없는 인터페이스를 동적으로 추가할 수 있다.

특히 Spring AOP를 사용하면 Proxy된 객체에 새로운 인터페이스를 도입할 수 있다. 또한, bean이 이 인터페이스를 구현하도록 쉽게 캐싱할 수 있다.

##### AOP Proxy

Proxy는 “대신 일을 하는 사람”이라는 사전적 의미를 가지고 있다. 이와 마찬가지로 AOP Proxy는 Aspect를 대신 수행하기 위해 AOP 프레임워크에 의해 생성된 객체(Object)이다.

![img](https://gmoon92.github.io/md/img/aop/proxy1.png)

일반적으로 Spring을 포함한 많은 AOP 프레임워크에선 핵심 관심 코드에 직접적인 Aspect를 하지 않고  `Proxy Object`를 활용하여 Aspect를 한다.

결과적으로 횡단 관심 객체와 핵심 관심 객체의 느슨한 결합 구조를 만들고, 필요 여부에 따라 부가 기능을 탈 부착하기 용이하게 해준다.

-   직접적인 참조가 아닌 Proxy를 사용하여 동적으로 참조
-   부가 기능의 탈부착이 용이

Spring을 포함하여 대부분 AOP 프레임워크에서 Proxy를 사용하여 동적으로 Advice하기 위해 Java에서 제공해주는  `java.lang.reflect.Proxy`을 사용하여 Proxy 객체를 동적으로 생성해준다.

![img](https://gmoon92.github.io/md/img/aop/proxy2.png)

구체적으로  `JDK Dynamic Proxy`와  `CGLIB Proxy`의 방식이 존재한다. 물론 Spring AOP에선 두 가지 구현 방식을 제공하고 있다.

-   JDK Dynamic Proxy
-   CGLIB Proxy

#### 용어와 동작 - 관심사의 교차

AOP는 특정 JoinPoint에 Advice하여 핵심기능과 횡단기능이 교차하여 새롭게 생성된 객체를 프로세스에 적용하는 일련의 모든 과정을  `Weaving`라 한다.

##### Weaving

이 Weaving은 수행 시점에 따라 CTW, LTW, RTW으로 분류할 수 있다.

-   CTW : Compile-Time Weaving (AspectJ Compiler)
-   LTW : Load-Time Weaving (AspectJ Compiler)
-   RTW : Run-Time Weaving (Spring AOP)

특히 Java 환경에서 AOP를 한다면 가장 먼저 AspectJ와 Spring AOP를 떠올릴 수 있는데, 이 둘은 서로 독립적인 대상이므로 항상 비교가 되고 Weaving에서도 그 차이를 알 수 있다.

먼저 AspectJ는 바이트 코드 기반으로 기존 클래스 코드를 조작하여 AspectJ Compiler(ACJ)에 의해 Aspect를 Weaving하는 방식을 취하고 있다.

![img](https://gmoon92.github.io/md/img/aop/aspect-cycle.png)

따라서 CTW, LTW 방식을 기본적으로 사용하고 있다.

반면 Spring AOP는 Dynamic Proxy 기반으로 기본적으로 CTW, LTW를 사용하지 않고 RTW를 사용한다. Spring AOP의 Weaving의 방식은 AspectJ에 비해 가볍지만, 대부분 기능을 구현할 수 있다.

![img](https://gmoon92.github.io/md/img/aop/proxy3.png)

## 마무리
AOP는 DI, IOC와 같은 스플링을 대표하는 3가지 요소 중 하나지만 가장 마지막에 공부할 것을 추천한다. Proxy방식에 대한 추가적인 공부가 더 필요하며, 예제에 대한 중요도 또한 높다. 다음 발표는 DI/IOC가 나왔으면 좋겠다.
## 참고
-   Blog
    -   [Spring-DOC : 11. Aspect Oriented Programming with Spring](https://docs.spring.io/spring/docs/4.3.15.RELEASE/spring-framework-reference/html/aop.html)
    -   [Spring-DOC : Chapter 6. Aspect Oriented Programming with Spring](https://docs.spring.io/spring/docs/2.0.x/reference/aop.html)
    -   [Baeldung : Intro to AspectJ](https://www.baeldung.com/aspectj)
    -   [Baeldung : Introduction to Pointcut](https://www.baeldung.com/spring-aop-Pointcut-tutorial)
    -   [egovframework : aop-aspect](http://www.egovframe.go.kr/wiki/doku.php?id=egovframework:rte:fdl:aop:aspectj)
    -   [stackoverflow](https://stackoverflow.com/questions/29650355/why-in-spring-aop-the-object-are-wrapped-into-a-jdk-proxy-that-implements-interf)
    -   [spring-3-part-6-spring-aop](http://ojitha.blogspot.com/2013/03/spring-3-part-6-spring-aop.html)
    -   [Aspect-Oriented Programming vs. Object-Oriented Programming](https://study.com/academy/lesson/aspect-oriented-programming-vs-object-oriented-programming.html)
    -   [the-basics-of-aop](https://blog.jayway.com/2015/09/07/the-basics-of-aop/)
    -   [Spring AOP AspectJ @After Annotation Example](https://howtodoinjava.com/spring-aop/aspectj-after-annotation-example/)
    -   [Implementing AOP With Spring Boot and AspectJ](https://dzone.com/articles/implementing-aop-with-spring-boot-and-aspectj)
    -   [스프링 부트에서 aspectJ 형식으로 코드 참고](http://jsonobject.tistory.com/247)
    -   [AOP 슬라이드](https://slideplayer.com/slide/9380068/)
    -  [ AOP : Aspect Oriented Programming 개념](https://gmoon92.github.io/spring/aop/2019/01/15/aspect-oriented-programming-concept.html)
-   그 외
    -   [Spring Filter, Interceptor AOP 차이 및 정리](http://goddaehee.tistory.com/154)
    -   [Filter, Interceptor, AOP의 흐름](https://doublesprogramming.tistory.com/133)
    -   [filter, interceptor, aop의 차이와 그 목적](http://hayunstudy.tistory.com/53)