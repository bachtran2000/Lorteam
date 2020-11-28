// Import React and Component
import React from 'react';
import {View, Text, Alert, StyleSheet, Image} from 'react-native';
import { Ionicons } from '@expo/vector-icons'; 

import {
  DrawerContentScrollView,
  DrawerItemList,
  DrawerItem,
} from '@react-navigation/drawer';
import { widthPercentageToDP as wp, heightPercentageToDP as hp } from 'react-native-responsive-screen';


import AsyncStorage from '@react-native-community/async-storage';

const CustomSidebarMenu = (props) => {
  return (
    <View style={stylesSidebar.sideMenuContainer}>
      <View style={stylesSidebar.profileHeader}>
        <Ionicons name="md-person" size={hp('6%')} color="#153B2E" />        
        <Text style={stylesSidebar.profileHeaderText}>Đỗ Minh Đức</Text>
      </View>
      <View style={stylesSidebar.profileHeaderLine} />

      <DrawerContentScrollView {...props}>
        <DrawerItemList {...props} />
        <DrawerItem
          label={({color}) => <Text style={{color: '#153B2E', fontSize: hp('3%')}}>Đăng xuất</Text>}
          onPress={() => {
            props.navigation.toggleDrawer();
            Alert.alert(
              'Đăng xuất',
              'Bạn có chắc không? Bạn muốn đăng xuất?',
              [
                {
                  text: 'Huỷ',
                  onPress: () => {
                    return null;
                  },
                },
                {
                  text: 'Xác nhận',
                  onPress: () => {
                    AsyncStorage.clear();
                    props.navigation.replace('Auth');
                  },
                },
              ],
              {cancelable: false},
            );
          }}
        />
      </DrawerContentScrollView>
    </View>
  );
};

export default CustomSidebarMenu;

const stylesSidebar = StyleSheet.create({
  sideMenuContainer: {
    width: '100%',
    height: '100%',
    backgroundColor: '#fff',
    paddingTop: 40,
    color: 'white',
  },
  profileHeader: {
    flexDirection: 'row',
    backgroundColor: '#fff',
    padding: 15,
    textAlign: 'center',
  },
  profileHeaderText: {
    color: '#153B2E',
    alignSelf: 'center',
    paddingHorizontal: 10,
    fontWeight: 'bold',
    fontSize: hp('4%'),
    marginLeft: 10
  },
  profileHeaderLine: {
    height: 1,
    marginHorizontal: 20,
    backgroundColor: '#e2e2e2',
    marginTop: 15,
  },
});
