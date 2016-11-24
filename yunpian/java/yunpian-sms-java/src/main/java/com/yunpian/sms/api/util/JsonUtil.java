package com.yunpian.sms.api.util;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

/**
 * Created by jiacheo on 15/5/23.
 */
public class JsonUtil {

  private static final Gson gson = new GsonBuilder().setDateFormat("yyyy-MM-dd HH:mm:ss").create();

  public static <T>T fromJson(String json, Class<T> type){
    return gson.fromJson(json, type);
  }

  public static String toJson(Object obj){
    return gson.toJson(obj);
  }

}
