import React, {Component} from 'react';
import './App.css';
import Jumbotron from './Jumbotron'

class App extends Component {
	render() {
	  return (
		<div className="App">
			<Jumbotron 
				title={'예발자닷컴'} 
				content={'예비개발자를 위한 무료 부트캠프 코스를 한 눈에 비교하세요.'}>
			</Jumbotron>
		</div>
	  );
	}
  }

  export default App;