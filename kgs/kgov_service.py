from kgs.client import KGSClient

client = KGSClient()


# todo: cache && schedule
def get_stats():
    return client.load_stats()
