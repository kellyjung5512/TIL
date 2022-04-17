import { StatusBar } from "expo-status-bar";
import { View, StyleSheet, Text, ScrollView, Dimensions } from "react-native";
import React, { useState, useEffect } from "react";
import * as Location from "expo-location";

const { width: SCREEN_WIDTH } = Dimensions.get("window");

export default function App() {
  const [city, setCity] = useState();
  const [location, setLocation] = useState("Loading...");
  const [ok, setOk] = useState(true);

  // 위치 정보 받아오기
  const ask = async () => {
    const { granted } = await Location.requestForegroundPermissionsAsync();
    if (!granted) {
      setOk(false);
    }
    const {
      coords: { latitude, longitude },
    } = await Location.getCurrentPositionAsync({ accuracy: 5 });
    const place = await Location.reverseGeocodeAsync(
      { latitude, longitude },
      { useGoogleMaps: false }
    );
    setCity(place[0].city);
  };

  useEffect(() => {
    ask();
  }, []);

  return (
    <View style={styles.container}>
      <StatusBar style="light"></StatusBar>
      <View style={styles.city}>
        <Text style={styles.cityName}>{city}</Text>
      </View>

      <ScrollView
        // 스크롤 할 때 가로로 정렬 horizontal
        horizontal
        // scrollview의 style을 가져올 때
        contentContainerStyle={styles.weather}
        // 페이징 처리 할 때
        pagingEnabled
        // 가로 스크롤 없애고 싶을 때 showsHorizontalScrollIndicator => false
        // 세로 스크롤은? showsVerticalScrollIndicator => false
        showsHorizontalScrollIndicator={false}
      >
        <View style={styles.day}>
          <Text style={styles.temp}>27</Text>
          <Text style={styles.description}>Sunny</Text>
        </View>
        <View style={styles.day}>
          <Text style={styles.temp}>27</Text>
          <Text style={styles.description}>Sunny</Text>
        </View>
        <View style={styles.day}>
          <Text style={styles.temp}>27</Text>
          <Text style={styles.description}>Sunny</Text>
        </View>
        <View style={styles.day}>
          <Text style={styles.temp}>27</Text>
          <Text style={styles.description}>Sunny</Text>
        </View>
      </ScrollView>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "teal",
  },
  city: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
  },
  cityName: {
    fontSize: 60,
    // fontWeight: "bold",
  },
  weather: {
    // flex: 3,
  },
  day: {
    // flex: 1,
    alignItems: "center",
    width: SCREEN_WIDTH,
  },
  temp: {
    fontSize: 178,
    marginTop: 50,
  },
  description: {
    fontSize: 60,
    marginTop: -30,
  },
});
// flexDirection의 기본 값: column, 웹은 row가 기본임
