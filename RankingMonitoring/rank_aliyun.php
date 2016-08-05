<!DOCTYPE html>
<html>
<head>
    <title>rank</title>
    <meta charset="utf-8">
    <!-- 引入 ECharts 文件 -->
   <script src="./calendar.js"></script>
   <script src='./echarts.common.min.js'></script>
</head>
<body>
<form method='get' action=''>
  <div class="fl" style="margin-right: 20px;">
            <span class="fl">选择时间段：</span> 
            <input type="text" name="start_date" id="start_date" class="input_text" size="12" value="">
            <script language="javascript" type="text/javascript">
                            Calendar.setup({
                                inputField     :    "start_date",
                                ifFormat       :    "%Y%m%d",
                            });
                        </script>
            - <input type="text" name="end_date" id="end_date" class="input_text" size="12" value="">
            <script language="javascript" type="text/javascript">
                            Calendar.setup({
                                inputField     :    "end_date",
                                ifFormat       :    "%Y%m%d",
                            });
                        </script>
	<input type="submit" class="report_searchbtn fr" value="查&nbsp;询">
    </div>  
    
</form>
   
    <?php 
       
        @$_GET['start_date'] ? $start_date = $_GET['start_date'] : $start_date ='';
        @$_GET['end_date'] ? $end_date = $_GET['end_date'] : $end_date ='';
        if($start_date !='' && $end_date !=''){
            $start = preg_replace("/(\d{4})(\d{2})(\d{2})/","$1-$2-$3",$start_date);
            $end = preg_replace("/(\d{4})(\d{2})(\d{2})/","$1-$2-$3",$end_date);
            $sql = "select * from baidu where date between  '$start' and '$end' order by date";
        }
    ?>
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
        $con = mysql_connect("ip","user","pass");
        if (!$con)
          {
          die('Could not connect: ' . mysql_error());
          }
        mysql_query("SET NAMES UTF8");
        mysql_select_db("baikedb", $con);
        if(empty($sql)){#如果sql已经配置（get到值），返回假
            $sql = "select * from baidu order by date";
        }
        $result = mysql_query($sql);
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
        $con = mysql_connect("ip","user","pass");
        if (!$con)
          {
          die('Could not connect: ' . mysql_error());
          }
        mysql_query("SET NAMES UTF8");
        mysql_select_db("baikedb", $con);
        $result = mysql_query($sql);
      
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
