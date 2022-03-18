import styled from "styled-components";

const Father = styled.div`
  display: flex;
`;

const Box = styled.div`
  background-color: ${(props) => props.bgColor};
  width: 100px;
  height: 100px;
`;

const Text = styled.span`
  color: white;
`;

const Circle = styled(Box)`
  border-radius: 50px;
`;

const Btn = styled.button`
  color: white;
  background-color: tomato;
  border: 0;
  border-radius: 15px;
`;

const Input = styled.input.attrs({ required: true })`
  background-color: tomato;
`;

function App() {
  return (
    <Father>
      {/*
      // Box styled 하나로 여러가지 props 전달 받기
      <Box bgColor="teal">
        <Text>hello</Text>
      </Box>
      <Circle bgColor="tomato" /> */}

      {/*
      // button 태그 -> a 태그로 바꾸는 방법
      <Btn>Log in</Btn>
      <Btn as="a" href="/">
        Log in
      </Btn> */}

      {/* 
      // styled로 attrs(속성) 적용하기
      <Input />
      <Input />
      <Input /> */}
    </Father>
  );
}

export default App;
