import React,{ useState} from "react";
import { StyleSheet, View,Text, Image, ImageBackground, ScrollView,SafeAreaView,Modal,TouchableHighlight,Picker, TextInput, TouchableOpacity } from "react-native";
import { widthPercentageToDP as wp, heightPercentageToDP as hp } from 'react-native-responsive-screen';
import 'react-native-gesture-handler';

function HomeScreen({ navigation }) {
  return (
    <SafeAreaView style={{flex: 1,backgroundColor:'#fff'}}>
      <View style={{flex: 1, padding: 16}}>
        <View style={styles.helloWrappertar}>
          <View style={styles.helloArea}>
            <Image style={styles.hiicon} source={{uri:'https://scontent.fhan5-3.fna.fbcdn.net/v/t1.0-9/125495998_2916630491993557_7662259783795800373_n.jpg?_nc_cat=111&ccb=2&_nc_sid=0debeb&_nc_ohc=-9RrpyuaHO0AX8UmZpX&_nc_ht=scontent.fhan5-3.fna&oh=bcce0a53780e2c61853c42b334fcd210&oe=5FD71C7D'}}/>
            <Text style={styles.hellotext}>Xin chào!</Text>
          </View>
          <View style={styles.nameArea}>
            < Text style={styles.nameText}>Đỗ Minh Đức</Text>
          </View>
        </View>
        <View style={styles.searchWrappertar}>
          <ImageBackground style={styles.imageBackground} source={{uri:'https://scontent.fhan5-7.fna.fbcdn.net/v/t1.0-9/125487902_2916892415300698_7490974106393711473_n.jpg?_nc_cat=100&ccb=2&_nc_sid=0debeb&_nc_ohc=cdm7GDYTZzwAX8lO0Hc&_nc_ht=scontent.fhan5-7.fna&oh=c6c72c244e71f6d7d1392c8018dd437d&oe=5FD71B34'}}>
            <View style={styles.searchButton}>
              <Image style={styles.searchicon} source={{uri:'https://scontent.fhan5-7.fna.fbcdn.net/v/t1.0-9/125446093_2916630605326879_7586599589609321669_n.jpg?_nc_cat=103&ccb=2&_nc_sid=0debeb&_nc_ohc=UMSYoGgaw2cAX_f6mBr&_nc_ht=scontent.fhan5-7.fna&oh=09ae59ca3911d8c108f5622502afa04e&oe=5FD8A59E'}} />
              <Text style={styles.searchtext} onPress={() => navigation.navigate('ResultScreen')} >Tra cứu giá bất động sản</Text>
            </View>
          </ImageBackground>
        </View>
        </View>
      <View style={styles.newsWrappertar}>
        <View style={styles.newstextArea}>
          <Image style={styles.newsicon} source={{uri:'https://scontent.fhan5-6.fna.fbcdn.net/v/t1.0-9/125458342_2916630541993552_8552025525227791473_n.jpg?_nc_cat=105&ccb=2&_nc_sid=0debeb&_nc_ohc=Ecfk1w3HFzAAX8dQ2WT&_nc_ht=scontent.fhan5-6.fna&oh=1a7923c148a3ff67f2c2094af7925e5d&oe=5FD778C7'}}/>
          <Text style={styles.newstext}>Tin tức</Text>
        </View>
        <View style={styles.newsScrollview}>
          <ScrollView contentContainerStyle={{ flexDirection:"column"}} >
            <View style={styles.newsItem}>
              <View style={styles.newsItemImage}>
                <Image style={styles.newsImage} source={{uri:'https://nhaban24h.com.vn/wp-content/uploads/2019/03/bat-dong-san-binh-duong-1.jpg'}}/>
              </View>
              <View style={styles.newsItemText}>
                <Text style={styles.newsItemTime}>12-11-2020 12:45</Text>
                <Text style={styles.newsItemTextTitle}>Bất ngờ với một siêu dự án tại Hà Nội</Text>
              </View>
            </View>
            <View style={styles.newsItem}>
            <View style={styles.newsItemImage}>
                <Image style={styles.newsImage} source={{uri:'https://cafefcdn.com/thumb_w/650/pr/2020/1605518826609-0-142-804-1428-crop-1605518830868-63741142435428.jpg'}}/>
              </View>
              <View style={styles.newsItemText}>
                <Text style={styles.newsItemTime}>12-11-2020 12:45</Text>
                <Text style={styles.newsItemTextTitle}>Căn hộ xanh khó tìm ở trung tâm Hà Nội</Text>
              </View>
            </View>
            <View style={styles.newsItem}>
            <View style={styles.newsItemImage}>
                <Image style={styles.newsImage} source={{uri:'https://cafefcdn.com/thumb_w/650/203337114487263232/2020/11/17/photo1605576369760-16055763699121442299738.jpg'}}/>
              </View>
              <View style={styles.newsItemText}>
                <Text style={styles.newsItemTime}>12-11-2020 12:45</Text>
                <Text style={styles.newsItemTextTitle}>Thị trường BĐS Hà Nội sôi động những tháng cuối năm</Text>
              </View>
            </View>
            <View style={styles.newsItem}>
            <View style={styles.newsItemImage}>
                <Image style={styles.newsImage} source={{uri:'https://cafefcdn.com/thumb_w/650/203337114487263232/2020/11/16/photo1605503891302-1605503891791624714041.jpg'}}/>
              </View>
              <View style={styles.newsItemText}>
                <Text style={styles.newsItemTime}>12-11-2020 12:45</Text>
                <Text style={styles.newsItemTextTitle}>Sắp đến thời điểm vàng của thị trường bất động sản</Text>
              </View>
            </View>
          </ScrollView>
        </View>
      </View>
    </SafeAreaView>
  );
};


const styles = StyleSheet.create({
  headerWrappertar: {
    backgroundColor: '#fff',
    flexDirection: "row",
    marginTop: hp('10%'),
  },
  helloWrappertar:{
    backgroundColor: '#fff',
    justifyContent: 'center',
    marginLeft: hp('2%'),
  },
  helloArea:{
    flexDirection: "row",
  },
  hiicon:{
    width: hp('5%'),
    height: hp('5%  '),
    backgroundColor: '#fff',
  },
  nameText:{
    fontSize: hp('4.5%'),
    color: '#2BC48A',
  },
  hellotext:{
    fontSize: hp('3%'),
    color: '#000',
    marginLeft: hp('1%'),
  },
  searchWrappertar: {
    flex: 1.2,
    backgroundColor: '#fff',
    alignItems: 'center',
  },
  searchButton:{
    flexDirection: "row",
    justifyContent: 'center',
    alignItems: 'center',
    marginTop: hp('1%'),
    height: hp('7%'),
    width: wp('85%'),
    borderRadius: 10,
    borderColor: '#B9B9B9',
    backgroundColor:'#fff',
    shadowColor: "#000",
    shadowOffset: {
	    width: 0,
	   height: 2,
    },
    shadowOpacity: 0.25,
    shadowRadius: 3.84,
    elevation: 5,
  },
  searchicon:{
    width: hp('4%'),
    height: hp('4% '),
  },
  searchtext:{
    fontSize: hp('3%'),
    color: '#B9B9B9',
    marginLeft: hp('1%'),
  },
  imageBackground:{
    resizeMode: "center",
    justifyContent: "center",
    flex: 1,
  },
  newsWrappertar: {
    flex: 1,
    backgroundColor: '#fff',
    marginLeft: hp('3%'),
  },
  newstextArea:{
    flexDirection: 'row',
    marginLeft: hp('2%'),
  },
  newsScrollview:{
    alignItems: 'center',
    justifyContent: 'center',
  },
  newsicon:{
    width: hp('5%'),
    height: hp('5%  '),
    backgroundColor: '#fff',
  },
  newstext:{
    fontSize: hp('3.5%'),
    color: '#000',
    marginLeft: hp('1%'),
  },
  newsItem:{
    backgroundColor: '#fff',
    height: hp('15%'),
    width: wp('85%'),
    borderRadius: 10,
    marginBottom: hp('1.5%'),
    marginTop: hp('1.5%'),
    marginLeft: hp('1.5%'),
    marginRight: hp('5%'),
    flexDirection: "row",
    shadowColor: "#000",
    shadowOffset: {
	    width: 0,
	   height: 2,
    },
    shadowOpacity: 0.25,
    shadowRadius: 3.84,
    elevation: 5,
  },
  newsItemImage:{
    flex: 0.35,
  },
  newsItemText:{
    flex: 0.65,
    marginTop: hp('1%'),
    marginBottom: hp('1%'),
    marginLeft:hp('1%'), 
  },
  newsItemTime:{
    fontSize: hp('1.5%'),
    marginLeft: hp('14%'),
  },
  newsImage:{
    width: hp('13%'),
    height: hp('13%'),
    marginLeft: hp('1%'),
    marginTop: hp('1%'),
  },
  newsItemTextTitle:{
    fontSize: hp('3%'),
  },
});

export default HomeScreen;