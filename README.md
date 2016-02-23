# Holiday-counter
This small python script helps counting holiday days

To use it, create a json file named "./holidays.json" with the following structure:

    {
        "starting_date": "01/04/2015",
        "starting_days": 10,
        "days_per_month": 2.5,
        "holiday_reduction": 1,
        "holiday_reduction_every": 5,
        "holidays": [
                     	    {
                                "name": "My first holidays 2015",
                                "days": 3,
                            },
                            {
                                "name": "My second holidays 2015",
                                "days": 2,
                            }
                    ]
    }

usage
-----

    $> ./holiday-counter.py
    nb of days earned since 2015-04-01 00:00:00: 27.5
    nb of days used: 28
    nb of days left: -0.5
