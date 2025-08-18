def array_to_dict(array):
    """ヘッダーありの配列を辞書のリストに変換する"""
    headers = array[0]
    return [dict(zip(headers, row)) for row in array[1:]]
