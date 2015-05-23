import com.yunpian.sms.api.YunpianSmsApi;
import com.yunpian.sms.api.domain.SendInfo;
import com.yunpian.sms.api.domain.UserInfo;
import com.yunpian.sms.api.exception.ApiException;
import com.yunpian.sms.api.result.GetUserInfoResult;
import com.yunpian.sms.api.result.SendSmsResult;
import com.yunpian.sms.api.util.JsonUtil;
import junit.framework.TestCase;
import org.junit.Test;

import java.net.URLEncoder;

/**
 * yunpian sms api test.
 * Created by jiacheo on 15/5/23.
 */
public class YunpianSmsApiTest extends TestCase {

  private String mobileNo = "18757120965";

  private String text = "【云片网】您的验证码是5201314";

  private long tpl_id = 1;

  private String code = "中文验证码";

  @Test
  public void testGetUserInfo() throws ApiException {
    GetUserInfoResult getUserInfoResult = YunpianSmsApi.getUserInfo();
    assertNotNull(getUserInfoResult);
    assertTrue(getUserInfoResult.isSuccess());
    UserInfo user = getUserInfoResult.getUser();
    assertNotNull(user);
    System.out.println(JsonUtil.toJson(user));
  }

  @Test
  public void testSendSms() throws ApiException {
    SendSmsResult sendSmsResult = YunpianSmsApi.sendSms(text, mobileNo);
    assertNotNull(sendSmsResult);
    assertTrue(sendSmsResult.isSuccess());
    SendInfo result = sendSmsResult.getResult();
    assertNotNull(result);
    System.out.println(JsonUtil.toJson(result));
  }

  @Test
  public void testTplSend() throws ApiException {
    //设置对应的模板变量值
    //如果变量名或者变量值中带有#&=%中的任意一个特殊符号，需要先分别进行urlencode编码
    //如code值是#1234#,需作如下编码转换
    String codeValue = encode(code);
    String tpl_value = "#code#=" + codeValue ;
    SendSmsResult sendSmsResult = YunpianSmsApi.tplSendSms(tpl_id, tpl_value, mobileNo);
    assertNotNull(sendSmsResult);
    assertTrue(sendSmsResult.isSuccess());
    SendInfo sendInfo = sendSmsResult.getResult();
    assertNotNull(sendInfo);
    System.out.println(JsonUtil.toJson(sendInfo));
  }

  private String encode(String str) {
    try {
      return URLEncoder.encode(str, "utf-8");
    } catch (Exception e) {
      return str;
    }
  }

}
