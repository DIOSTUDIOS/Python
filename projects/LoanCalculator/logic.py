from math import log
from matplotlib import pyplot as plt


def equal_principal_and_interest(P=0.00, i=0.00, n=0):
    """
        等额本息
        已知参数:
            P (float): 借款金额（元）
            i (float): 年利率（%）
            n (int): 还款期数（月）

        需要计算:
            im（float）: 月利率
            Y（float）: 月供
            S（float）: 本息和
            I（float）: 利息额
            Yi（float）: 利息/月
            Yp（float）: 本金/月
            Pr（float）: 剩余本金/月
    """
    im = i / 12 / 100
    # 月供
    Y = (P * im * (1 + im) ** n) / (((1 + im) ** n) - 1)
    # 累计还款额
    S = n * Y
    # 累计利息额
    I = S - P

    Yi = []
    Yp = []
    Pr = []

    for k in range(1, n + 1):
        Yi.append(Y - (1 + im) ** (k - 1) * (Y - im * P))
        Yp.append((1 + im) ** (k - 1) * (Y - im * P))
        Pr.append((1 + im) ** k * (P - Y/im) + Y/im)

    return P, n, i, Y, S, I, Yp, Yi, Pr


def equal_principal_amount(P=0.00, i=0.00, n=0):
    """
        等额本金
        已知参数:
            P (float): 借款金额（元）
            i (float): 年利率（%）
            n (int): 还款期数（月）

        需要计算:
            im（float）: 月利率
            Y（float）: 月供
            S（float）: 本息和
            I（float）: 利息额
            Yi（float）: 利息/月
            Yp（float）: 本金/月
            Pr（float）: 剩余本金/月
    """
    # 计算月利率
    im = i / 12 / 100
    S = P * im * (n + 1) / 2 + P
    I = P * im * (n + 1) / 2
    Yp = P / n

    Pr = []
    Yi = []
    Y = []

    for k in range(1, n + 1):
        Pr.append(P - Yp * k)
        Yi.append(im * (P - Yp * (k - 1)))
        Y.append(Yp + Yi[k - 1])

    return P, n, i, Y, S, I, Yi, Yp, Pr


# 提前还款计算
def early_repayment(P=0.00, i=0.00, n=0, T=0.00, m=0):
    """
    提前还款
    已知参数：
        P (float): 借款金额（元）
        i (float): 年利率（%）
        n (int): 还款期数（月）
        T (float): 提前还款金额（元）
        m (int): 提前还款期数（月）

    需要计算:
        im（float）: 月利率
        Y（float）: 月供
        Yi（float）: 利息/月
        Yp（float）: 本金/月
        Yn（float）: 提前还款后月供
        S（float）: 本息和
        Sn（float）: 提前还款后本息和
        Se（float）: 提前还款后节省金额
        I（float）: 利息额
        In（float）: 提前还款后利息额
        Pr（float）: 剩余本金/月
        Pn（float）: 提前还款后剩余本金
        ne(float）: 提前还款后还款期数（月）
    """
    im = i / 12 / 100
    # 等额本息
    Y = equal_principal_and_interest(P=P, i=i, n=n)[0]
    S = equal_principal_and_interest(P=P, i=i, n=n)[1]
    Pn = (1 + im) ** m * (P - Y/im) + Y/im - T
    print(f'月供{Y:.2f}')
    print(f'本息和{S:.2f}')
    print(f'剩余本金{Pn:.2f}')
    # 减少月供保持期数
    Yn = (Pn * (1 + im) ** (n - m) * im) / ((1 + im) ** (n - m) - 1)
    Sn = ((n - m) * Pn * (1 + im) ** (n - m) * im) / ((1 + im) ** (n - m) - 1)
    Se = S - m * Y - T - Sn
    # print(Yn, Sn, Se)
    print(f'提前还款月供{Yn:.2f}')
    print(f'提前还款本息和{Sn:.2f}')
    print(f'提前还款节省金额{Se:.2f}')
    # 保持月供缩短期数
    Y = equal_principal_and_interest(P=P, i=i, n=n)[0]
    ne = (log(Y / (Y - Pn * im))) / (log(1 + im))
    Sn = ne * Y
    Se = (n - m - ne) * Y - T
    # 等额本金
    Pn = P - P / n * m - T
    # 减少月供保持期数
    # 保持月供缩短期数


#  利率变化
def calculate_interest_rate_change(loan_amount, interest_rates, loan_terms):
    periods = sum(loan_terms)
    remaining_balance = loan_amount
    total_payment = 0
    total_interest = 0

    for i, rate in enumerate(interest_rates):
        monthly_interest_rate = rate / 12 / 100
        monthly_payment = (loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** periods) / ((1 + monthly_interest_rate) ** periods - 1)

        for month in range(1, loan_terms[i] + 1):
            monthly_interest = remaining_balance * monthly_interest_rate
            monthly_principal = monthly_payment - monthly_interest

            if remaining_balance - monthly_principal <= 0:
                monthly_payment = remaining_balance + monthly_interest
                remaining_balance = 0
            else:
                remaining_balance -= monthly_principal

            total_interest += monthly_interest

            print(f'月供:{monthly_payment:.2f}')

        total_payment += monthly_payment


# 还款计划表生成
def generate_repayment_schedule(loan_amount, annual_interest_rate, periods):
    monthly_interest_rate = annual_interest_rate / 12 / 100
    # total_payments = loan_term * 12
    remaining_balance = loan_amount
    monthly_payment = (loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** periods) / \
                      ((1 + monthly_interest_rate) ** periods - 1)

    print("{:<10} {:<15} {:<15} {:<15}".format("期数", "本金", "利息", "剩余贷款"))
    for month in range(1, periods + 1):
        monthly_interest = remaining_balance * monthly_interest_rate
        monthly_principal = monthly_payment - monthly_interest

        if remaining_balance - monthly_principal <= 0:
            monthly_payment = remaining_balance + monthly_interest
            remaining_balance = 0
        else:
            remaining_balance -= monthly_principal

        print("{:<10} {:<15.2f} {:<15.2f} {:<15.2f}".format(month, monthly_principal, monthly_interest, remaining_balance))


# 数据可视化
def visualize_data(loan_amount, annual_interest_rate, loan_term):
    monthly_interest_rate = annual_interest_rate / 12 / 100
    total_payments = loan_term * 12
    remaining_balance = loan_amount
    monthly_payment = (loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** total_payments) / \
                      ((1 + monthly_interest_rate) ** total_payments - 1)

    principal_paid = []
    interest_paid = []
    remaining_balance_list = []

    for month in range(1, total_payments + 1):
        monthly_interest = remaining_balance * monthly_interest_rate
        monthly_principal = monthly_payment - monthly_interest

        if remaining_balance - monthly_principal <= 0:
            monthly_payment = remaining_balance + monthly_interest
            remaining_balance = 0
        else:
            remaining_balance -= monthly_principal

        principal_paid.append(monthly_principal)
        interest_paid.append(monthly_interest)
        remaining_balance_list.append(remaining_balance)

    # 绘制图表
    plt.figure(figsize=(10, 6))
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.plot(principal_paid, label='本金')
    plt.plot(interest_paid, label='利息')
    plt.plot(remaining_balance_list, label='剩余贷款')

    plt.title('贷款还款计划')
    plt.xlabel('期数')
    plt.ylabel('金额')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    early_repayment(285000, 3.10, 276, 20000, 18)
    pass
