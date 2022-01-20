import { useState } from 'react';

const EventPractice = () => {
  const [form, setForm] = useState({
    username: '',
    message: '',
  });

  const { username, message } = form;
  const onChange = e => {
    const nextForm = {
      ...form,
      [e.target.name]
    };
    setForm(nextForm);
  };

  const onClick = () => {
    alert(username + ': ' + message);
    setUsername('');
    SetMessage('');
  };

  const onKeyPress = (e) => {
    if (e.key === 'Enter') {
      onClick();
    }
  };
}
  return (
    <div>
      <h1>이벤트 연습</h1>

      <input
        type="text"
        name="username"
        value={username}
        placeholder="사용자명"
        onChange={onChangeUsername}
      />

      <input
        type="text"
        name="message"
        value={message}
        placeholder="사용자명"
        onChange={onChangeMessage}
        onKeyPress={onKeyPress}
      />

      <button onClick={onClick}>확인</button>
    </div>
  );
};

export default EventPractice;
