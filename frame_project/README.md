#简介：UI自动化框架的改造

1.当yaml文件名字与py文件名字一致，会自动去解析yaml，动态导入函数，最终将yaml中的数据生成用例
2.数据驱动、数据分离

先解析yaml---如果需要导入指定包，则动态导入

yaml格式：

  - hello.a: []
  - print: ['abcde']
  - re.search: ['.*','xxxx']
  - save: [temp]    #将前面步骤的结果返回temp
  - print: [$(temp)]     #将变量打印出来，注意要加$

  - 代表list；
  不加-代表字典：字典不允许重名
  里面的关键字有些是自定义的，有些是内置的

  yaml是定义了格式的高阶txt


 自动导入：
      import re
      re.search()
 动态导入：


