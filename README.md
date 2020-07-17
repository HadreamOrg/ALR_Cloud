# 自学习AI机器人-Hadream-云端(ALR_Cloud)

## 简介-Introduction
- 「自学习AI机器人-Hadream」是以能『自我学习』『自我意识』为目标的机器人项目。
- 为了能够使用不只一台设备进行测试，从而具备更强的信息获取能力，并且为了降低运算成本，本机器人采用『统一大脑』。
  - 即Hadream的记忆与思考在一台拥有强大运算能力的计算机上进行。
  - 而『设备端』则通过网络方式连接，将所感所知传递到『大脑』，『大脑』再根据这些信息作出学习和反应。
- 本项目为『云端』代码
  - 要查看『设备端』代码，请前往![ALR_Client](https://github.com/AutoLearningRobotHadream/ALR_Client)

## 开发者-Developers
- Lan_zhijiang
- FFXW
- Leo_Han

## 基本信息-BasicInformation
- 语言：
  - Python3
  - C++
- IDE：
  - JetBrains-Pycharm社区版(我好穷)

### 结构设计-Structure
![ALR_Cloud结构设计图](https://github.com/AutoLearningRobotHadream/ALR_Cloud/blob/master/ALR_Cloud.png)

### 设计说明-DesignDescrpition

- 主系统-main_system
  - 顾名思义，本系统是管理整个云端功能的部分。
  - 它负责将其它部分连接起来，从而使ALR具备智能。

- 逻辑思考系统-logical_thinking_system
  - 通过建立逻辑关系模型，从而达到思考的效果。
  - 对从周围环境获取到的数据/自己做出的行为及得到的反响中找出逻辑关系，然后再经过神经网络建立模型

- 语言系统-language_system
  - 分为声音和文字两部分
    - 而声音又分为听和说两部分
    - 且文字又分为读与写两部分
  - 这个系统的目的就是使ALR能够学习任何语言

- 分类系统-classification_system
  - 本系统负责对收集到的数据进行分类和识别，对原始数据做出初步的理解。
  - 而本系统又由简单分类器(simple_classifier)与复杂分类器(complex_classifier)组成
  - 简单分类器是对数据的初步认识，判断数据表达的内容类型。
    - 如分类一张图片上记录了什么，是某种动物亦或是文字
  - 而复杂分类器就是在简单分类的基础上，再对被分类对象添加详细的属性。
    - 如简单分类器分类了一张图片为猫，则复杂分类器将识别这是什么样的猫，譬如品种，状态，毛色等等。
  - 分类器是需要自行学习的，要从一开始什么都没有的情况下，不断优化自身网络，不断积累知识。
    - 要达到这个目的，最直接的就是由某个人告诉它这是什么
    - 举个例子：在设备端的摄像头前，有一个苹果，但分类器不知道这是什么，从而对设备端要求更多信息，也就是收集周围的语音。如果收集到的语音里有人说这是「苹果」，那么通过语言系统的识别，分类器就能学习到「哦！原来这是苹果啊」，并且优化自身模型，积累知识。

- 网络沟通器-network_communicator
  - 专门负责连接管理和与设备端通信，所以分为「连接管理器」和「处理器」两大部分。
  - 「连接管理器」管理着http和socket服务器以及WIFI/蓝牙连接
  - 「处理器」负责对从各种连接方式获得的信息进行处理，作出响应。但不仅是处理获得的信息，还包括发送信息的能力。
  
- 记忆系统-memory_system
  - 记忆系统是ALR积累学习成果的地方，同时对ALR的人格和对话有莫大的影响。
  - 本系统通过对事件(event)的整理，从中提炼知识(knowledge)和行为，再寻找它们间的关系，最后建立模型，改进人格和技能等等。
  - 因为需要整理事件之间或其中的关系，逻辑思考系统是最为重要的，但其它系统也都一个不能少。
  - 但最后，说到底本系统输出的也不过是加工理解过后的数据
  
- 人格系统-personality_system
  - 负责建造并记录自身人格的系统
  - 在每一个行为中混入人格的影响，再观察反响并优化，这就是人格系统自学习的方式之一。同时，从记忆系统输出的信息中改善人格也是必须的。
  - 人格系统的目的在于使行为变得富有个性，不再是单纯的行为，而是有特点的行为。

## 更新日志-UpdateLog
- 2020.6.26
  - 创建项目
  - 添加README
- 2020.7.13
  - 添加ALR_Cloud结构设计思维导图
  - 更新文件架构
- 2020.7.14
  - 更新ALR_Cloud结构设计
- 2020.7.16
  - 更新设计思想
- 2020.7.18
  - 更新设计思想
