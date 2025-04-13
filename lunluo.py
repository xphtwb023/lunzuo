import itertools

# 定义升级次数对应的A和B系数（A表示黄，B表示蓝紫）
upgrade_data = {
    1: {'A': 0.00, 'B': 0.00},
    2: {'A': 7.00, 'B': 4.00},
    3: {'A': 18.69, 'B': 10.68},
    4: {'A': 33.43, 'B': 19.08},
    5: {'A': 50.04, 'B': 28.82},
    6: {'A': 66.86, 'B': 38.64},
    7: {'A': 84.34, 'B': 49.12},
    8: {'A': 101.89, 'B': 59.84},
    9: {'A': 120.58, 'B': 71.77},
}


def parse_input(input_str):
    """解析输入字符串为队伍列表"""
    parts = input_str.strip().split()
    teams = []
    for part in parts:
        color = part[0]
        quantity = int(part[1:])
        coeff_type = 'A' if color == '黄' else 'B'
        teams.append({'color': color, 'quantity': quantity, 'coeff_type': coeff_type})
    return teams

def calculate_score(order):
    """计算指定顺序的总积分"""
    total = 0.0
    current_p = 0  # 当前累计P值
    for team in order:
        # 获取当前升级次数（取当前P值和9的较小值）
        upgrade_step = min(current_p, 9)

        # 获取系数值
        coeff = upgrade_data.get(upgrade_step + 1, {'A': 0.00, 'B': 0.00})[team['coeff_type']]

        # 计算本次贡献 (公式:系数 * 数量)
        contribution = coeff * team['quantity']
        total += contribution

        # 更新累计P值
        current_p += team['quantity']
    return round(total, 2)


def main():
    # 获取用户输入
    input_str = input("请输入颜色和数量（例如：黄2 蓝2 紫4）: ")
    teams = parse_input(input_str)
    # 生成所有可能的排列组合
    max_score = -1
    best_order = None

    # 遍历所有排列计算积分
    for perm in itertools.permutations(teams):
        current_score = calculate_score(perm)
        if current_score > max_score:
            max_score = current_score
            best_order = perm
    # 格式化输出结果
    order_str = " → ".join([f"{team['color']}{team['quantity']}" for team in best_order])
    print("\n最优排列顺序及积分：")
    print(f"顺序：{order_str}")
    print(f"总积分：{max_score:.2f}")
if __name__ == "__main__":
    main()
