<!DOCTYPE html>
<html>
<head>
	<title>rank</title>
    <meta charset="utf-8">
    <!-- 引入 ECharts 文件 -->
    <script src="echarts.common.min.js"></script>
</head>
<body>
    <div id="main" style="width: 600px;height:400px;margin:0 auto;">
	   <script type="text/javascript">
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('main'));

        // 指定图表的配置项和数据
        var option = {
    title: {
        text: '家居知识排名情况'
    },
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data:['pcrank','waprank']
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    toolbox: {
        feature: {
            saveAsImage: {}
        }
    },
    xAxis: {
        type: 'category',
        boundaryGap: false,	        
		<?php		
        $con = mysql_connect("rm-2ze2ec4330fud59f6o.mysql.rds.aliyuncs.com","baike","2016Hzl");
        if (!$con)
          {
          die('Could not connect: ' . mysql_error());
          }

        mysql_query("SET NAMES UTF8");
        mysql_select_db("baikedb", $con);
        $result = mysql_query("select * from baidu order by date");

        echo 'data : [';
        while($row = mysql_fetch_array($result))
          {
          echo "'".$row['date']."'";
          echo ",";
          }
        echo ']';
        mysql_close($con);
	   ?>
    },
    yAxis: {
        type: 'value'
    },
    series: [
        <?php

        $con = mysql_connect("rm-2ze2ec4330fud59f6o.mysql.rds.aliyuncs.com","baike","2016Hzl");
        if (!$con)
          {
          die('Could not connect: ' . mysql_error());
          }
        mysql_query("SET NAMES UTF8");
        mysql_select_db("baikedb", $con);
        $result = mysql_query("select * from baidu order by date");
      

        for ($x=1;$x<=2;$x++) {

          $re_name = mysql_field_name($result,$x);
          echo " {name:'".$re_name."',type:'line',line: '排名',data:[ ";
          while($row = mysql_fetch_array($result))
            {
            echo $row[$x].',';
            }
          echo ']},';
          mysql_data_seek($result,0);

        }

        mysql_close($con);
       ?>      
    ]
};

        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
    </script>
	
	</div>

</body>

</html>