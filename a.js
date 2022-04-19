// "Promise 객체"를 통한 값을 전달하는 함수
function delay(dTime) {
  // Promise를 이용해 dTime 만큼의 시간이 지난 후 resolve를 통해 dTime 값을 리턴
  return new Promise((resolve) => {
    // setTimeout으로 dTime 만큼의 시간 delay를 건다
    setTimeout(() => {
      resolve(dTime);
    }, dTime);
  });
}

// 비동기 처리를 위한 함수 getApple
async function getApple(aTime) {
  const appleTime = await delay(aTime); // aTime 값 만큼의 딜레이를 await 해줌
  console.log(appleTime); // 그리고 지난 시간 출력
  return "Apple!"; // 최종적으로 "Apple!"" 리턴
}

// 비동기 처리를 위한 함수 getBanana
async function getBanana(bTime) {
  const bananaTime = await delay(bTime); // bTime 값 만큼의 딜레이를 await 해줌
  console.log(bananaTime); // 그리고 지난 시간 출력
  return "Banana!!"; // 최종적으로 "Banana!!" 리턴
}

// // 비동기 처리를 위한 함수
// async function pickFruits() {
//   // 미리 과일+Promise 변수에 할당을 해놓지 않으면
//   // "[object] + [object] has picked" 가 먼저 출력되고 숫자들이 출력됨
//   const applePromise = getApple(5000);
//   const bananaPromise = getBanana(2000);

//   // await을 해주지 않으면
//   // 병렬 처리가 되지 않아 총 7000 ms가 걸리게 된다
//   const apple = await applePromise;
//   const banana = await bananaPromise;

//   // apple과 banana에 리턴된 값을 문장으로 만들어 리턴
//   return `${apple} + ${banana} has picked`;
// }

// // 최종 리턴값을 then의 console.log를 통해 출력
// pickFruits().then(console.log);

async function pickFruits() {
  const apple = await getApple(5000);
  const banana = await getBanana(2000);
  return `${apple} + ${banana} has picked`;
}
pickFruits().then(console.log);
