import { StatusBar } from "expo-status-bar";
import {
  View,
  StyleSheet,
  Text,
  ScrollView,
  Dimensions,
  ActivityIndicator,
} from "react-native";
import React, { useState, useEffect } from "react";
import * as Location from "expo-location";
import { Fontisto } from "@expo/vector-icons";

const { width: SCREEN_WIDTH } = Dimensions.get("window");
const API_KEY = "f361d1c557f81f3d114da593925b6f44";

const icons = {
  Clouds: "cloudy",
  Clear: "day-sunny",
  Rain: "rain",
  Snow: "snow",
  Atmosphere: "cloudy-gusts",
  Drizzel: "rain",
  Thunderstorm: "lightning",
};

export default function App() {
  const [city, setCity] = useState();
  const [ok, setOk] = useState(true);
  const [days, setDays] = useState([]);

  // 위치 정보 받아오기
  const getWeather = async () => {
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
    const response = await fetch(
      `https://api.openweathermap.org/data/2.5/onecall?lat=${latitude}&lon=${longitude}&exclude=alerts&appid=${API_KEY}&units=metric`
    );
    const json = await response.json();
    setDays(json.daily);
  };

  useEffect(() => {
    getWeather();
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
        {days.length === 0 ? (
          <View style={{ ...styles.day, alignItems: "center" }}>
            <ActivityIndicator
              color="white"
              size="large"
              style={{ marginTop: 10 }}
            />
          </View>
        ) : (
          days.map((day, index) => (
            <View key={index} style={styles.day}>
              <View
                style={{
                  flexDirection: "row",
                  alignItems: "center",
                  width: "100%",
                  justifyContent: "space-between",
                }}
              >
                <Text style={styles.temp}>
                  {parseFloat(day.temp.day).toFixed(1)}
                </Text>
                <Fontisto
                  name={icons[day.weather[0].main]}
                  size={68}
                  color="white"
                />
              </View>

              <Text style={styles.description}>{day.weather[0].main}</Text>
              <Text style={styles.tinyText}>{day.weather[0].description}</Text>
            </View>
          ))
        )}
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
    fontSize: 40,
    // fontWeight: "bold",
  },
  weather: {
    // flex: 3,
  },
  day: {
    // flex: 1,
    // alignItems: "center",
    // marginLeft: 20,
    width: SCREEN_WIDTH,
  },
  temp: {
    fontSize: 100,
    marginTop: 50,
  },
  description: {
    fontSize: 40,
    // marginTop: -30,
  },
  tinyText: {
    fontSize: 20,
  },
});
// flexDirection의 기본 값: column, 웹은 row가 기본임
