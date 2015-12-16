package com.yunpian.sms.api.domain;

import com.yunpian.sms.api.result.ApiResultBase;

/**
 * Created by jiacheo on 15/5/18.
 */
public class SendInfo extends ApiResultBase {

  private Integer count;

  private Double fee;

  private String sid;

  public Integer getCount() {
    return count;
  }

  public void setCount(Integer count) {
    this.count = count;
  }

  public Double getFee() {
    return fee;
  }

  public void setFee(Double fee) {
    this.fee = fee;
  }

  public String getSid() {
    return sid;
  }

  public void setSid(String sid) {
    this.sid = sid;
  }
}
