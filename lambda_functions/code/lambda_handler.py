import datetime

from api import MercadoBitcoinApi
from writer import S3Writer


def handler(event, context):
    coin = "BTC"
    date = (datetime.datetime.now() - datetime.timedelta(days=1)).date()

    api = MercadoBitcoinApi(coin=coin)
    data = api.get_data(date=date)

    writer = S3Writer(coin=coin)
    writer.write(data)

    # TODO: Ajustar para ingerir várias moedas
    # TODO: Ajustar para ingerir o historico a partir de uma data
    # TODO: Arranjar uma maneira de vericar se um dia já foi ingerido ou não