# 语音技术与自然语言处理作业
## 语料库 
* qingyun中文语料库

## 项目结构

```
│  .gitignore
│  config.py               #模型配置参数
│  corpus.pth              #已经过处理的数据集
│  dataload.py             #dataloader
│  datapreprocess.py       #数据预处理
   serve.py                #聊天机器人服务器
│  main.py               
│  model.py       
│  README.md
│  requirements.txt
│  train_eval.py            #训练和验证,测试
│  
├─checkpoints              
│      chatbot_0509_1437   #已经训练好的模型
│      
├─clean_chat_corpus
│      qingyun.tsv         #语料库
│      
└─utils
        beamsearch.py      #未完全实现
        greedysearch.py    #贪婪搜索，用于测试
        __init__.py
```



安装依赖

```shell
$ pip install -r requirements.txt
```



## 开始使用

### 数据预处理

```shell
$ python datapreprocess.py
```

可修改参数:

```
# datapreprocess.py
corpus_file = 'clean_chat_corpus/qingyun.tsv' #未处理的对话数据集
max_voc_length = 10000 #字典最大长度
min_word_appear = 10 #加入字典的词的词频最小值
max_sentence_length = 50 #最大句子长度
save_path = 'corpus.pth' #已处理的对话数据集保存路径
```

### 使用

```shell
$ python main.py chat 
```

### 服务器
```shell script
$ python serve.py
```

* 退出聊天：输入`exit`, `quit`, `q`  均可

### 其他可配置参数

在`config.py` 文件中说明


### 训练
```
$ python train_eval.py train
```
