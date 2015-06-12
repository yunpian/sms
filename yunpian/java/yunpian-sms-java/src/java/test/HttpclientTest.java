import junit.framework.TestCase;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.junit.Test;

/**
 * test httpclient performance :  single connection vs multi connections
 * Created by jiacheo on 15/6/12.
 */
public class HttpclientTest extends TestCase {

  private String url = "http://www.yunpian.com/v1/user/get.json";
//  private String url = "https://www.yunpian.com/v1/user/get.json";
  private int requestTimes = 500;

  //this test is for test single connection or prototype connection performance
  //it figure out that single connection's performance is better than prototype connection
  //not only https but also http

  @Test
  public void testPrototypeClient() throws Exception{
    long start = System.currentTimeMillis();
    for(int i=0; i<requestTimes; i++){
      HttpGet method = new HttpGet(url);
      CloseableHttpResponse response = HttpClients.createDefault().execute(method);
      response.getEntity();
      response.close();
    }
    long end = System.currentTimeMillis();
    System.out.println("testPrototypeClient request " + url + " " + requestTimes + " times spend " + (end-start) + "ms");
  }

  @Test
  public void testSingleClient() throws Exception{
    long start = System.currentTimeMillis();
    CloseableHttpClient client = HttpClients.createDefault();
    for(int i=0; i<requestTimes; i++){
      HttpGet method = new HttpGet(url);
      CloseableHttpResponse response = client.execute(method);
      response.getEntity();
      response.close();
    }
    long end = System.currentTimeMillis();
    System.out.println("testSingleClient request " + url  + " " + requestTimes + " times spend " + (end-start) + "ms");
  }

}
