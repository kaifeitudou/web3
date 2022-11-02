from eth_account import Account
import xlwt
import os
'''
批量生成钱包
保存钱包地址和私钥
注意：最好生成一次，以防覆盖掉私钥找不回
'''
def createNewEthWallet():
    if os.path.exists('eth_wallet220506.xls'):
        print("eth_wallet.xls is exist, return")
        exit()

    workbook = xlwt.Workbook(encoding='ascii')
    worksheet = workbook.add_sheet("eth_wallet")
    worksheet.write(0, 0, "address")
    worksheet.write(0, 1, "private")

    post = 1
    for i in range(1, 2000):
        account = Account.create()
        #privateKey = account.privateKey()
        #print("privateKey: ", account.privateKey)
        #print("key: ", type(account.key))
        print("key: ", account.key.hex()[2:])
        print("address: ", account.address)
        worksheet.write(post, 0, account.address)
        worksheet.write(post, 1, account.key.hex()[2:])
        post += 1
    workbook.save("eth_wallet220506.xls")


def input_name_excel():
    workbook = xlwt.Workbook(encoding='ascii')
    worksheet = workbook.add_sheet("name_mapping")
    worksheet.write(0, 0, "S Name")
    worksheet.write(0, 1, "D Name")

    post = 1
    while 1:
        line = source.readline()
        if not line:
            break
        elif len(line) < 2:
            continue
        line = line.replace("\n", "")
        worksheet.write(post, 0, line)
        sql = line.replace("_view", "")
        sql = 'ads_' + sql
        worksheet.write(post, 1, sql)
        post += 1
    workbook.save("Name_Map.xls")
    source.close()

if __name__ == '__main__':
    createNewEthWallet()