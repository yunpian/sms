package com.yunpian.sms.api.result;

import java.io.Serializable;

/**
 * Created by jiacheo on 15/5/18.
 */
public class ApiResultBase implements Serializable{

  private int code;

  private String msg;

  public int getCode() {
    return code;
  }

  public void setCode(int code) {
    this.code = code;
  }

  public String getMsg() {
    return msg;
  }

  public void setMsg(String msg) {
    this.msg = msg;
  }

  public boolean isSuccess(){
    return code == 0;
  }

}
