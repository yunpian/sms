package com.yunpian.sms.api.domain;

import com.yunpian.sms.api.result.ApiResultBase;

/**
 * Created by jiacheo on 15/5/18.
 */
public class SendInfo extends ApiResultBase {

  private Integer count;

  private Integer fee;

  private Long sid;

  public Integer getCount() {
    return count;
  }

  public void setCount(Integer count) {
    this.count = count;
  }

  public Integer getFee() {
    return fee;
  }

  public void setFee(Integer fee) {
    this.fee = fee;
  }

  public Long getSid() {
    return sid;
  }

  public void setSid(Long sid) {
    this.sid = sid;
  }
}
