package com.yunpian.sms.api.result;

import com.yunpian.sms.api.domain.SendInfo;

/**
 * Created by bingone on 15/12/16.
 */
public class SendVoiceResult {
    private SendInfo result;

    public SendInfo getResult() {
        return result;
    }

    public void setResult(SendInfo result) {
        this.result = result;
    }
}
