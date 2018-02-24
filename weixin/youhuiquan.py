#coding:utf-8
import itchat,json,time
import requests,sys
import urllib
reload(sys) 
sys.setdefaultencoding('utf-8')

@itchat.msg_register(itchat.content.TEXT)
# 注册消息响应事件，消息类型为itchat.content.TEXT，即文本消息
def text_reply(msg):
	print msg['Text']#unicode
#	msg['Text'].encode("utf-8")  unicode转为 str
#	print urllib.quote(msg['Text'].encode("utf-8"))	
	url = 'http://yhq.techseo.cn/yhq/?r=l&kw=%s'%(urllib.quote(msg['Text'].encode("utf-8")))	
	print url
	message = u'一一一一导 购 信 息一一一一\n已为您找到:%s\n点击下方链接查看\n%s'%(msg['Text'],url)
	itchat.send(message,msg.fromUserName)
#	return url


#处理群消息
@itchat.msg_register([itchat.content.TEXT, itchat.content.SHARING], isGroupChat=True)
def group_reply_text(msg):
	chatroom_id = msg['FromUserName']
	username = msg['ActualNickName']
	
	if chatroom_id == '@@a3f3bfafe461ecb368a6c602e42d1cb6f4a26fca1fff90215a69653298af31b5' and msg['Type'] == itchat.content.TEXT:
		url = 'http://yhq.techseo.cn/yhq/?r=l&kw=%s'%(urllib.quote(msg['Text'].encode("utf-8")))
		itchat.send(u'一一一一导 购 信 息一一一一\n已为您找到:%s\n点击下方链接查看\n%s'%(msg['Text'],url),'@@a3f3bfafe461ecb368a6c602e42d1cb6f4a26fca1fff90215a69653298af31b5')

		
# 处理好友添加请求
@itchat.msg_register(itchat.content.FRIENDS)
def add_friend(msg):
    # 该操作会自动将新好友的消息录入，不需要重载通讯录
    itchat.add_friend(**msg['Text'])
    # 加完好友后，给好友打个招呼
    itchat.send_msg('你好，我是优惠券机器人，想找什么优惠券直接发给我，我帮你找！', msg['RecommendInfo']['UserName'])
		
		
		
		
def  main():
	itchat.auto_login(hotReload=True)
	itchat.run()
#itchat.send('Hello, filehelper', toUserName='filehelper')
	
if __name__ == "__main__":
	main()
	

	
	
	
'''
#coding:utf-8
import requests,time,md5,sys
import top.api
#hzl
reload(sys)
sys.setdefaultencoding("utf-8")

def get_goods_id_by_url():
	pass
	
def main():
	product_url = 'http://detail.tmall.com/item.htm?id=543478119787'
	product_id = 543478119787
	Key = 23558049
	Secret = '85029326775b7cb3922bebdfa4f2f3e9'
	site_id = 19454296#二营长
	url = 'http://gw.api.taobao.com/router/rest?'
	now = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
	#adzone_id19454296
	#sign = '%sadzone_id19454296app_key23558049fieldsnum_iid,click_urlformatjsonmethodtaobao.tbk.item.convertnum_iids%ssign_methodmd5timestamp%sv2.0%s'%(Secret,product_id,now,Secret)
	sign = ''	
	params = {
	'adzone_id':'%s'%site_id,
	'app_key':'23558049',
	'fields':'num_iid,click_url,title',
	'format':'json',
	'method':'taobao.tbk.item.convert',
	'num_iids':'%s'%product_id,	
	'sign_method':'md5',
	'timestamp':now,	
	'v':'2.0'
	}
	
	for k,v in params:
		print k,v
	
	m1 = md5.new()
	m1.update(sign)
	sign = m1.hexdigest()

	url = 'http://gw.api.taobao.com/router/rest?sign=%s'sign
	
	r = requests.get(url,params=params)
	
if __name__ == '__main__':
	main()
	
	
'''
<?php

/**
 * yyl
 */
include APPPATH . 'third_party/taobao/TopSdk.php';

class Tool_model extends CI_Model {

    public $tablename;
    private	$categorys;

    public $jd_app_key = 'EB8F6A216D59DFCCA6F899B02C0BE586';
    public $jd_app_secret = '6a53c05b035e4022ae63d46c527cef5e';
    private $unionId = '1000256765';
    private $webId = '1043583033';

    public $app_key_tb = '24641064';
    public $app_secret_tb = '3e5bc31c602a003a27a480235787393a';
    public $site_id_tb = 37264238;

    public function __construct() {
        parent::__construct();
        $this->tablename = $this->db->dbprefix('goods');
    }

    public function switch_tb($url) {
        // $url: http://detail.tmall.com/item.htm?id=543478119787
        $goods_id = $this->get_goods_id_by_url($url);
        // App Key： 24641064
        // App Secret： 3e5bc31c602a003a27a480235787393a
        $zone_id = 37264238;
        //参数数组
        $param_arr = array(
             'app_key' => $this->app_key_tb,
             'method' => 'taobao.tbk.item.convert',
             'format' => 'json',
             'v' => '2.0',
             'sign_method'=>'md5',
             'timestamp' => date('Y-m-d H:i:s'),
             'fields' => 'num_iid,click_url',
             'num_iids' => $goods_id,
             'adzone_id' => $zone_id,
        );
        //生成签名
        $sign = $this->create_sign_tb($param_arr);
        //组织参数
        $str_param = $this->create_str_param_tb($param_arr);
        $str_param .= 'sign='.$sign;
        //访问服务
        $url = 'http://gw.api.taobao.com/router/rest?'.$str_param;
        $result = file_get_contents($url);
        $result = json_decode($result);
        
        return $result;

    }

    private function get_goods_id_by_url($url) {
        $url_arr = parse_url($url);
        $query = $url_arr['query'];
        $arr = explode('=', $query);
        $goods_id = $arr[1];
        if ($goods_id) {
            return $goods_id;
        }
        return '';
    }

    public function get_goods_info_tb($url) {
        $c = $this->tb_ap

'''


'''
