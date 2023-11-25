import os

import pyupbit


class Upbit:
    def __init__(self):
        self.access = os.environ["UPBIT_OPEN_API_ACCESS_KEY"]
        self.secret = os.environ["UPBIT_OPEN_API_SECRET_KEY"]
        self.client = pyupbit.Upbit(self.access, self.secret)

    # https://github.com/sharebook-kr/pyupbit

    def main(self):
        print(self.client.get_balance("KRW-XRP"))  # KRW-XRP 조회
        print(self.client.get_balance("KRW"))  # 보유 현금 조회
        print(self.client.get_balances())
