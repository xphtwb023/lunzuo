通过轮作升级概率：T1-> T2: 25%, T2-> T3: 20%, T3-> T4: 3%
概率数据来自于https://forgottenarbiter.github.io/Poe-Harvest-Mechanics/

然后生成了一个1000样本（指的是怪物数量不是命能数量）的不同等级分布的期望值
然后根据一个公式来计算出国服流放之路不同颜色命能的价值积分，从而简化了程序避免递归深度太大

因为国服的命能对应神圣石比例是黄7D，蓝紫4D，也就是黄比篮紫等于7：4

这里我们不用命能数做为对比依据，而是只算他的价值，因为最终都是为了获得更多的价值

游戏中每个颜色的农田都会有22-23个初始怪物生成，为了方便计算以20为固定数

然后因为1级和2级怪获得的命能数可以忽略，所以不去计算1级和2级怪物的数量，只考虑3级和4级的可能

根据这个价值比可以得到一个公式以黄命能被升级了两次为例：20×3级数量L3_COUNT/1000×7(这里就是表格中的收益系数)+20×4级数量L4_COUNT/1000×35(因为4级的命能数比3级的多5倍左右)
可以得到下面这张表格

![image](https://github.com/user-attachments/assets/61c84e2d-954b-449b-9ec8-43a4cf778f82)

升级次数	新列1（收益系数A）	新列2（收益系数B）	1级数量	2级数量	3级数量	4级数量

1	0	0	750	250	0	0

2	7	4	562.5	387.5	50	0

3	18.69	10.68	421.88	450.63	126	1.5

4	30.94	17.79	316.41	465.97	212.35	5.28

5	43.33	25.15	237.3	451.88	299.17	11.65

6	55.09	32.11	177.98	420.83	380.57	20.63

7	66.65	39.07	133.48	381.16	453.12	32.04

8	78.07	46.06	100.11	338.3	515.76	45.64

9	89.75	53.46	75.08	295.67	567.94	61.11

根据这个表格就可以获得一个期望的价值积分，那么只要比对积分大小，就可以知道那种收割顺序可以在数学的期望上是最大的

