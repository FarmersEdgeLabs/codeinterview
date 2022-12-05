from locater import locate


def main():
    # testing the locate function
    test_lat, test_long = 49.877129, -97.085386
    test2_lat, test2_long = 41.65682, -93.79158
    test3_lat, test3_long = 39.768783399760835, -71.54455408811515

    assert locate(test2_lat, test2_long) == 'Southeast 37th Street, Grimes, Polk County, Iowa, 50111, United States'
    assert locate(test_lat,
                  test_long) == 'Promenade Brunet, Maginot, Winnipeg, Division No. 11, Manitoba, R2J 1J9, Canada'
    assert locate(test3_lat, test3_long) == False


if __name__ == '__main__':
    main()
