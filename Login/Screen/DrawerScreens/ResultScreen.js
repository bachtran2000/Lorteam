import React, { useState, useEffect } from "react";
import { FlatList, View, Text, StyleSheet, Image, Modal, Card, TouchableHighlight, SafeAreaView, Picker, TextInput, Alert,TouchableOpacity,ActivityIndicator } from 'react-native';
import { widthPercentageToDP as wp, heightPercentageToDP as hp } from 'react-native-responsive-screen';
import { NavigationContainer, useFocusEffect} from '@react-navigation/native';
import Collapsible from 'react-native-collapsible';
import { MaterialIcons, MaterialCommunityIcons } from '@expo/vector-icons'; 
import { ScrollView } from "react-native-gesture-handler";
import axios from 'axios';

function ResultScreen({ navigation }) {
    const [modalVisible, setModalVisible] = useState(false);
 
    useFocusEffect(
        React.useCallback(() => {
            setModalVisible(true);
        }, [])
    );
    const [collapsed, setCollapsed] = useState(true);
    const toggleExpanded = () => {
        setCollapsed(!collapsed);
    };
    const [vitri, setVitri] = useState('');
    const [chudautu, setChudautu] = useState('');
    const [dientich, setDientich] = useState('');
    const [sophongngu, setSophongngu] = useState('');
    const [sotoilet, setSotoilet] = useState('');
    const [huongnha, setHuongnha] = useState('');
    const [huongbancong, setHuongbancong] = useState('');
    const [duDoan,setDuDoan] = useState();
    const [thongtin, setThongtin] = useState(null);
    
   
    useEffect(() => {
      apartment = () => {
        fetch(`http://18.139.111.217:5000/apartment/?DienTich=${dientich}&Quan=${vitri}&ChuDauTu=${chudautu}&SoPhongNgu=${sophongngu}&SoToilet=${sotoilet}&HuongNha=${huongnha}&HuongBanCong=${huongbancong}`)
        .then((response) => response.json())
        .then(function(data){
          setDuDoan(data)
        })
        .catch((error) => {
          console.error(error);
        });
      };
    });
    useEffect(() => {
      timthongtin = () => {
        fetch(`http://18.139.111.217:5001/timthongtin?DienTich=90&SoToilet=2&SoPhongNgu=2&Quan=Hai%20B%C3%A0%20Tr%C6%B0ng&HuongNha=%C4%90%C3%B4ng&fbclid=IwAR1nONlK6tqHC4uHJ6tFK_oq91LNtSRLwhGkQC7KI15uA3Adq1pBJXHCz_0`)
        .then((response) => response.json())
        .then(function(data){
          setThongtin(data);
        })
        .catch((error) => {
          console.error(error);
        });
      };
    })
    
      return (
        <SafeAreaView style={{flex: 1,backgroundColor:'#fff'}}><View style={styles.priceArea}>
            <View style={styles.priceAreaChild}>
                <View style={{flex: 0.7, justifyContent:'center', alignItems:'center'}}>
                    <Text style={{marginLeft:hp('2%'), fontSize:hp('6%')}}>{duDoan}</Text>
                    <Text style={{marginLeft:hp('2%'), fontSize:hp('2.7%')}}>± {duDoan} (VND/m²)</Text>
                </View>
                <View style={{flex: 0.3, alignItems: 'center'}}><TouchableOpacity onPress={() => {setModalVisible(true)}} style={{width:hp('8%'), height: hp('8%'),marginTop:hp('2%'),borderRadius: hp('3%'), backgroundColor:'#fff'}} >
                    <Image source={{uri:'https://scontent.fhan5-7.fna.fbcdn.net/v/t1.0-9/126009221_2919994408323832_6356501572709310242_n.jpg?_nc_cat=103&ccb=2&_nc_sid=0debeb&_nc_ohc=YJlJ_4OiDosAX_7WHh5&_nc_ht=scontent.fhan5-7.fna&oh=62a78aabdaad1365e1761dc4659a634d&oe=5FDD8152'}} style={{width:hp('5%'), height: hp('5%'),marginLeft:hp('1.5%'),marginTop:hp('1.5%')}}></Image>
                </TouchableOpacity ></View>
                </View>
            </View>
            <View style={styles.listArea} >
              <View style={{flexDirection:'row', marginLeft:hp('4%'), marginTop:hp('2%')}} >
                <Image style={{width:hp('4%'), height: hp('4%')}} source={{uri:'https://scontent.fhan5-5.fna.fbcdn.net/v/t1.0-9/126294163_2920137568309516_5757696432729288507_n.jpg?_nc_cat=101&ccb=2&_nc_sid=0debeb&_nc_ohc=cqHC98QL1qIAX8t_Wpq&_nc_ht=scontent.fhan5-5.fna&oh=6aaa96036f3795fcda8a106b89f61201&oe=5FDBB8EF'}}></Image>
                <Text style={{fontSize:hp('3%'), marginLeft:hp('1%')}}>Bất động sản nổi bật</Text>
              </View>
              <View>
                <FlatList
                  data={thongtin}
                  keyExtractor={item => item.idss}
                  renderItem={({ item }) => (
                    <ScrollView  horizontal={true}>
                      <View style={styles.listItems}>
                      <Text style={{marginLeft:hp('3%'),marginRight:hp('2%')}}>{item.ViTri}</Text>
                      <Text style={{marginLeft:hp('3%'),marginRight:hp('2%')}}>Chủ đầu tư: {item.ChuDauTu}</Text>
                      <Text style={{marginLeft:hp('3%'),marginRight:hp('2%')}}>Diện tích: {item.DienTich} m2</Text>
                      </View>
                   </ScrollView>
                  )}
                />
              </View>
            </View>
            <View style={styles.mapbuttonArea}> 
                <TouchableOpacity style={styles.mapButton} onPress={() => navigation.navigate('MapScreen')}>
                    <View style={{width:hp('5.5%'), height: hp('5.5%'),marginTop:hp('2%'),borderRadius: hp('1%'), backgroundColor:'#fff', marginBottom:hp('2%'),}}><Image style={styles.searchicon} source={{uri:'https://scontent.fhan5-5.fna.fbcdn.net/v/t1.0-9/125338936_2920042264985713_2862734757864117661_n.jpg?_nc_cat=108&ccb=2&_nc_sid=0debeb&_nc_ohc=sP5NCWPMjOoAX8pSyio&_nc_ht=scontent.fhan5-5.fna&oh=42c7e663813813fc8ef00c1a4e2559cf&oe=5FDB957B'}} /></View>
                    <Text  style={styles.searchtext} onPress={() => navigation.navigate('ResultScreen')} >Xem trên bản đồ</Text>
                </TouchableOpacity>
            </View>
            <Modal animationType="slide" transparent={true} visible={modalVisible} onRequestClose={() => {Alert.alert("Modal has been closed.");}}>
              <View style={styles.centeredView}>
                <View style={styles.modalView}>
                  <View style={{borderRadius: 10, borderWidth: 1, borderColor: '#bdc3c7', overflow: 'hidden', width:hp('35%'), marginBottom:hp('2%'), alignItems: 'center' } }>
                    <Picker style={{ height: hp('6%'), width:hp('33%'),}} selectedValue={vitri} onValueChange={(itemValue, itemIndex) => setVitri(itemValue)} >
                    <Picker.Item value='' label='Vị trí' />
                    <Picker.Item label="Quận Hai Bà Trưng" value="Hai Bà Trưng" />
                    <Picker.Item label="Quận Hoàn Kiếm" value="Hoàn Kiếm" />
                    <Picker.Item label="Quận Ba Đình" value="Ba Đình" />
                    <Picker.Item label="Quận Hoàng Mai" value="Hoàng Mai"/>
                    <Picker.Item label="Quận Thanh Xuân" value="Thanh Xuân"/>
                    <Picker.Item label="Quận Đống Đa" value="Đống Đa"/>
                    <Picker.Item label="Quận Tây Hồ" value="Tây Hồ"/>
                    <Picker.Item label="Quận Cầu Giấy" value="Cầu Giấy"/>
                    <Picker.Item label="Quận Hà Đông" value="Hà Đông"/>
                    <Picker.Item label="Quận Bắc Từ Liêm" value="Bắc Từ Liêm"/>
                    <Picker.Item label="Quận Nam Từ Liêm" value="Nam Từ Liêm"/>
                    <Picker.Item label="Quận Long Biên" value="Long Biên"/>
                    <Picker.Item label="Huyện Gia Lâm" value="Gia Lâm"/>
                    <Picker.Item label="Huyện Hoài Đức" value="Hoài Đức"/>
                    <Picker.Item label="Huyện Thanh Trì" value="Thanh Trì"/>
                  </Picker>
                </View>
                <View style={{borderRadius: 10, borderWidth: 1, borderColor: '#bdc3c7', overflow: 'hidden', width:hp('35%'), marginBottom:hp('2%'), alignItems: 'center'}}>
                  <Picker style={{ height: hp('6%'), width:hp('33%'),}} selectedValue={chudautu} onValueChange={(itemValue, itemIndex) => setChudautu(itemValue)}>
                    <Picker.Item value='' label='Chủ đầu tư' />
                    <Picker.Item value='Công ty CP Eco Land' label='Công ty CP Eco Land' />
                    <Picker.Item value='Công ty CP Đầu tư Phát triển Nhà Thăng Long - Việt Nam' label='Công ty CP Đầu tư Phát triển Nhà Thăng Long - Việt Nam' />
                    <Picker.Item value='Công ty TNHH Thương mại - Quảng cáo - Xây dựng - Địa ốc Việt Hân' label='Công ty TNHH Thương mại - Quảng cáo - Xây dựng - Địa ốc Việt Hân' />
                    <Picker.Item value='Công ty CP Đầu tư Xây dựng số 9 Hà Nội' label='Công ty CP Đầu tư Xây dựng số 9 Hà Nội' />
                    <Picker.Item value='Công ty CP Tập đoàn Sunshine' label='Công ty CP Tập đoàn Sunshine' />
                    <Picker.Item value='Công ty CP tập đoàn S.S.G' label='Công ty CP tập đoàn S.S.G'/>
                    <Picker.Item value='HD Mon Holdings' label='HD Mon Holdings'/>
                    <Picker.Item value='Công ty CP Xuất nhập khẩu tổng hợp Hà Nội - Geleximco' label='Công ty CP Xuất nhập khẩu tổng hợp Hà Nội - Geleximco'/>
                    <Picker.Item value='Công ty TNHH MTV đầu tư Phương Đông' label='Công ty TNHH MTV đầu tư Phương Đông'/>
                    <Picker.Item value='Tập đoàn Vingroup' label='Tập đoàn Vingroup'/>
                    <Picker.Item value='Công ty TNHH Indochina Land' label='Công ty TNHH Indochina Land'/>
                    <Picker.Item value='Công ty CP Nông sản Agrexim' label='Công ty CP Nông sản Agrexim'/>
                    <Picker.Item value='Công ty TNHH Gamuda Land Việt Nam' label='Công ty TNHH Gamuda Land Việt Nam'/>
                    <Picker.Item value='Doanh nghiệp tư nhân xây dựng số 1 tỉnh Điện Biên' label='Doanh nghiệp tư nhân xây dựng số 1 tỉnh Điện Biên'/>
                    <Picker.Item value='Công ty CP Đầu tư Phú Thượng ' label='Công ty CP Đầu tư Phú Thượng '/>
                    <Picker.Item value='Công ty CP Đầu tư Dầu khí Toàn cầu ' label='Công ty CP Đầu tư Dầu khí Toàn cầu '/>
                    <Picker.Item value='Tân Hoàng Minh Group' label='Tân Hoàng Minh Group'/>
                    <Picker.Item value='Công ty TNHH Thiên Hương' label='Công ty TNHH Thiên Hương'/>
                    <Picker.Item value='Công ty TNHH phát triển khu đô thị Nam Thăng Long' label='Công ty TNHH phát triển khu đô thị Nam Thăng Long'/>
                    <Picker.Item value='Tổng Công ty Đầu tư phát triển nhà và đô thị Bộ Quốc Phòng ' label='Tổng Công ty Đầu tư phát triển nhà và đô thị Bộ Quốc Phòng '/>
                    <Picker.Item value='Công ty CP Đầu tư Hạ tầng và Công trình Kiến trúc Hà Nội' label='Công ty CP Đầu tư Hạ tầng và Công trình Kiến trúc Hà Nội'/>
                    <Picker.Item value='Công ty TSQ Việt Nam' label='Công ty TSQ Việt Nam'/>
                    <Picker.Item value='Công ty CP Hóa Dầu Quân Đội' label='Công ty CP Hóa Dầu Quân Đội'/>
                    <Picker.Item value='Công ty CP Terra Gold Việt Nam' label='Công ty CP Terra Gold Việt Nam'/>
                    <Picker.Item value='Công ty CP Phát triển Đô thị Từ Liêm - LIDECO, JSC' label='Công ty CP Phát triển Đô thị Từ Liêm - LIDECO, JSC'/>
                    <Picker.Item value='Công ty Cổ phần Tập đoàn FLC' label='Công ty Cổ phần Tập đoàn FLC'/>
                    <Picker.Item value='Tổng công ty Xây dựng Thanh Hóa' label='Tổng công ty Xây dựng Thanh Hóa'/>
                  </Picker>
                </View>
                <View style={{borderRadius: 10, borderWidth: 1, borderColor: '#bdc3c7', overflow: 'hidden', width:hp('35%'), marginBottom:hp('3%'), alignItems: 'center'}}>
                  <TextInput style={{ height: hp('6%'), width:hp('33%'),}} placeholder="Diện tích (m2)" onChangeText={dientich => setDientich(dientich)} defaultValue={dientich} keyboardType="numeric"/>
                </View>
                <TouchableOpacity onPress={toggleExpanded}>
                  <View style={{alignItems:'flex-end'}}>
                    <Text style={{fontSize:hp('2%'),marginBottom:hp('2%')}}>Hiển thị thêm</Text>
                </View>
                </TouchableOpacity>
                <Collapsible collapsed={collapsed} align="center">
                <View style={{borderRadius: 10, borderWidth: 1, borderColor: '#bdc3c7', overflow: 'hidden', width:hp('35%'), marginBottom:hp('2%'), alignItems: 'center'}}>
                  <Picker style={{ height: hp('6%'), width:hp('33%'),}} selectedValue={sophongngu} onValueChange={(itemValue, itemIndex) => setSophongngu(itemValue)}>
                    <Picker.Item value='' label='Số phòng ngủ' />
                    <Picker.Item label="1" value="1"/>
                    <Picker.Item label="2" value="2"/>
                    <Picker.Item label="3" value="3"/>
                    <Picker.Item label="4" value="4"/>
                    <Picker.Item label="5" value="5"/>
                  </Picker>
                </View>
                <View style={{borderRadius: 10, borderWidth: 1, borderColor: '#bdc3c7', overflow: 'hidden', width:hp('35%'), marginBottom:hp('2%'), alignItems: 'center'}}>
                  <Picker style={{ height: hp('6%'), width:hp('33%'),}} selectedValue={sotoilet} onValueChange={(itemValue, itemIndex) => setSotoilet(itemValue)}>
                    <Picker.Item value='' label='Số Toilet'/>
                    <Picker.Item label="1" value="1"/>
                    <Picker.Item label="2" value="2"/>
                    <Picker.Item label="3" value="3"/>
                  </Picker>
                </View>
                <View style={{borderRadius: 10, borderWidth: 1, borderColor: '#bdc3c7', overflow: 'hidden', width:hp('35%'), marginBottom:hp('2%'), alignItems: 'center'}}>
                  <Picker style={{ height: hp('6%'), width:hp('33%'),}} selectedValue={huongnha} onValueChange={(itemValue, itemIndex) => setHuongnha(itemValue)}>
                    <Picker.Item value='' label='Hướng nhà'/>
                    <Picker.Item label="Đông" value="Đông"/>
                    <Picker.Item label="Tây" value="Tây"/>
                    <Picker.Item label="Nam" value="Nam"/>
                    <Picker.Item label="Bắc" value="Bắc"/>
                    <Picker.Item label="Tây-Nam" value="Tây-Nam"/>
                    <Picker.Item label="Đông-Nam" value="Đông-Nam"/>
                    <Picker.Item label="Tây-Bắc" value="Tây-Bắc"/>
                    <Picker.Item label="Đông-Bắc" value="Đông-Bắc"/>
                  </Picker>
                </View>
                <View style={{borderRadius: 10, borderWidth: 1, borderColor: '#bdc3c7', overflow: 'hidden', width:hp('35%'), marginBottom:hp('2%'), alignItems: 'center'}}>
                  <Picker style={{ height: hp('6%'), width:hp('33%'),}} selectedValue={huongbancong} onValueChange={(itemValue, itemIndex) => setHuongbancong(itemValue) }>
                    <Picker.Item value='' label='Hướng ban công'/>
                    <Picker.Item label="Đông" value="Đông"/>
                    <Picker.Item label="Tây" value="Tây"/>
                    <Picker.Item label="Nam" value="Nam"/>
                    <Picker.Item label="Bắc" value="Bắc"/>
                    <Picker.Item label="Tây-Nam" value="Tây-Nam"/>
                    <Picker.Item label="Đông-Nam" value="Đông-Nam"/>
                    <Picker.Item label="Tây-Bắc" value="Tây-Bắc"/>
                    <Picker.Item label="Đông-Bắc" value="Đông-Bắc"/>
                  </Picker>
                </View>
              </Collapsible>
            <View style={{flexDirection:'row', justifyContent: 'space-around'}}>
              <TouchableHighlight style={{ ...styles.openButton, backgroundColor: "#2BC48A" }} onPress={() => {setModalVisible(!modalVisible);}}>
                <MaterialIcons name="cancel" size={24} color="white" />
              </TouchableHighlight>
              <TouchableHighlight style={{ ...styles.openButton, backgroundColor: "#2BC48A", marginLeft:hp('7%')}} onPress={() => {setModalVisible(!modalVisible); apartment(); timthongtin() }}>
                <MaterialCommunityIcons name="file-find-outline" size={24} color="white" />
              </TouchableHighlight>
            </View>
          </View>
        </View>
      </Modal>
    </SafeAreaView>
    );
  }
 export default ResultScreen;

 const styles = StyleSheet.create({
    priceArea:{
        backgroundColor:'#153B2E',
        width: wp('100%'),
        height: hp('2%'),
        flex: 0.2,
        borderBottomLeftRadius: hp('3%'),
        borderBottomRightRadius: hp('3%'),
        alignItems: "center",
    },
    priceAreaChild:{
        backgroundColor:'#FFD9B2',
        width:hp('45%'),
        height: hp('12%'),
        borderRadius: hp('2%'),
        flexDirection: 'row',
    },
    mapbuttonArea:{
        backgroundColor:'#fff',
        flex: 0.1,
        alignItems: 'center',
    },
    mapButton:{
        flexDirection: "row",
        justifyContent: 'center',
        alignItems: 'center',
        height: hp('7.5%'),
        width: wp('65%'),
        borderRadius: 10,
        borderColor: '#B9B9B9',
        backgroundColor:'#153B2E',
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
        marginLeft: hp('0.5%'),
        marginTop: hp('0.5%'),
      },
    searchtext:{
        fontSize: hp('3%'),
        color: '#fff',
        marginLeft: hp('1%'),
    },
    listArea:{
        backgroundColor:'#fff',
        flex: 0.7,
    },
    listItems:{
      backgroundColor: '#fff',
      height: hp('30%'),
      width: wp('90%'),
      borderRadius: 10,
      marginBottom: hp('1.5%'),
      marginTop: hp('3%'),
      marginLeft: hp('2%'),
      flexDirection: "column",
      shadowColor: "#000",
      shadowOffset: {
        width: 0,
       height: 2,
      },
      shadowOpacity: 0.25,
      shadowRadius: 3.84,
      elevation: 5,
    },
    

    modalView: {
        marginLeft: hp('5%'),
        marginRight: hp('5%'),
        marginTop: hp('10%'),
        backgroundColor: "white",
        borderRadius: 10,
        padding: hp('5%'),
        shadowColor: "#000",
        shadowOffset: {
          width: 0,
          height: 2
        },
        shadowOpacity: 0.25,
        shadowRadius: 3.84,
        elevation: 5,
        alignItems: 'center'
      },
    openButton: {
        backgroundColor: "#F194FF",
        borderRadius: hp('2%'),
        padding: hp('2%'),
        elevation: 2,
        marginTop: hp('1%'),
      }, 
 })
