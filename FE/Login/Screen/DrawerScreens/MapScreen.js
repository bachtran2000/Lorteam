import React, { Component } from 'react';
import {StyleSheet,Text,View,Animated,Image,Dimensions} from "react-native";
import MapView from 'react-native-maps';

const Images = [
  { uri: "https://image.plo.vn/w653/Uploaded/2020/mrwqldxwp/2020_05_03/chungcu_bhnr.jpg" },
  { uri: "https://lh3.googleusercontent.com/proxy/lLckaeeam3y-r1HnYRuMAqJAZStydYZpllvxrMlXKpArn85E84rAVt5mgSzBBq42cJtZXXp7QEbGpzN_VFb7E-FY6UDW66pb5WmZhAPAWgDZyQ8ZMHv-E_r1" },
  { uri: "https://giathuecanho.com/wp-content/uploads/2019/03/King-Center.jpg" },
  { uri: "https://vnn-imgs-f.vgcloud.vn/2020/07/07/18/hon-3-000-can-ho-chung-cu-o-da-nang-su-dung-khong-dung-muc-dich-2.jpg" },
  { uri: "https://file4.batdongsan.com.vn/crop/490x294/2020/10/15/hmcVYWuR/20201015104459-0a2f.jpg" }
]
const { width, height } = Dimensions.get("window");
const CARD_HEIGHT = height / 4;
const CARD_WIDTH = CARD_HEIGHT - 50;

export default class MapScreen extends Component {
  
  state = {
    markers: [
      {
        coordinate: {
          latitude:21.009282681828243,
          longitude:105.82745677933846,
        },
        title: "90's Home",
        description: "30 triệu/m²",
        image: Images[0],
      },
      {
        coordinate: {
          latitude:21.00469216269175, 
          longitude:105.83950636540337,
        },
        title: "Tập thể nam đồng",
        description: "45 triệu/m²",
        image: Images[1],
      },
      {
        coordinate: {
          latitude:21.012083725942936, 
          longitude:105.83287594471834,
        },
        title: "Khu Ngoại Giao Đoàn Trung Tự",
        description: "35 triệu/m²",
        image: Images[2],
      },
      {
        coordinate: {
          latitude:21.005459809330812, 
          longitude:105.82413849140465,
        },
        title: "Mipec Palace",
        description: "32 triệu/m²",
        image: Images[3],
      },
      {
        coordinate: {
          latitude:21.00619583680554, 
          longitude:105.83171043359157,
        },
        title: "Mipec Vincom Phạm Ngọc Thạch",
        description: "38 triệu/m²",
        image: Images[4],
      },
    ],
    region: {
      latitude: 21.0092826, 
      longitude: 105.8272191,
      latitudeDelta: 0.04,
      longitudeDelta: 0.05,
    },
  };

  UNSAFE_componentWillMount() {
    this.index = 0;
    this.animation = new Animated.Value(0);
  }
  UNSAFE_componentDidMount() {
    this.animation.addListener(({ value }) => {
      let index = Math.floor(value / CARD_WIDTH + 0.3); 
      if (index >= this.state.markers.length) {
        index = this.state.markers.length - 1;
      }
      if (index <= 0) {
        index = 0;
      }

      clearTimeout(this.regionTimeout);
      this.regionTimeout = setTimeout(() => {
        if (this.index !== index) {
          this.index = index;
          const { coordinate } = this.state.markers[index];
          this.map.animateToRegion(
            {
              ...coordinate,
              latitudeDelta: this.state.region.latitudeDelta,
              longitudeDelta: this.state.region.longitudeDelta,
            },
            350
          );
        }
      }, 10);
    });
  }

  render() {
    const interpolations = this.state.markers.map((marker, index) => {
      const inputRange = [
        (index - 1) * CARD_WIDTH,
        index * CARD_WIDTH,
        ((index + 1) * CARD_WIDTH),
      ];
      const scale = this.animation.interpolate({
        inputRange,
        outputRange: [1, 2.5, 1],
        extrapolate: "clamp",
      });
      const opacity = this.animation.interpolate({
        inputRange,
        outputRange: [0.35, 1, 0.35],
        extrapolate: "clamp",
      });
      return { scale, opacity };
    });

    return (
      <View style={styles.container}>
        <MapView
          ref={map => this.map = map}
          initialRegion={this.state.region}
          style={styles.container}
        >
          {this.state.markers.map((marker, index) => {
            const scaleStyle = {
              transform: [
                {
                  scale: interpolations[index].scale,
                },
              ],
            };
            const opacityStyle = {
              opacity: interpolations[index].opacity,
            };
            return (
              <MapView.Marker key={index} coordinate={marker.coordinate}>
                <Animated.View style={[styles.markerWrap, opacityStyle]}>
                  <Animated.View style={[styles.ring, scaleStyle]} />
                  <View style={styles.marker} />
                </Animated.View>
              </MapView.Marker>
            );
          })}
        </MapView>
        <Animated.ScrollView
          horizontal
          scrollEventThrottle={1}
          showsHorizontalScrollIndicator={false}
          snapToInterval={CARD_WIDTH}
          onScroll={Animated.event(
            [
              {
                nativeEvent: {
                  contentOffset: {
                    x: this.animation,
                  },
                },
              },
            ],
            { useNativeDriver: true }
          )}
          style={styles.scrollView}
          contentContainerStyle={styles.endPadding}
        >
          {this.state.markers.map((marker, index) => (
            <View style={styles.card} key={index}>
              <Image
                source={marker.image}
                style={styles.cardImage}
                resizeMode="cover"
              />
              <View style={styles.textContent}>
                <Text numberOfLines={1} style={styles.cardtitle}>{marker.title}</Text>
                <Text numberOfLines={1} style={styles.cardDescription}>
                  {marker.description}
                </Text>
              </View>
            </View>
          ))}
        </Animated.ScrollView>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  scrollView: {
    position: "absolute",
    bottom: 30,
    left: 0,
    right: 0,
    paddingVertical: 10,
  },
  endPadding: {
    paddingRight: width - CARD_WIDTH,
  },
  card: {
    padding: 10,
    elevation: 2,
    backgroundColor: "#FFF",
    marginHorizontal: 10,
    shadowColor: "#000",
    shadowRadius: 5,
    shadowOpacity: 0.3,
    shadowOffset: { x: 2, y: -2 },
    height: CARD_HEIGHT,
    width: CARD_WIDTH,
    overflow: "hidden",
  },
  cardImage: {
    flex: 3,
    width: "100%",
    height: "100%",
    alignSelf: "center",
  },
  textContent: {
    flex: 1,
  },
  cardtitle: {
    fontSize: 12,
    marginTop: 5,
    fontWeight: "bold",
  },
  cardDescription: {
    fontSize: 12,
    color: "#444",
  },
  markerWrap: {
    alignItems: "center",
    justifyContent: "center",
  },
  marker: {
    width: 10,
    height: 10,
    borderRadius: 5,
    backgroundColor: "rgba(130,4,150, 0.9)",
  },
  ring: {
    width: 30,
    height: 30,
    borderRadius: 15,
    backgroundColor: "rgba(130,4,150, 0.3)",
    position: "absolute",
    borderWidth: 1,
    borderColor: "rgba(130,4,150, 0.5)",
  },
});