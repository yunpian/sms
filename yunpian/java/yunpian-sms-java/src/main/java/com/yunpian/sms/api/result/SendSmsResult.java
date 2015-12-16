package com.yunpian.sms.api.result;

import com.yunpian.sms.api.domain.SendInfo;

/**
 * Created by jiacheo on 15/5/23.
 */
public class SendSmsResult extends ApiResultBase {

  private SendInfo result;

  public SendInfo getResult() {
    return result;
  }

  public void setResult(SendInfo result) {
    this.result = result;
  }
}
