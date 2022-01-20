import { Component } from 'react';

class Temp2 extends Component {
  render() {
    return (
      <div>
        <h1>이벤트 연습</h1>
        <input
          type="text"
          name="message"
          placeholder="아무거나 입력하세요"
          onChange={(e) => console.log(e.target.name)}
        />
      </div>
    );
  }
}

export default Temp2;
