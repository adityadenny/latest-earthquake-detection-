"""
Latest Earthquake Detection Application
modularization with functions
d
"""


def data_extraction():
    """
    Date : 03 Maret 2022,
    Time : 13:37:04 WIB
    Magnitude : 4.8
    Depth : 10 km
    Location : 0.15 LU - 100.00 BT
    Epicenter : Pusat gempa berada di darat 8 km tenggara Talu
    Feel : Dirasakan (Skala MMI): III Pasaman Barat, I-II Padang Panjang, I-II Pariaman
    :return:
    """
    results = dict()
    results['date'] = '03 Maret 2022'
    results['time'] = '13:37:04 WIB'
    results['magnitude'] = 4.8
    results['depth'] = '10 km'
    results['location'] = {'LU': 1.48, 'BT': 100.00}
    results['epicenter'] = 'Pusat gempa berada di darat 8 km tenggara Talu'
    results['feel'] = 'Dirasakan (Skala MMI): III Pasaman Barat, I-II Padang Panjang, I-II Pariaman'

    return results


def show_data(result):
    print('Latest Earthquake based on bmkg.go.id:')
    print(f"Date : {result['date']}")
    print(f"Time : {result['time']}")
    print(f"Magnitude : {result['magnitude']}")
    print(f"Depth : {result['depth']}")
    print(f"Location : LU = {result['location']['LU']}, BT = {result['location']['BT']}")
    print(f"Epicenter : {result['epicenter']}")
    print(f"Feel : {result['feel']}")


if __name__ == '__main__':
    print('main application')
    result = data_extraction()
    show_data(result)