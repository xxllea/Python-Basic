# Python

### 1 计算思维

##### 1）本质

- 抽象（Abstraction）
- 自动化（Automation）

##### 2）编程是一个求解问题的过程

1. 分析问题-抽象内容之间的交互关系
2. 设计利用计算机求解问题的确定性方法
3. 编写调试代码以解决问题

##### 3）扩展-三种基本思维

- 以实验和验证为特征的实证思维， 以物理学科为代表
- 以推理和演绎为特征的逻辑思维，以数学学科为代表
- 以设计和构造为特征的计算思维，以计算机学科为代表



### 2 程序设计方法

##### 1）基本编程方法

- 输入
- 处理
- 输出

##### 2）自顶向下设计

​	**每层设计中，参数和返回值如何设计是重点，其他细节可以暂时忽略**

- 步骤1：将算法表达为一系列小问题
- 步骤2：为每个小问题设计接口
- 步骤3：通过将算法表达为接口关联的多个小问题来细化算法
- 步骤4：为每个小问题重复上述过程

##### 3）自底向上执行

- 开展测试的更好办法也是将程序分成小部分逐个测试
- 执行中等规模程序的最好方法是从结构图最底层开始，而不是从顶部开始，然后逐步上升
- 或者说，先运行和测试每一个基本函数，再测试由基础函数组成的整体函数，这样有助于定位错误

##### 4）总结

- 通过模块化设计可以分解问题使编写复杂程序成为可能，通过单元测试方法分解问题使运行和调试复杂程序成为可能
- 自顶向下和自底向上贯穿程序设计和执行的整个过程



### 3 Python计算生态

##### 1）Python标准库

- 有一部分Python计算生态随Python安装包一起 发布，用户可以随时使用，被称为Python标准库
- 受限于Python安装包的设定大小，标准库数量 270个左右

##### 2）Python第三方库

###### **①概述**

- 更广泛的Python计算生态采用额外安装方式服务用户，被称为Python第三方库
- 这些第三方库由全球各行业专家、工程师和爱好者开发，没有顶层设计，由开发者采用“尽力而为”的方式维护

###### **②获取与安装**

1. `pip工具安装`

   - pip是Python官方提供并维护的在线第三方库安装工具

   ![img](https://mubu.com/document_image/2640d073-c368-46b5-994a-6a35fd922b25-5974427.jpg)

   - pip是Python第三方库最主要的安装方式，可以安装超过90%以上的第三方库。然而，还有一些第三方库无法暂时用pip安装，此时，需要其他的安装方法

   - pip工具与操作系统也有关系，在MacOS X和Linux等操作系统中，pip工具几乎可以安装任何Python第三方库， 在Windows操作系统中，有一些第三方库仍然需要用其他方式尝试安装

2. `自定义安装`

   - 自定义安装指按照第三方库提供的步骤和方式安装。第三方库都有主页用于维护库的代码和文档

3. `文件安装`

   - 为了解决这类第三方库安装问题，美国加州大学尔湾分校提供了一个页面，帮助Python用户获得Windows可直接安装的第三方库文件

   - 链接地址如下：http://www.lfd.uci.edu/~gohlke/pythonlibs/

   - 这里以scipy为例说明，首先在上述页面中找到scipy库对应的内容。选择其中的.whl文件下载，这里选择适用于Python3.5版本解释器和32位系统的对应文件：scipy- 0.17.1 - cp35 -cp35m-win32 .whl，下载该文件到 D:\pycodes目录

   - 然后，采用pip命令安装该文件

     ![img](https://mubu.com/document_image/aaf8c5ad-44f2-4504-a966-17e0b7eda764-5974427.jpg)

###### 	③pyinstaller库

- PyInstaller是一个十分有用的Python第三方库

- 它能够在Windows、Linux、Mac OS X等操作系统下将Python 源文件打包，变成直接可运行的可执行文件

- 通过对源文件打包，Python程序可以在没有安装Python 的环境中运行，也可以作为一个独立文件方便传递和管理

- 使用PyInstaller库对Python源文件打包十分简单， 使用方法如下：

  ![img](https://mubu.com/document_image/c3649dac-390b-4aeb-86b0-f4a93b3121b8-5974427.jpg)

- 执行完毕后，源文件所在目录将生成dist和build 两个文件夹。最终的打包程序在dist内部与源文件同名的目录中

- 可以通过-F参数对Python源文件生成一个独立的 可执行文件

  ![img](https://mubu.com/document_image/dd63e3b3-0dd3-4a8a-b349-496fba8ef119-5974427.jpg)

- 执行后在dist目录中出现了SnowView.exe文件， 没有任何依赖库，执行它即可显示雪景效果

- PyInstaller有一些常用参数

  ![img](https://mubu.com/document_image/c3f18c2c-b355-46e8-8843-7cb404155160-5974427.jpg)

###### 	④jieba库

1. `概述`

   - 由于中文文本中的单词不是通过空格或者标点符号分割，中文及类似语言存在一个重要的“分词” 问题
   - jieba（“结巴”）是Python中一个重要的第三方中文分词函数库
   - jieba库的分词原理是利用一个中文词库，将待分词的内容与分词词库进行比对，通过图结构和动 态规划方法找到最大概率的词组
   - 除了分词， jieba还提供增加自定义中文单词的功能

2. `分词模式`

   1. 精确模式

      - 将句子最精确地切开，适合文本分析

      - jieba.lcut(s)是最常用的中文分词函数，用于精准模式，即将字符串分割成等量的中文词组，返回结果是列表类型

        ![img](https://mubu.com/document_image/22d83a93-fcee-4b3e-ab30-13f8257aca47-5974427.jpg)

   2. 全模式

      - 把句子中所有可以成词的词语都扫描出来，速度非常快， 但是不能解决歧义

      - jieba.lcut(s, cut_all = True)用于全模式，即将字符串的所有分词可能均列出来，返回结果是列表类型，冗余性最大

        ![img](https://mubu.com/document_image/f95b9b31-4e20-4400-9908-e03472c99599-5974427.jpg)

   3. 搜索引擎模式

      - 在精确模式基础上，对长词再次切分，提高召回率，适合用于搜索引擎分词

      - jieba.lcut_for_search(s)返回搜索引擎模式，该模式首先执行精确模式，然后再对其中长词进一 步切分获得最终结果

        ![img](https://mubu.com/document_image/1a6a7909-0a82-4702-9a4f-179f7a2bae4e-5974427.jpg)

   4. 附加

      - jieba.add_word()函数，顾名思义，用来向jieba 词库增加新的单词![img](https://mubu.com/document_image/ad416773-3abc-4450-bd6e-d5ae9590cf31-5974427.jpg)

##### 3）基本内置函数

- Python解释器提供了68个内置函数（下面介绍32个）

- 

  ![img](https://mubu.com/document_image/be8f39d0-1d38-474b-9476-eb152f3b02b9-5974427.jpg)

- 

  ![img](https://mubu.com/document_image/63647a67-267a-4ed7-8561-fd76f46485ae-5974427.jpg)

- 

  ![img](https://mubu.com/document_image/aaf64211-aef6-4650-a1e7-5994e00fd87b-5974427.jpg)



### 4 语言属性及特征

##### 1）胶水语言

- 由于Python有非常简单灵活的编程方式，很多采用C、C++等语言编写的专业库可以经过简单的接口封装供Python语言程序调用
- 这样的粘性功能使得Python语言成为了各类编程语言之间的接口，Python语言也被称为“胶水语言”

##### 2）编程语言（按执行机制分）

1. `静态语言`
   - 编译执行：Java\C
   - 编译器
     - 将源代码一次性、全部转换成目标代码的程序
     - 一旦程序被编译，不再需要编译器或者源代码
   - 特点
     - 目标代码对于相同源代码执行速度更快
     - 目标代码只能在同类型操作系统灵活使用
2. `脚本语言`
   - 解释执行：Python\JavaScript\PHP
   - 解释器
     - 将源代码逐行转换成目标代码的程序
     - 每次执行程序都需要源代码和解释器
   - 特点
     - 程序纠错、维护方便
     - 可移植性好

##### 3）语言特点

- 通用性
- 语法简洁
- 生态高产
- 平台无关
- 强制可读
- 支持中文



### 5 Python语法元素

##### 1）程序格式框架

###### ①缩进

- 表达代码之间的包含和层次关系
- 1个缩进=4个空格

###### ②注释

- 代码说明，会被编译器或解释器省去
- 单行、多行都可用#
- 多行注释（块注释）用一对 连续的三个 引号(单引号和双引号都可以)

##### 2）语法元素

###### ①变量

- 保存和表示数据值的一种语法元素，可通过赋值方式修改
- ![img](https://mubu.com/document_image/65981fa4-d528-491a-955d-b6d8b52bae96-5974427.jpg)

###### ②标识符命名

- 用A-Za-z0-9_组合命名，大小写敏感
- 首字母不能为数字，中间不能有空格，长度无限制
- 不能用关键字命名

###### ③关键字（保留字）

- 编程语言内部定义并保留的标识符

##### 3）语句元素

###### ①表达式

- 产生或计算新数据值的代码片段
- 一般由数据和操作符等构成

###### ②赋值

- <变量> = <表达式>
- <变量1>, …, <变量N> = <表达式1>, …, <表达式N>

###### ③引用

- import <功能库名称>
- 用<功能库名称>.<函数名称>()调用具体功能![img](https://mubu.com/document_image/b19b3b6c-138b-4d06-a143-450452e0d0de-5974427.jpg)

##### 4）基本输入输出函数

###### ①Input()

- <变量> = input(<提示性文字>)

- 

  ![img](https://mubu.com/document_image/8a64d8c7-defc-48bc-a45c-b1494cb526f9-5974427.jpg)

###### ②eval()

- 能够以Python表达式的方式解析并执行字符串，将返回结果输出

  ![img](https://mubu.com/document_image/2ac8d605-259d-4031-84e5-e106aa72395c-5974427.jpg)

- 经常和input()函数一起使用，用来获取用 户输入的数字

  ![img](https://mubu.com/document_image/5ea07d62-6559-4022-a233-afda77483089-5974427.jpg)

###### ③print()

- ①仅用于输出字符串

  ![img](https://mubu.com/document_image/92d0c6e6-b5f3-4d3b-93a4-324eeabf211f-5974427.jpg)

- ②仅用于输出一个或多个变量

  ![img](https://mubu.com/document_image/5264116d-ac77-450c-b04c-74d1a32a5333-5974427.jpg)

- ③用于混合输出字符串与变量值

  ![img](https://mubu.com/document_image/af22b394-fe32-4f0b-ad3d-b11b7783df04-5974427.jpg)

- 对print()函数的end参数进行赋值

  ![img](https://mubu.com/document_image/744916e4-3feb-4ef5-b3cc-ff2e70b039a9-5974427.jpg)

### 6 Python数据类型

##### 1）基本数据类型

###### ①整数类型（int）

- 不同进制的整数之间可以直接运算

- 表示方式（常用）

  - 十进制（默认）：1010
  - 二进制：0b1010，0B1010
  - 八进制：0o1762，0O762
  - 十六进制：0x3F2，0X3F2

- 整数类型运算

  - 数值运算操作符

    - Python提供了9个基本的数值运算操作符

      ![img](https://mubu.com/document_image/45e4b72e-c994-405c-9200-b09fcc7a499a-5974427.jpg)

    - 增强赋值操作符（由二元运算操作符与等号组成）

      ![img](https://mubu.com/document_image/c93258ff-2152-4965-afaf-bcc8b9dff911-5974427.jpg)

    - 基本规则

      ![img](https://mubu.com/document_image/2ba40b86-3866-41c5-895e-1e672fe0824a-5974427.jpg)

  - 数值运算函数

    ![img](https://mubu.com/document_image/9eed00cd-fd1c-45d6-a6c3-e465ba0e216c-5974427.jpg)

###### ②浮点数（float）

- 表示方式

  - 一般形式：123.456

  - 科学计数法：1.23456e2

    ![img](https://mubu.com/document_image/d62e7e80-4a4f-4cd4-954e-46806427469a-5974427.jpg)

###### ③复数（complex）

- Python语言中，复数可以看作是二元有序实数对（a, b）

- 表示方式

  - a+bj：10 + 10j

- 用 z.real和z.imag分别获得它的实数部分和虚数部分

  ![img](https://mubu.com/document_image/a1d1eaa1-864e-40eb-b650-5d7c0296c5ee-5974427.jpg)

###### ④布尔型（bool）

- 真 True 非 0 数 —— 非零即真
- 假 False 0

###### ⑤字符串类型（str）

1. `表示`

   用两个双引号" "或者单引号' '括起来的一个或多个字符

2. `转义字符`

   - \n表示换行
   - \\\\表示反斜杠
   - \\'表示单引 号
   - \\"表示双引号
   - \t表示制表符（TAB）

3. `两种符号体系`

   - 
     ![img](https://mubu.com/document_image/84d2d30d-bf92-40c9-9a06-f4e9509559e8-5974427.jpg)

   - 

     ![img](https://mubu.com/document_image/1b8dde03-79d3-4798-9808-5c898d91f195-5974427.jpg)

4. `字符串索引`

   - <字符串或字符串变量>[序号]

     ![img](https://mubu.com/document_image/cd1d64a8-22eb-4257-9840-c4841f4bf4cf-5974427.jpg)

5. `字符串切片`

   - 采用[N: M]格式获取字符串的子串

     ![img](https://mubu.com/document_image/5aa92844-7a4d-4259-bce9-e58265dbaec7-5974427.jpg)

6. `格式化字符串`

   - q%格式化

     - % 被称为格式化操作符，专门用于处理字符串中的格式

       - 包含 % 的字符串，被称为格式化字符串
       - % 和不同的字符连用，不同类型的数据需要使用不同的格式化字符

     - 格式化字符

       ![img](https://mubu.com/document_image/1580d0d8-097f-41ed-bd32-b3d17683e991-5974427.jpg)

     - 语法格式

       - 

         ![img](https://mubu.com/document_image/8a89bd01-a955-460d-89a9-6b418e105e73-5974427.jpg)

       - 

         ![img](https://mubu.com/document_image/7ddbc6e0-0f05-4058-a92a-a9b1f6d6c0b0-5974427.jpg)

   - format格式化

     - <模板字符串>.format(<逗号分隔的参数>)

       ![img](https://mubu.com/document_image/73e1a366-0382-4db6-9dbd-939501d04812-5974427.jpg)

     - 可以通过format()参数的序号在模板字符串槽中 指定参数的使用，参数从0开始编号

       ![img](https://mubu.com/document_image/c68ad222-6dcb-4e65-a12c-df9e89931eb6-5974427.jpg)

     - format()方法中模板字符串的槽除了包括参数序号，还可以包括格式控制信息

       - {<参数序号>: <格式控制标记>}

         ![img](https://mubu.com/document_image/1424517c-1cdb-4042-bebe-7d7b9fefdba9-5974427.jpg)

       - 

         ![img](https://mubu.com/document_image/777882ed-f1b0-40bb-95c4-cbb2ee4450ce-5974427.jpg)

7. `获取字符串长度`

   - len()

   - 

     ![img](https://mubu.com/document_image/8758f464-a3b0-46d3-baf9-868e532c6da8-5974427.jpg)

##### 2）组合数据类型

###### ①集合类型

- 一个具体的数据类型名称
- 集合类型是一个元素集合，元素之间无序，相同元素在集合中唯一存在

1. `概述`

   - 即包含0个或多个数据项的无序组合

     ![img](https://mubu.com/document_image/80d928df-ac4e-4578-8f37-4ed8725b7cd9-5974427.jpg)

   - 集合是无序组合，用大括号（{}）表示，它没有索引和位置的概念，集合中元素可以动态增加或删除

   - 集合中元素不可重复，元素类型只能是固定数据类型， 例如：整数、浮点数、字符串、元组等，使用集合类型能够过滤掉重复元素

   - 列表、字典和集合类型本身都是可变数据类型，不能作为集合的元素出现

   - 集合的打印效果与定义顺序可以不一致

2. `作用`

   - 主要用于元素去重，适合于任何组合数据类型

     ![img](https://mubu.com/document_image/a8810f7f-4dcd-4f9c-a668-8fca1a2c844c-5974427.jpg)

3. `操作符`

   - 有4个操作符，交集（&）、并集（|）、差集 （-）、补集（^）

     ![img](https://mubu.com/document_image/a71fcfdd-34cd-429b-be97-f5e1f610e2a6-5974427.jpg)

   - 实例

     ![img](https://mubu.com/document_image/dbdb4e7f-0d81-4b3c-b259-493cbaf7dd7a-5974427.jpg)

4. `函数或方法`

   ![img](https://mubu.com/document_image/7bcf3dde-0749-4d9f-9114-f3cc7732381f-5974427.jpg)

###### ②序列类型

1. `概念`

   - 是一类数据类型的总称
   - 序列类型是一维元素向量，元素之间存在先后关系，通过序号访问，元素之间不排他
   - 序列类型使用相同的索引体系，即正向递增序号和反向递减序号

2. `通用操作符和函数`

   - 概述

   ![img](https://mubu.com/document_image/6c2e85be-4846-49da-b0ef-c477af2aa578-5974427.jpg)

3. `典型代表`

   - 元组类型（ ）

   - 字符串类型" "或' '

   - 列表类型[ ]

     **①定义**

     - 列表是一个十分灵活的数据结构，它具有处理任意长度、 混合类型的能力，并提供了丰富的基础操作符和方法
     - 列表类型支持序列类型对应的操作，列表没有长度限制，元素类型可以不同，不需要预定义长度
     - 当程序需要使用组合数据类型管理批量数据时，请尽量使用列表类型

     **②表示方式**

     - 列表类型用中括号（[]）表示，也可以通过list(x) 函数将集合或字符串类型转换成列表类型

       ![img](https://mubu.com/document_image/ee802e2a-42a3-490a-9ca9-a681b4f39163-5974427.jpg)

     ③**索引**

     - 索引是列表的基本操作，用于获得列表的一个元 素。使用中括号作为索引操作符

       ![img](https://mubu.com/document_image/b6e19d2c-30f2-4b3d-adf1-079ac3cd1998-5974427.jpg)

     ④**切片**

     - ①<列表或列表变量>[N：M]

       ![img](https://mubu.com/document_image/c5db2922-8233-4f03-8058-71ce62b40cd1-5974427.jpg)

     - ②列表或列表变量>[N：M：K]

       ![img](https://mubu.com/document_image/5d0c6ff9-e9d7-4bc9-bdae-07feb0f40d95-5974427.jpg)

     ⑤**操作函数**

     - 概述

       ![img](https://mubu.com/document_image/43ad1806-720f-4c06-90a6-2e5714fe7b92-5974427.jpg)

     ⑥**操作方法**

     - 概述

       ![img](https://mubu.com/document_image/b50cd520-637f-4652-bb72-ffd10e80f491-5974427.jpg)

     - ls.append(x)在列表ls最后增加一个元素x

       ![img](https://mubu.com/document_image/c425e304-642d-4ed3-9b49-6ba51089e8cd-5974427.jpg)

     - 如果希望增加多个元素，可以使用加号，将两个列表合并

       ![img](https://mubu.com/document_image/45682f9f-9cf7-4643-884b-b59430ac5de6-5974427.jpg)

     - ls.insert(i, x)在列表ls中序号i位置上增加元素x，序号i之 后的元素序号依次增加

       ![img](https://mubu.com/document_image/7f614449-51e9-451d-9fdc-ede5a643afa6-5974427.jpg)

     - ls.clear()将列表ls的所有元素删除，清空列表

       ![img](https://mubu.com/document_image/68fde3e2-18a5-41b2-af14-6eaf4a13d63a-5974427.jpg)

     - ls.pop(i)将返回列表ls中第i位元素，并将该元素从列表中删除

       ![img](https://mubu.com/document_image/780aacd7-e0b4-4643-81f3-1d1bd7541f74-5974427.jpg)

     - ls.remove(x)将删除列表ls中第一个出现的x元素

       ![img](https://mubu.com/document_image/4003396e-c5b5-4b16-a464-50b7c64be80a-5974427.jpg)

     - 用Python保留字del对列表元素或片段进行删除

       ![img](https://mubu.com/document_image/217649d6-a0b3-4975-950c-d6ea11c4c8c7-5974427.jpg)

     - ls.reverse()将列表ls中元素进行逆序反转

       ![img](https://mubu.com/document_image/5516c377-55a3-400c-bfb2-39e0beb822ca-5974427.jpg)

     - ls.copy() 复制ls中所有元素生成一个新列表，由下例看出，一个列表lt使用.copy()方法复制后赋值给变量ls，将lt元素清空不影响新生成的变量ls

       ![img](https://mubu.com/document_image/dbd338d5-b74b-4fdd-88b3-579dd7f27d57-5974427.jpg)

     - 使用索引配合等号（=）可以对列表元素进行修改

       ![img](https://mubu.com/document_image/0cb1dc42-3796-4df0-b2b1-5ca43622c4ac-5974427.jpg)

     ⑦**遍历循环**

     - 

       ![img](https://mubu.com/document_image/fc3c45c3-4cf0-48f9-a324-16a9199d940b-5974427.jpg)

     ⑧**注意事项**

     - 对于基本的数据类型，如整数或字符串，可以通过等号实现元素赋值；但对于列表类型，使用等号无法实现真正的赋值

     - 其中，ls = lt语句并不是拷贝lt中元素给变量ls，而是新关联了一个引用，即ls和lt所指向的是同一套内容

       ![img](https://mubu.com/document_image/2519be70-1e1f-4e95-9fb8-9c0eabc00362-5974427.jpg)

###### ③映射类型

1. `概念`

   - 是一类数据类型的总称

   - “键-值”数据项的组合，每个元素是一个键值对，表示为(key, value)，元素之间是无序的，

   - 键值对是一种二元关系，源于属性和值的映射关系

     ![img](https://mubu.com/document_image/7e7894e2-597c-4d03-9e0a-84691d0e12bb-5974427.jpg)

   - 映射类型的典型代表是字典类型

   - 映射类型是序列类型的一种扩展，序列类型中，采用 从0开始的正向递增序号进行具体元素值的索引，而映射类型则由用户来定义序号，即键，用其去索引具体的值

   - 键（key）表示一个属性，也可以理解为一个类别或项目， 值（value）是属性的内容

   - 键值对将映射关系结构化，用于存储和表达

2. `字典（dict）`

   ①**定义**

   - 字典类型也具有和集合类似的性质，即键值对之间没有顺序且不能重复

   - 表示方式

     ![img](https://mubu.com/document_image/74f62442-4e3b-470a-99ac-c8f086ae49ad-5974427.jpg)

     ![img](https://mubu.com/document_image/ad4e35fe-dbba-4a7f-9fb6-0de54e22221e-5974427.jpg)

   ②**索引**

   - 

     ![img](https://mubu.com/document_image/fda99423-0089-44c4-a4b5-3fae105d550a-5974427.jpg)

   - 利用索引和赋值（=）配合，可以对字典中每个元素进行修改

     ![img](https://mubu.com/document_image/5c60c5ac-3785-4b98-b284-7b3aa27d5ac1-5974427.jpg)

   - 使用大括号可以创建字典。通过索引和赋值配合，可以向字典中增加元素

     ![img](https://mubu.com/document_image/adf70380-a09c-4906-8ab4-5754201c9de8-5974427.jpg)

   ③**操作函数**

   - 概述

     ![img](https://mubu.com/document_image/59cbb0a6-0744-4897-a600-db496e04b33d-5974427.jpg)

   - len(d)给出字典d的元素个数，也称为长度

     ![img](https://mubu.com/document_image/bca22eb6-3b00-459e-b105-39b6ca548421-5974427.jpg)

   - min(d)和max(d)分别返回字典d中最小或最大索引值

     ![img](https://mubu.com/document_image/ddae31c6-ef97-48f7-92b0-432419499205-5974427.jpg)

   - dict()函数用于生成一个空字典，作用和{}一致

     ![img](https://mubu.com/document_image/dbadf905-b4dc-4401-9f5f-1454ea2f7812-5974427.jpg)

   ④**操作方法**

   - 概述

     ![img](https://mubu.com/document_image/862699be-dc19-4d0e-af6d-df86b9fa6090-5974427.jpg)

   - d.keys()返回字典中的所有键信息，返回结果是Python 的一种内部数据类型dict_keys，专用于表示字典的键。如果希望更好的使用返回结果，可以将其转换为列表类 型

     ![img](https://mubu.com/document_image/fb853e7e-ac03-456d-8d12-a043e7a6395c-5974427.jpg)

   - d.values()返回字典中的所有值信息，返回结果是Python 的一种内部数据类型dict_values。如果希望更好的使用返回结果，可以将其转换为列表类型

     ![img](https://mubu.com/document_image/8e5481b3-93cf-430b-b2b8-f4d726010497-5974427.jpg)

   - d.items()返回字典中的所有键值对信息，返回结果是 Python的一种内部数据类型dict_items

     ![img](https://mubu.com/document_image/caabaf63-5a47-4ef3-9157-a59f86e59a9d-5974427.jpg)

   - d.get(key, default)根据键信息查找并返回值信息，如果 key存在则返回相应值，否则返回默认值，第二个元素 default可以省略，如果省略则默认值为空

     ![img](https://mubu.com/document_image/3e2df0d5-5565-4d2e-a42f-984d3706ebac-5974427.jpg)

   - d.pop(key, default)根据键信息查找并取出值信息，如果 key存在则返回相应值，否则返回默认值，第二个元素 default可以省略，如果省略则默认值为空

     ![img](https://mubu.com/document_image/8782075f-b4bf-4928-b68f-21e6f26676c9-5974427.jpg)

   - d.popitem()随机从字典中取出一个键值对，以元组(key, value)形式返回。取出后从字典中删除这个键值对

     ![img](https://mubu.com/document_image/36f0e8c9-ea35-44b4-8e11-6151360e0958-5974427.jpg)

   - d.clear()删除字典中所有键值对

     ![img](https://mubu.com/document_image/1ebd046b-1325-4ecc-afee-4987dafdb46e-5974427.jpg)

   - 如果希望删除字典中某一个元素，可以使用 Python保留字del

     ![img](https://mubu.com/document_image/4ab48013-0e2b-46f6-bab3-4a94cc8d7ce8-5974427.jpg)

   - 字典类型也支持保留字in，用来判断一个键是否在字典中。如果在则返回True，否则返回False

     ![img](https://mubu.com/document_image/79a10806-3c70-40ef-8b65-7936b9ad7f1a-5974427.jpg)

   ⑤**遍历循环**

   - 基本语法

     ![img](https://mubu.com/document_image/0bf7af46-444b-4850-9c2c-9f8903669ed9-5974427.jpg)

   - for循环返回的变量名是字典的索引值。如果需要获得键对应的值，可以在语句块中通过get()方法获得

     ![img](https://mubu.com/document_image/b15308b1-2e41-409b-a6ff-0d3556693c1e-5974427.jpg)

   

### 7 Python程序控制结构

##### 1）顺序结构

 略

##### 2）分支结构

###### 概述

- 作用：根据判断条件选择程序执行路径

- 判断条件及组合

  1. 关系运算符

     - 

       ![img](https://mubu.com/document_image/bab1a522-b4b4-4982-aa22-e58095cd99c5-5974427.jpg)

     - Python语言中，任何非零的数值、非空的数据类型都 等价于True，0或空类型等价于False，可以直接用作判 断条件

  2. 逻辑运算符

     - not、and和or

     ![img](https://mubu.com/document_image/bb296c1f-68ac-4f61-b020-28f28510c8db-5974427.jpg)

###### ①单分支

- 表示方式

  ![img](https://mubu.com/document_image/2f2d3e23-68f8-401e-86a8-4050bb163e0e-5974427.jpg)

###### ②二分支

- 表示方式

  ![img](https://mubu.com/document_image/8972ad7f-4c35-49cb-a6e6-cd3b359adb7e-5974427.jpg)

- 

  ![img](https://mubu.com/document_image/39ca4fe0-e838-4a99-9412-bea68d1cd739-5974427.jpg)

- 可简洁表达为

  ![img](https://mubu.com/document_image/add2c908-f808-4414-825f-b66d5f3086a7-5974427.jpg)

###### ③多分支

- 表示方式

![img](https://mubu.com/document_image/fe2a4259-9c74-4a1b-944a-91b855643681-5974427.jpg)

##### 3）循环结构

- 作用：根据判断条件确定一段程序是否再次执行一次或者多次

###### ①遍历循环

- 用保留字for依次提取遍历结构各元素进行处理

- 表示方式

  - 

    ![img](https://mubu.com/document_image/14254b14-615f-4761-b9af-547c2ac9cda3-5974427.jpg)

  - 使用range()函数，可以指定语句块的循环次数

    ![img](https://mubu.com/document_image/87a08183-1e20-42ca-a2d6-24d472a30709-5974427.jpg)

  - 扩展模式

    ![img](https://mubu.com/document_image/21e7f02a-e78f-4057-a5df-bfc8950acaa2-5974427.jpg)

###### ②条件循环

- 用保留字while根据判断条件执行程序

- 表示方式

  - 

    ![img](https://mubu.com/document_image/bf3d29db-eb45-478a-b772-840e94533e06-5974427.jpg)

  - 扩展模式

    ![img](https://mubu.com/document_image/61c54b70-e84a-4327-81b6-83e464f08a2a-5974427.jpg)

- 循环控制

  - continue

    - continue语句只结束本次循环，不终止整个循环的执行

    - 

      ![img](https://mubu.com/document_image/030ae6ad-5a50-4d87-8100-ecfc7b7d89e9-5974427.jpg)

  - break

    - break用来跳出最内层for或while循环，脱离该循环后程序从循环后代码继续执行

      ![img](https://mubu.com/document_image/51bb8c73-de7e-42fb-b561-8559887d7b48-5974427.jpg)

##### 4）扩展结构

###### try-except

![img](https://mubu.com/document_image/88b5504b-4552-40a7-865e-c7ef9fb49816-5974427.jpg)



### 8 Python函数与代码复用

##### 1）函数定义

###### ①概念

- 函数是一段具有特定功能的、可重用的语句组，通过函数名来表示和调用
- 函数的使用包括两部分：函数的定义和函数的使用
- 函数是一种功能抽象

###### ②包含

- 用def保留字，return语句可选

  ![img](https://mubu.com/document_image/56323b32-ae9f-4e0c-9547-3b11b646190f-5974427.jpg)

- 例子

  ![img](https://mubu.com/document_image/74278db7-6e3d-4279-933b-4d904a58fa6f-5974427.jpg)

- 函数名

  - 可以是任何有效的Python标识符

- 参数列表

  - 即是调用该函数时传递给它的值
  - 参数可以有零个、 一个或多个
  - 多参数由逗号分隔，无参数时也要保留圆括号

- 函数体

  - 即函数每次被调用时执行的代码，由一行或多行语句组成。

##### 2）函数调用

- 定义后的函数不能直接运行，需要经过“调用” 才能运行

- 

  ![img](https://mubu.com/document_image/aeacb2c0-3c31-49f8-99f2-27c58e1e0a53-5974427.jpg)

##### 3）参数传递

###### ①可选参数

- 参数定义时可指定默认值，当函数调用时，若没有传入对应的参数值，则使用默认值替代

  ![img](https://mubu.com/document_image/a7ded677-6515-4670-a777-6c260e9e330f-5974427.jpg)

- 可选参数一般都放置在非可选参数的后面

  ![img](https://mubu.com/document_image/9d249c90-7d75-4fa1-ae7a-e6e3bb9bc19e-5974427.jpg)

###### ②参数名称

- Python语言同时支持函数按照参数名称方式传递参数

  ![img](https://mubu.com/document_image/1b437deb-da8c-4e88-8f44-a8f4633d329a-5974427.jpg)

###### ③返回值

- return语句用来结束函数并将程序返回到函数被调用的位置继续执行

- return可将0个、1个或多个函数运算的结果返回给函数被调用处的变量

- 函数可以没有return，此时函数并不返回值

- 当函数使用return返回多个值，可以使用一个变量或多个变量保存结果

  ![img](https://mubu.com/document_image/4ff811ed-d379-4bd0-bf53-02a9bac81eee-5974427.jpg)

##### 4）变量作用域

###### ①局部变量

- 指在函数内部使用的变量，仅在函数内部有效，当函数退出时变量将不再存在

![img](https://mubu.com/document_image/0e26a62b-cdb6-4904-924c-d60cf995ed61-5974427.jpg)

###### ②全局变量

- 指在函数之外定义的变量，在程序执行全过程有效

- 全局变量在函数内部使用时，需要提前使用保留字global声明

  ![img](https://mubu.com/document_image/b8169f59-da45-4a3a-8f99-73f7820cecab-5974427.jpg)

##### 5）代码复用

###### ①模块化设计

- 通过函数的封装功能将程序划分成主程序、子程序和子程序间关系的表达
- 模块化设计是使用函数设计程序的思考方法，以功能块为基本单位
- 两个基本要求：功能块内部之间紧耦合、功能块之间松耦合

###### ②注意事项

- 使用函数只是模块化设计的必要非充分条件，根据计算需求合理划分函数十分重要
- 一般来说， 完成特定功能或被经常复用的一组语句应该采用函数来封装，并尽可能减少函数间参数和返回值的数量。



### 9 Python文件和数据格式化

##### 1）文件概念

- 文件是存储在辅助存储器上的一组数据序列，可以包含任何数据内容
- 概念上，文件是数据的集合和抽象

##### 2）文本类型

###### ①文本文件

- 文本文件一般由单一特定编码的字符组成，如UTF-8编码，内容容易统一展示和阅读

![img](https://mubu.com/document_image/a468ebef-62d3-4970-b8bf-8fcf51788a40-5974427.jpg)

###### ②二进制文件

- 二进制文件直接由比特0和比特1组成，文件内部数据的组织格式与文件用途有关
- 二进制是信息按照非字符但特定格式形成的文件，例如，png 格式的图片文件、avi格式的视频文件

###### ![img](https://mubu.com/document_image/ebb187b2-ba33-4113-8380-3ab7d459c42a-5974427.jpg)两者区别

- 二进制文件和文本文件最主要的区别在于是否有统一的字符编码
- 无论文件创建为文本文件或者二进制文件，都可以用 “文本文件方式”和“二进制文件方式”打开，但打开后的操作不同

##### 3）文件使用

- Python对文本文件和二进制文件采用统一的操作步骤，即“打开-操作-关闭”

![img](https://mubu.com/document_image/e9bb3a33-185c-45a0-981c-77a5d3a5f812-5974427.jpg)

###### ①文件打开

- Python通过open()函数打开一个文件，并返回一个操作这个文件的变量，打开模式使用字符串方式表示

![img](https://mubu.com/document_image/a8327af3-ea98-48ca-86bc-b5b59d831ad5-5974427.jpg)

###### ②文件关闭

- 文件使用结束后要用close()方法关闭，释放文件的使用授权

![img](https://mubu.com/document_image/d2316af2-f0e8-454e-a35f-f144ccab96fb-5974427.jpg)

###### ③文件读入

- 文件打开后，对文件的读写有一个读取指针，当从文件中读入内容后，读取指针将向前进，再次读取的内容将 从指针的新位置开始

- 根据打开方式不同，文件读写也会根据文本文件 或二进制打开方式有所不同

  ![img](https://mubu.com/document_image/de34d6b5-b7c2-42d5-a39f-4c1b770eb1fb-5974427.jpg)

- f.read()是最常用的一次性读入文件的函数，其结果是一个字符串

  ![img](https://mubu.com/document_image/f7d7ad0c-5a82-44ba-8f3c-cc6a0c5a6892-5974427.jpg)

- f.readlines()也是一次性读入文件的函数，其结果是一个列表，每个元素是文件的一行

  ![img](https://mubu.com/document_image/91cb827f-6474-4c02-a098-373866dcc5e0-5974427.jpg)

- f.seek()方法能够移动读取指针的位置，f.seek(0)将读取指针移动到文件开头，f.seek(2)将读取指针移动到文件结尾

  ![img](https://mubu.com/document_image/b8696ea3-a4ce-4b77-ba83-e2ea00bc460f-5974427.jpg)

- 从文本文件中逐行读入内容并进行处理是一个基本的文件操作需求

- 文本文件可以看成是由行组成的组合类型， 因此，可以使用遍历循环逐行遍历文件

  ![img](https://mubu.com/document_image/a15d350a-38da-4b53-b968-71165a6aeb88-5974427.jpg)

  ![img](https://mubu.com/document_image/589152e9-edc6-4180-b5bd-b4e9fcf3d12d-5974427.jpg)

###### ④文件写入

- 方法

  ![img](https://mubu.com/document_image/16897e6f-c2ae-4dc5-ac3f-d791f33dff3c-5974427.jpg)

- f.write(s)向文件写入字符串s，每次写入后，将会记录一个写入指 针。该方法可以反复调用，将在写入指针后分批写入内容，直至文件被关闭

  ![img](https://mubu.com/document_image/bef14833-8695-4d89-9931-aba907f97099-5974427.jpg)

- f.writelines(lines)直接将列表类型的各元素连接起来写入文件f

  ![img](https://mubu.com/document_image/4bf2fade-7e82-400a-9182-b130c07da3a8-5974427.jpg)

##### 4）数据维度

###### ①一维数据

- `概念`

  - 一维数据由对等关系的有序或无序数据构成，采 用线性方式组织，对应于数学中数组的概念

  - 例如：中国的直辖市列表即可表示为一维数据， 一维数据具有线性特点

    ![img](https://mubu.com/document_image/162b34df-dcf0-4dfb-9d66-573eb8a07e85-5974427.jpg)

- `表示`

  - 一维数据是最简单的数据组织类型，由于是线性结构，在Python语言中主要采用列表形式表示

  - 例如：中国的直辖市数据可以采用一个列表变量表示

    ![img](https://mubu.com/document_image/11fd1b2a-0568-4720-9a1b-60c8c4894607-5974427.jpg)

- `存储`

  - 一维数据的文件存储有多种方式，总体思路是采用特殊字符分隔各数据。
  - 常用4种存储方法
    - （1）采用空格分隔元素，例如： 北京 上海 天津 重庆
    - （2）采用逗号分隔元素，例如： 北京,上海,天津,重庆
    - （3）采用换行分隔包括，例如： 北京\n上海\n天津\n重庆
    - （4）其他特殊符号分隔，以分号分隔为例，例如：北京;上海;天津;重庆

- `处理`

  - CSV格式

    - 逗号分割的存储格式叫做CSV格式，它是一种通用的、相对简单的文件格式，在商业和科学上广泛应用，大部分编辑器 都支持直接读入或保存文件为CSV格式

    - 一维数据保存成CSV格式后，各元素采用逗号分隔，形成一行。从Python表示到数据存储，需要将列表对象输出为CSV格式以及将CSV格式读入成列表对象

    - 列表对象输出为CSV格式文件方法如下，采用字符串的join()方法最为方便

      ![img](https://mubu.com/document_image/95f105b4-d7a5-4d74-8cf5-9434ca3ef726-5974427.jpg)

    - 对一维数据进行处理首先需要从CSV格式文件读入一维数据，并将其表示为列表对象

      ![img](https://mubu.com/document_image/27af24f7-e7eb-4dee-ab82-acaa070400a0-5974427.jpg)

###### ②二维数据

- `概念`

  - 二维数据，也称表格数据，由关联关系数据构成， 采用二维表格方式组织，对应于数学中的矩阵

  - 常见的表格都属于二维数据

    ![img](https://mubu.com/document_image/bb051466-ed5c-45c7-9099-7a3030d8fffe-5974427.jpg)

- `表示`

  - 二维数据由多条一维数据构成，可以看成是一维数据的组合形式。因此，二维数据可以采用二维列表来表示，即列表的每个元素对应二维数据的 一行，这个元素本身也是列表类型，其内部各元素对应这行中的各列值

- `存储`

  - 二维数据由一维数据组成，用CSV格式文件存储。CSV文件的每一行是一维数据，整个CSV文件是一个二维数据

  - 二维列表对象输出为CSV格式文件方法如下，采用遍历循环和字符串的join()方法相结合

    ![img](https://mubu.com/document_image/003f02c4-97fb-4088-a10a-0bb5c5b67ec4-5974427.jpg)

- `处理`

  - 对二维数据进行处理首先需要从CSV格式文件读入二维数据，并将其表示为二维列表对象

    ![img](https://mubu.com/document_image/2fc40848-d565-4c0b-a3c7-f67fd42ad2a7-5974427.jpg)

  - 程序执行后二维列表对象ls的内容如下

    ![img](https://mubu.com/document_image/2a03cdf8-f219-4d54-b40c-19886884a688-5974427.jpg)

  - 二维数据处理等同于二维列表的操作，与一维列表不同，二维列表一般需要借助循环遍历实现对每个数据的处理

    ![img](https://mubu.com/document_image/064c72f3-a039-4331-a834-3aa47cb6dee5-5974427.jpg)

    ![img](https://mubu.com/document_image/05afa7db-a5fc-4380-b601-6cfc87e034d9-5974427.jpg)

###### ③高维数据

- `概念`

  - 高维数据由键值对类型的数据构成，采用对象方式组织，可以多层嵌套

  - 高维数据在Web系统中十分常用，作为当今 Internet组织内容的主要方式，高维数据衍生出 HTML、XML、JSON等具体数据组织的语法结构

    ![img](https://mubu.com/document_image/c344ae7d-f369-4dc5-ba41-d4ed817a537a-5974427.jpg)
