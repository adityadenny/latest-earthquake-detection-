"""
Latest Earthquake Detection Application
modularization with functions
"""
from earthquake_detection import data_extraction, show_data

if __name__ == '__main__':
    print('main application')
    result = data_extraction()
    show_data(result)