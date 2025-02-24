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
    # "Maharlika",
    # "Narra",
    # "Pacita 1",
    # "Poblacion",
    # "Langgam",
    # "Pacita 2",
    # "Cuyab",
    # "San Lorenzo Ruiz",
    # "Chrysanthemum",
    # "Laram",
    # "Landayan",
    # "Fatima",
    # "San Vicente",
    # "United Better Living",
    # "Bagong Silang",
    # "San Roque",
    # "Nueva",
    # "Calendola",
    # "Sampaguita Village",
    # "Riverside",
    # "Rosario",
    # "United Bayanihan",
    # "Estrella",
    # "G.S.I.S.",
    # "Santo Niño",
]

with open("magsaysay-sanantonio6months_data.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(
        [
            "barangay_Res",
            "date",
            "count_Exposed",
            "count_Infected",
            "count_Recovered",
            "count_Exposed_age_9_below",
            "count_Exposed_age_10_17",
            "count_Exposed_age_18_39",
            "count_Exposed_age_40_59",
            "count_Exposed_age_60_79",
            "count_Exposed_age_80_above",
            "count_Infected_age_9_below",
            "count_Infected_age_10_17",
            "count_Infected_age_18_39",
            "count_Infected_age_40_59",
            "count_Infected_age_60_79",
            "count_Infected_age_80_above",
            "count_Recovered_age_9_below",
            "count_Recovered_age_10_17",
            "count_Recovered_age_18_39",
            "count_Recovered_age_40_59",
            "count_Recovered_age_60_79",
            "count_Recovered_age_80_above",
            "count_Exposed_Unknown",
            "count_Infected_Unknown",
            "count_Recovered_Unknown",
            "count_Exposed_Male",
            "count_Exposed_Female",
            "count_Infected_Male",
            "count_Infected_Female",
            "count_Recovered_Male",
            "count_Recovered_Female",
        ]
    )

    for barangay in barangays:
        for i in range(num_days):
            date = (start_date + timedelta(days=i)).strftime("%Y-%m-%d")

            count_Exposed_age_9_below = random.randint(0, 10)
            count_Exposed_age_10_17 = random.randint(0, 10)
            count_Exposed_age_18_39 = random.randint(0, 10)
            count_Exposed_age_40_59 = random.randint(0, 10)
            count_Exposed_age_60_79 = random.randint(0, 10)
            count_Exposed_age_80_above = random.randint(0, 10)
            count_Exposed_Unknown = random.randint(0, 10)

            count_Recovered_age_9_below = random.randint(0, 10)
            count_Recovered_age_10_17 = random.randint(0, 10)
            count_Recovered_age_18_39 = random.randint(0, 10)
            count_Recovered_age_40_59 = random.randint(0, 10)
            count_Recovered_age_60_79 = random.randint(0, 10)
            count_Recovered_age_80_above = random.randint(0, 10)
            count_Recovered_Unknown = random.randint(0, 10)

            count_Exposed = (
                count_Exposed_age_9_below
                + count_Exposed_age_10_17
                + count_Exposed_age_18_39
                + count_Exposed_age_40_59
                + count_Exposed_age_60_79
                + count_Exposed_age_80_above
                + count_Exposed_Unknown
            )

            # Create an upward and downward curve for count_Infected using a sine function
            sine_value = math.sin(math.pi * i / num_days)
            count_Infected = int(
                (sine_value + 1) * 15
            )  # Scale and shift to fit within the range 0-10

            # Distribute count_Infected across count_Infected_xx fields
            count_Infected_age_9_below = random.randint(0, count_Infected)
            remaining = count_Infected - count_Infected_age_9_below
            count_Infected_age_10_17 = random.randint(0, remaining)
            remaining -= count_Infected_age_10_17
            count_Infected_age_18_39 = random.randint(0, remaining)
            remaining -= count_Infected_age_18_39
            count_Infected_age_40_59 = random.randint(0, remaining)
            remaining -= count_Infected_age_40_59
            count_Infected_age_60_79 = random.randint(0, remaining)
            remaining -= count_Infected_age_60_79
            count_Infected_age_80_above = random.randint(0, remaining)
            remaining -= count_Infected_age_80_above
            count_Infected_Unknown = remaining

            count_Recovered = (
                count_Recovered_age_9_below
                + count_Recovered_age_10_17
                + count_Recovered_age_18_39
                + count_Recovered_age_40_59
                + count_Recovered_age_60_79
                + count_Recovered_age_80_above
                + count_Recovered_Unknown
            )

            # Ensure male and female counts sum to total counts
            count_Exposed_Male = random.randint(0, count_Exposed)
            count_Exposed_Female = count_Exposed - count_Exposed_Male

            count_Infected_Male = random.randint(0, count_Infected)
            count_Infected_Female = count_Infected - count_Infected_Male

            count_Recovered_Male = random.randint(0, count_Recovered)
            count_Recovered_Female = count_Recovered - count_Recovered_Male

            writer.writerow(
                [
                    barangay,
                    date,
                    count_Exposed,
                    count_Infected,
                    count_Recovered,
                    count_Exposed_age_9_below,
                    count_Exposed_age_10_17,
                    count_Exposed_age_18_39,
                    count_Exposed_age_40_59,
                    count_Exposed_age_60_79,
                    count_Exposed_age_80_above,
                    count_Infected_age_9_below,
                    count_Infected_age_10_17,
                    count_Infected_age_18_39,
                    count_Infected_age_40_59,
                    count_Infected_age_60_79,
                    count_Infected_age_80_above,
                    count_Recovered_age_9_below,
                    count_Recovered_age_10_17,
                    count_Recovered_age_18_39,
                    count_Recovered_age_40_59,
                    count_Recovered_age_60_79,
                    count_Recovered_age_80_above,
                    count_Exposed_Unknown,
                    count_Infected_Unknown,
                    count_Recovered_Unknown,
                    count_Exposed_Male,
                    count_Exposed_Female,
                    count_Infected_Male,
                    count_Infected_Female,
                    count_Recovered_Male,
                    count_Recovered_Female,
                ]
            )