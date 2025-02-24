import csv
import random
from datetime import datetime, timedelta
import math

barangay = "Landayan"
start_date = datetime.today() - timedelta(days=6 * 30)
end_date = datetime.today()
num_days = (end_date - start_date).days + 1
barangays = [
    "Magsaysay",
    "San Antonio",
    "Maharlika",
    "Narra",
    "Pacita 1",
    "Poblacion",
    "Langgam",
    "Pacita 2",
    "Cuyab",
    "San Lorenzo Ruiz",
    "Chrysanthemum",
    "Laram",
    "Landayan",
    "Fatima",
    "San Vicente",
    "United Better Living",
    "Bagong Silang",
    "San Roque",
    "Nueva",
    "Calendola",
    "Sampaguita Village",
    "Riverside",
    "Rosario",
    "United Bayanihan",
    "Estrella",
    "G.S.I.S.",
    "Santo Niño",
]

with open("allbrgy6months_data.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(
        [
            "barangay_Res",
            "date",
            "count_Exposed",
            "count_Infectious",
            "count_Recovered",
            "count_Specimen_age_9_below",
            "count_Specimen_age_10_17",
            "count_Specimen_age_18_39",
            "count_Specimen_age_40_59",
            "count_Specimen_age_60_79",
            "count_Specimen_age_80_above",
            "count_Conf_age_9_below",
            "count_Conf_age_10_17",
            "count_Conf_age_18_39",
            "count_Conf_age_40_59",
            "count_Conf_age_60_79",
            "count_Conf_age_80_above",
            "count_Reco_age_9_below",
            "count_Reco_age_10_17",
            "count_Reco_age_18_39",
            "count_Reco_age_40_59",
            "count_Reco_age_60_79",
            "count_Reco_age_80_above",
            "count_Specimen_Unknown",
            "count_Conf_Unknown",
            "count_Reco_Unknown",
        ]
    )

    for barangay in barangays:
        for i in range(num_days):
            date = (start_date + timedelta(days=i)).strftime("%Y-%m-%d")

            count_Specimen_age_9_below = random.randint(0, 10)
            count_Specimen_age_10_17 = random.randint(0, 10)
            count_Specimen_age_18_39 = random.randint(0, 10)
            count_Specimen_age_40_59 = random.randint(0, 10)
            count_Specimen_age_60_79 = random.randint(0, 10)
            count_Specimen_age_80_above = random.randint(0, 10)
            count_Specimen_Unknown = random.randint(0, 10)

            count_Reco_age_9_below = random.randint(0, 10)
            count_Reco_age_10_17 = random.randint(0, 10)
            count_Reco_age_18_39 = random.randint(0, 10)
            count_Reco_age_40_59 = random.randint(0, 10)
            count_Reco_age_60_79 = random.randint(0, 10)
            count_Reco_age_80_above = random.randint(0, 10)
            count_Reco_Unknown = random.randint(0, 10)

            count_Exposed = (
                count_Specimen_age_9_below
                + count_Specimen_age_10_17
                + count_Specimen_age_18_39
                + count_Specimen_age_40_59
                + count_Specimen_age_60_79
                + count_Specimen_age_80_above
                + count_Specimen_Unknown
            )

            # Create an upward and downward curve for count_Infectious using a sine function
            sine_value = math.sin(math.pi * i / num_days)
            count_Infectious = int(
                (sine_value + 1) * 15
            )  # Scale and shift to fit within the range 0-10

            # Distribute count_Infectious across count_Conf_xx fields
            count_Conf_age_9_below = random.randint(0, count_Infectious)
            remaining = count_Infectious - count_Conf_age_9_below
            count_Conf_age_10_17 = random.randint(0, remaining)
            remaining -= count_Conf_age_10_17
            count_Conf_age_18_39 = random.randint(0, remaining)
            remaining -= count_Conf_age_18_39
            count_Conf_age_40_59 = random.randint(0, remaining)
            remaining -= count_Conf_age_40_59
            count_Conf_age_60_79 = random.randint(0, remaining)
            remaining -= count_Conf_age_60_79
            count_Conf_age_80_above = random.randint(0, remaining)
            remaining -= count_Conf_age_80_above
            count_Conf_Unknown = remaining

            count_Recovered = (
                count_Reco_age_9_below
                + count_Reco_age_10_17
                + count_Reco_age_18_39
                + count_Reco_age_40_59
                + count_Reco_age_60_79
                + count_Reco_age_80_above
                + count_Reco_Unknown
            )

            writer.writerow(
                [
                    barangay,
                    date,
                    count_Exposed,
                    count_Infectious,
                    count_Recovered,
                    count_Specimen_age_9_below,
                    count_Specimen_age_10_17,
                    count_Specimen_age_18_39,
                    count_Specimen_age_40_59,
                    count_Specimen_age_60_79,
                    count_Specimen_age_80_above,
                    count_Conf_age_9_below,
                    count_Conf_age_10_17,
                    count_Conf_age_18_39,
                    count_Conf_age_40_59,
                    count_Conf_age_60_79,
                    count_Conf_age_80_above,
                    count_Reco_age_9_below,
                    count_Reco_age_10_17,
                    count_Reco_age_18_39,
                    count_Reco_age_40_59,
                    count_Reco_age_60_79,
                    count_Reco_age_80_above,
                    count_Specimen_Unknown,
                    count_Conf_Unknown,
                    count_Reco_Unknown,
                ]
            )  # Start date 6 months ago
