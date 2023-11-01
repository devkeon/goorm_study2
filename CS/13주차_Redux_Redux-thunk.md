# Redux + Redux Thunk

## Redux

- 자바스크립트 앱을 위한 예측 가능한 상태 컨테이너
- `props` 문법을 사용하지 않아도 된다.
- 상태 변경 관리가 용이하다.
- Redux Toolkit?

**핵심 원칙**

- 단일 진실 원천 (store).
- 상태는 읽기 전용 (액션을 통한 변경).
- 순수 함수 (reducer)를 통한 변경.

**왜 Redux인가?**

- 예측 가능: 액션과 리듀서로 인해 상태 변경이 추적 가능.
- 디버그 가능: Redux DevTools와 같은 도구를 사용하여 시간 여행 디버깅 가능.
- 생태계 & 커뮤니티: 미들웨어, 통합, 강력한 커뮤니티 지원.

![Untitled](Redux%20+%20Redux%20Thunk%20304cbb96279e4f6388f9712f9a4c28cd/Untitled.png)

**기존 React 방식 대로라면**

- 각 컴포넌트사이에서 상태(변수)를 공유하기 위해 props문법을 사용한다.
- 하지만 이런 경우 컴포넌트를 많이 쌓다보면 상태를 전해주기 위해 props문법을 매우 많이 사용해야 한다는 단점이 있다.
- 또한 각각의 컴포넌트가 상태를 변경시킬 경우 갑자기 상태에 문제가 생겼다면 각각의 수많은 컴포넌트들을 하나씩 살피면서 추적해야한다.

**Redux를 사용한다면**

- state를 보관하는 파일(스토어)을 만들어서 해당 파일에 보관하고 싶은 state를 보관할 수 있다.
- 보관된 state들은 모든 컴포넌트에서 직접 꺼내서 쓸 수 있고 props 문법을 사용하지 않아도 되기 때문에 코드가 전체적으로 짧아진다.
- redux를 사용하여 보관한 상태를 변경시키는 수정 방법을 미리 정의해놓고, 각 컴포넌트들은 직접 상태를 변경시키는 것이 아니라 수정해달라는 요청만 보내서 상태를 변경한다.
- 그렇게 되면 상태를 수정하는 곳이 하나밖에 없기 때문에 갑자기 상태 값 변경에 문제가 생겼을 때 추적하기가 용이하다.

![Untitled](Redux%20+%20Redux%20Thunk%20304cbb96279e4f6388f9712f9a4c28cd/Untitled%201.png)

### Redux 기본용어

![image.gif](Redux%20+%20Redux%20Thunk%20304cbb96279e4f6388f9712f9a4c28cd/image.gif)

**Store**

스토어는 컴포넌트의 상태를 관리하는 저장소이다. 하나의 프로젝트는 하나의 스토어만 가질 수 있다.

**Action**

스토어의 상태를 변경하기 위해서는, 액션을 생성해야한다. 액션은 객체이며, 반드시 type을 가져야 한다. 액션 객체는 액션생성함수에 의해서 만들어진다.

**Reducer**

리듀서는 현재 상태와 액션 객체를 받아 새로운 상태를 리턴하는 함수다.

**Dispatch**

디스패치는 스토어의 내장 함수 중 하나이며, 액션 객체를 넘겨줘 상태를 업데이트 시켜주는 역할을 한다.

**Subscribe**

스토어의 내장 함수 중 하나로, 리듀서가 호출될 때 서브스크라이브된 함수 및 객체를 호출한다.

아래의 그림으로 위의 용어들을 이해해보자.

### Redux-thunk

- 리덕스를 사용하는 프로젝트에서 비동기 작업을 처리할 때 사용하는 미들웨어
- 객체 대신 함수를 생성하는 액션 생성함수를 작성 할 수 있게 해준다.
- 함수를 디스패치할 수 있다 → 해당 함수에서 dispatch와 getState를 파마리터로 받아와야 한다 → 이 함수를 만들 수 있게 해주는 것이 thunk이다.

**예를 들어**

```jsx
const addOne = x => x+1;
addOne(1); //2
```

위 addOne 함수는 호출 시에 바로 1+1이 연산된다. 그런데 이 연산 작업을 미루고 싶다면

```jsx
const addOne = x => x+1;
function addOneThunk (x) {
	const thunk = () => addOne(x);
	return thunk;
}

const fn = addOneThunk(1);
setTimeout(() => {
	const value = fn();
	console.log(value);
}, 1000); 
```

이렇게 연산 작업을 fn()이 실행되는 시점에 수행되도록 미룰 수 있다. redux-thunk도 이와 같은 방식으로 동작한다.

redux-thunk 미들웨어는 객체 대신 함수를 생성하는 액션 생성함수를 작성 할 수 있게 해준다. 리덕스에서는 기본적으로는 액션 객체를 디스패치한다. 일반 액션 생성자는, 다음과 같이 파라미터를 가지고 액션 객체를 생성하는 작업만 한다.

```jsx
const actionCreator = (payload) => ({action: 'ACTION', payload});
```

만약 특정 액션이 몇초뒤에 실행되게 하거나, 상태에 따라 아예 액션이 무시되게 하려면, 일반 액션 생성자로는 할 수가 없다. redux-thunk 는 이를 가능하게 한다.

```jsx
$ yarn add redux-thunk //설치
```

## ****`index.js`****

```jsx
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import { createStore, applyMiddleware } from 'redux';
import { Provider } from 'react-redux'; //react 컴포넌트 트리 전체에 redux 스토어 제공
import rootReducer from './modules';
import logger from 'redux-logger';
import { composeWithDevTools } from 'redux-devtools-extension'; //
import ReduxThunk from 'redux-thunk'; //redux-thunk 사용

const store = createStore(
  rootReducer,
  composeWithDevTools(applyMiddleware(ReduxThunk, logger))
); //스토어 생성

ReactDOM.render(
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById('root')
);
```

리덕스 thunk를 사용하려면 store를 생성할 때 redux-thunk 미들웨어를 적용해주어야 한다. 

## ****`counter.js`****

```jsx
// 액션 타입
const INCREASE = 'INCREASE';
const DECREASE = 'DECREASE';

// 액션 생성 함수
export const increase = () => ({ type: INCREASE });
export const decrease = () => ({ type: DECREASE });

export const increaseAsync = () => dispatch => {
  setTimeout(() => dispatch(increase()), 1000);
};
export const decreaseAsync = () => dispatch => {
  setTimeout(() => dispatch(decrease()), 1000);
};

// 초깃값
const initialState = 0;

export default function counter(state = initialState, action) {
  switch (action.type) {
    case INCREASE:
      return state + 1;
    case DECREASE:
      return state - 1;
    default:
      return state;
  }
}
```

## `C****ounterContainer.js****`

```jsx
import React from 'react';
import Counter from '../components/Counter';
import { useSelector, useDispatch } from 'react-redux';
import { increaseAsync, decreaseAsync } from '../modules/counter';

function CounterContainer() {
  const number = useSelector(state => state.counter);
  const dispatch = useDispatch();

  const onIncrease = () => {
    dispatch(increaseAsync());
  };
  const onDecrease = () => {
    dispatch(decreaseAsync());
  };

  return (
    <Counter number={number} onIncrease={onIncrease} onDecrease={onDecrease} />
  );
}

export default CounterContainer;
```

![LSXLv2C.gif](Redux%20+%20Redux%20Thunk%20304cbb96279e4f6388f9712f9a4c28cd/LSXLv2C.gif)

### **Thunk Use Cases**

- 복잡한 로직을 컴포넌트 밖으로 이동
- 비동기 요청 또는 기타 비동기 로직 만들기
- 연속적으로 또는 시간에 따라 여러 작업을 디스패치해야 하는 로직 작성
- 의사 결정을 내리거나 다른 상태 값을 액션에 포함하기 위해 getState에 액세스해야 하는 로직 작성

**주의**

- thunk는 수명 주기가 없는 '단발성' 기능이다. 또한 다른 디스패치된 액션을 볼 수 없다. 따라서 일반적으로 웹 소켓과 같은 영구 연결을 초기화하는 데 사용해서는 안 되며, 다른 작업에 응답하는 데 사용할 수도 없다.