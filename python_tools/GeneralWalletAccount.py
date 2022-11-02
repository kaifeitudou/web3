from eth_account import Account
import xlwt
import os
'''
批量生成钱包
保存钱包地址和私钥
注意：最好生成一次，以防覆盖掉私钥找不回
'''
def createNewEthWallet():
    if os.path.exists('account.xls'):
        print("account.xls is exist, return")
        exit()

    workbook = xlwt.Workbook(encoding='ascii')
    worksheet = workbook.add_sheet("eth_wallet")
    worksheet.write(0, 0, "address")
    worksheet.write(0, 1, "private")

    post = 1
    for i in range(1, 2000):
        account = Account.create()
        print("key: ", account.key.hex()[2:])
        print("address: ", account.address)
        worksheet.write(post, 0, account.address)
        worksheet.write(post, 1, account.key.hex()[2:])
        post += 1
    workbook.save("account.xls")
if __name__ == '__main__':
    createNewEthWallet()
