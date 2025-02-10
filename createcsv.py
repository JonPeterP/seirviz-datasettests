import csv
import random
from datetime import datetime, timedelta

barangays = ["Landayan", "Bagong Silang", "Narra", "Poblacion", "San Antonio"]
start_date = datetime(2025, 1, 20)  # Start date from January 20
end_date = datetime.today()
num_days = (end_date - start_date).days + 1

with open('createcsv.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([
        "barangay_Res", "date", "count_Exposed", "count_Infectious", "count_Recovered",
        "count_Specimen_age_9_below", "count_Specimen_age_10_17", "count_Specimen_age_18_39",
        "count_Specimen_age_40_59", "count_Specimen_age_60_79", "count_Specimen_age_80_above",
        "count_Conf_age_9_below", "count_Conf_age_10_17", "count_Conf_age_18_39",
        "count_Conf_age_40_59", "count_Conf_age_60_79", "count_Conf_age_80_above",
        "count_Reco_age_9_below", "count_Reco_age_10_17", "count_Reco_age_18_39",
        "count_Reco_age_40_59", "count_Reco_age_60_79", "count_Reco_age_80_above",
        "count_Specimen_Unknown", "count_Conf_Unknown", "count_Reco_Unknown"
    ])

    for i in range(num_days):
        barangay = random.choice(barangays)
        date = (start_date + timedelta(days=i)).strftime("%Y-%m-%d")
        count_Exposed = random.randint(0, 10)
        count_Infectious = random.randint(0, 10)
        count_Recovered = random.randint(0, 10)
        count_Specimen_age_9_below = random.randint(0, 10)
        count_Specimen_age_10_17 = random.randint(0, 10)
        count_Specimen_age_18_39 = random.randint(0, 10)
        count_Specimen_age_40_59 = random.randint(0, 10)
        count_Specimen_age_60_79 = random.randint(0, 10)
        count_Specimen_age_80_above = random.randint(0, 10)
        count_Conf_age_9_below = random.randint(0, 10)
        count_Conf_age_10_17 = random.randint(0, 10)
        count_Conf_age_18_39 = random.randint(0, 10)
        count_Conf_age_40_59 = random.randint(0, 10)
        count_Conf_age_60_79 = random.randint(0, 10)
        count_Conf_age_80_above = random.randint(0, 10)
        count_Reco_age_9_below = random.randint(0, 10)
        count_Reco_age_10_17 = random.randint(0, 10)
        count_Reco_age_18_39 = random.randint(0, 10)
        count_Reco_age_40_59 = random.randint(0, 10)
        count_Reco_age_60_79 = random.randint(0, 10)
        count_Reco_age_80_above = random.randint(0, 10)
        count_Specimen_Unknown = random.randint(0, 10)
        count_Conf_Unknown = random.randint(0, 10)
        count_Reco_Unknown = random.randint(0, 10)

        writer.writerow([
            barangay, date, count_Exposed, count_Infectious, count_Recovered,
            count_Specimen_age_9_below, count_Specimen_age_10_17, count_Specimen_age_18_39,
            count_Specimen_age_40_59, count_Specimen_age_60_79, count_Specimen_age_80_above,
            count_Conf_age_9_below, count_Conf_age_10_17, count_Conf_age_18_39,
            count_Conf_age_40_59, count_Conf_age_60_79, count_Conf_age_80_above,
            count_Reco_age_9_below, count_Reco_age_10_17, count_Reco_age_18_39,
            count_Reco_age_40_59, count_Reco_age_60_79, count_Reco_age_80_above,
            count_Specimen_Unknown, count_Conf_Unknown, count_Reco_Unknown
        ])