from flask import Blueprint, render_template, send_file
from application.exporter.logic import generate_excel

import os


exporterPage = Blueprint('exporterPage', __name__)


@exporterPage.route("/expoter")
def exporter():
    return render_template('expoter.html')


@exporterPage.route("/expoter/ckmx")
def export_ckmx():
    generate_excel(tableName='ckmx', documentName='出库明细')

    return send_file(os.path.join(os.path.dirname(os.path.abspath(__file__)), '出库明细.xlsx'), as_attachment=True)


@exporterPage.route("/expoter/cpmx")
def export_cpmx():
    generate_excel(tableName='cpmx', documentName='产品明细')

    return send_file(os.path.join(os.path.dirname(os.path.abspath(__file__)), '产品明细.xlsx'), as_attachment=True)


@exporterPage.route("/expoter/ddmx")
def export_ddmx():
    generate_excel(tableName='ddmx', documentName='订单明细')

    return send_file(os.path.join(os.path.dirname(os.path.abspath(__file__)), '订单明细.xlsx'), as_attachment=True)


@exporterPage.route("/expoter/htmx")
def export_htmx():
    generate_excel(tableName='htmx', documentName='合同明细')

    return send_file(os.path.join(os.path.dirname(os.path.abspath(__file__)), '合同明细.xlsx'), as_attachment=True)


@exporterPage.route("/expoter/zpsr")
def export_zpsr():
    generate_excel(tableName='zpsr', documentName='装配收入')

    return send_file(os.path.join(os.path.dirname(os.path.abspath(__file__)), '装配收入.xlsx'), as_attachment=True)


@exporterPage.route("/expoter/yflr")
def export_yflr():
    generate_excel(tableName='yflr', documentName='研发利润')

    return send_file(os.path.join(os.path.dirname(os.path.abspath(__file__)), '研发利润.xlsx'), as_attachment=True)


@exporterPage.route("/expoter/hccb")
def export_hccb():
    generate_excel(tableName='hccb', documentName='耗材成本')

    return send_file(os.path.join(os.path.dirname(os.path.abspath(__file__)), '耗材成本.xlsx'), as_attachment=True)


@exporterPage.route("/expoter/lrtz")
def export_lrtz():
    generate_excel(tableName='lrtz', documentName='利润调整')

    return send_file(os.path.join(os.path.dirname(os.path.abspath(__file__)), '利润调整.xlsx'), as_attachment=True)


@exporterPage.route("/expoter/fpsr")
def export_fpsr():
    generate_excel(tableName='fpsr', documentName='分配收入')

    return send_file(os.path.join(os.path.dirname(os.path.abspath(__file__)), '分配收入.xlsx'), as_attachment=True)


@exporterPage.route("/expoter/lrmx")
def export_lrmx():
    generate_excel(tableName='lrmx', documentName='利润明细')

    return send_file(os.path.join(os.path.dirname(os.path.abspath(__file__)), '利润明细.xlsx'), as_attachment=True)


@exporterPage.route("/expoter/lrhz")
def export_lrhz():
    generate_excel(tableName='lrhz', documentName='利润汇总')

    return send_file(os.path.join(os.path.dirname(os.path.abspath(__file__)), '利润汇总.xlsx'), as_attachment=True)


@exporterPage.route("/expoter/hthklr")
def export_hthklr():
    generate_excel(tableName='hthklr', documentName='合同回款利润')

    return send_file(os.path.join(os.path.dirname(os.path.abspath(__file__)), '合同回款利润.xlsx'), as_attachment=True)


@exporterPage.route("/expoter/tzclcb")
def export_tzclcb():
    generate_excel(tableName='tzclcb', documentName='调整材料成本')

    return send_file(os.path.join(os.path.dirname(os.path.abspath(__file__)), '调整材料成本.xlsx'), as_attachment=True)
