#!/usr/bin/python

import json
import datetime
from dateutil.rrule import rrule, MONTHLY


HOLIDAYS_FILE = "./holidays.json"


def read_holidays(file):
	with open(file) as f:
		data = json.load(f)
	return data


def get_number_month(d1, d2):
	strt_dt = datetime.date(2001,1,1)
	end_dt = datetime.date(2005,6,1)
	return len([dt for dt in rrule(MONTHLY, dtstart=d1, until=d2)])


def to_date(s):
	return datetime.datetime.strptime(s, "%d/%m/%Y")


def get_nb_days_used(holidays):
	sum = 0
	for h in holidays:
		sum += h["days"]
	return sum


if __name__ == "__main__":
	holidays = read_holidays(HOLIDAYS_FILE)

	starting_date = to_date(holidays["starting_date"])
	nb_months = get_number_month(starting_date, datetime.datetime.now())
	days_earned = holidays["days_per_month"] * nb_months

	days_used = get_nb_days_used(holidays["holidays"])
	reductions = days_used % holidays["holiday_reduction_every"]
	days_used += reductions * holidays["holiday_reduction"]

	print("nb of days earned since " + str(starting_date) + ": " + str(days_earned))
	print("nb of days used: " + str(days_used))
	print("nb of days left: " + str(days_earned - days_used))
