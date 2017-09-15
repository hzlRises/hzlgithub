/**
     * 将网络图片下载到本地
     * @return [type] [description]
     */
    public function save_img() {
        $success = $fail = 0;

        $goods_list = $this->goods_model->get_data_for_web_img(700);
        if (empty($goods_list)) {
            return;
        }
        foreach ($goods_list as $key => $value) {
            //获取分类标识           
            $tag_arr = explode(',', rtrim($value['tag'],','));
            $tag_new = 't' . implode('-', $tag_arr);

            $new_img_name = '';
            $img_name = $value['img_name'];
            $img_arr = explode(';', $img_name);
            if (is_array($img_arr) && !empty($img_arr)) {
                foreach ($img_arr as $k => $v) {
                    $new_img_name .= $tag_new . '/' .$value['id'] . '/' . $this->saveimg_model->download_image('http://' . $v, $tag_new . '/' .$value['id']) . ";";
                }  
            }
            if ($new_img_name) {
                $res = $this->goods_model->update_new_img($value['id'], $new_img_name);
                if ($res) {
                    $success++;
                } else {
                    $fail++;
                }
            }
        }
        echo '成功:' . $success . ",失败:" . $fail . "<br/>";
    }
