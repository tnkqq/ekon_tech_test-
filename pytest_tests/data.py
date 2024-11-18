import datetime


class InitTestData:
    customer_test_data = {
        1: {
            "name": "Customer1",
        },
        2: {
            "name": "Customer2",
        },
        3: {
            "name": "Customer3",
        },
    }

    trafic_test_data = [
        {
            "customer_id": 1,
            "ip": "127.0.0.1",
            "date": datetime.datetime(2004, 7, 1, 20, 1, 30),
            "received_trafic": 22,
        },
        {
            "customer_id": 1,
            "ip": "127.0.0.2",
            "date": datetime.datetime(2006, 7, 1, 20, 1, 30),
            "received_trafic": 23,
        },
        {
            "customer_id": 1,
            "ip": "127.0.0.2",
            "date": datetime.datetime(2002, 7, 2, 20, 1, 30),
            "received_trafic": 24,
        },
        {
            "customer_id": 2,
            "ip": "127.0.0.2",
            "date": datetime.datetime(2006, 7, 2, 20, 1, 30),
            "received_trafic": 25,
        },
        {
            "customer_id": 3,
            "ip": "128.0.0.2",
            "date": datetime.datetime(2009, 7, 2, 20, 1, 30),
            "received_trafic": 26,
        },
    ]

    @classmethod
    def ip_trafic_data(cls):
        return set(
            [
                (
                    _.get("ip"),
                    sum(
                        [
                            (
                                int(x.get("received_trafic"))
                                if x.get("ip") == _.get("ip")
                                else 0
                            )
                            for x in cls.trafic_test_data
                        ]
                    ),
                )
                for _ in cls.trafic_test_data
            ]
        )

    @classmethod
    def customer_trafic_data(cls):
        return [
            (
                _.get("customer_id"),
                sum(
                    [
                        (
                            int(x.get("received_trafic"))
                            if x.get("customer_id") == _.get("customer_id")
                            else 0
                        )
                        for x in cls.trafic_test_data
                    ]
                ),
            )
            for _ in cls.trafic_test_data
        ]

    @classmethod
    def sorted_trafics_datetime(cls):
        return sorted([_.get("date") for _ in cls.trafic_test_data])


print(InitTestData.sorted_trafics_datetime())
