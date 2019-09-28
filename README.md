## 简介
基于Opennmt-tf 训练的端到端闲聊机器人，opennmt-tf 是一个非常灵活的框架，支持市面上主流的各种S2S模型，而且集成了非常好的部署支持，非常适合小公司快速敏捷开发

安装依赖
```
pip3 install -r requirements.txt
```

## 数据
数据来源于 [开源项目](https://github.com/codemayq/chinese_chatbot_corpus) 包含豆瓣，小黄鸡，微博，贴吧，字幕等问答对

本次使用了青云，豆瓣，小黄鸡的数据，可根据线上效果酌情增加或删除数据，当然数据对于最后对话系统的表现至关重要，远超于模型

### 生成训练数据

```
unzip clean_chat_corpus.zip
python3 data_preprocess.py
```

## 训练
```
bash train.sh
```

## 部署，启动服务
这次demo code使用了 python 实现了一个简单的server，运行脚本即可启动服务，如果有gpu服务器，可以直接使用docker启动GPU 的tf服务方式，[参考链接](https://github.com/OpenNMT/OpenNMT-tf/tree/master/examples/serving) 会有更好的性能

```
bash serving.sh
```

## 参考链接
[opennmt-tf](http://opennmt.net/OpenNMT-tf/quickstart.html)


