package com.yunpian.sms.api;

import java.util.Properties;

/**
 * Created by jiacheo on 15/5/18.
 */
public class ApiConfig {

  private static final Properties properties = new Properties();

  static {
    try {
      properties.load(Thread.currentThread().getContextClassLoader().getResourceAsStream("yunpian.api.config.properties"));
    } catch (Exception e) {
      //ignore
    }
  }

  public static  final String getApiKey(){
    return properties.getProperty("APIKEY");
  }

  public static final String getUserInfoApi(){
    return properties.getProperty("userinfo.api");
  }

  public static final String getSendSmsApi() {
    return properties.getProperty("send.sms.api");
  }

  public static final String getTplSendSmsApi() {
    return properties.getProperty("send.tpl.send.api");
  }

  public static final String getEncoding() {
    return properties.getProperty("api.encoding");
  }

  public static void main(String[] args) {
    System.out.println(properties);
  }

}
