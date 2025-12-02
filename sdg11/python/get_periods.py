from collections.abc import Callable
from sys import argv
import numpy as np
import sqlite3
import json

PERIODS_FILE = "periodos.csv"

def estimates_periods(stops: dict[str,list[int]]) -> list[str]:
    out: list[str] = []
    periods: tuple[list[np.floating],...] = ([], [], [], [], [], [])
    mask_func: tuple[Callable[[np.ndarray], np.ndarray],...] = (
        lambda x: x,
        lambda x: x[x < 300],
        lambda x: x[(x >= 300) & (x <= 510)],
        lambda x: x[(x > 510) & (x < 1050)],
        lambda x: x[(x >= 1050) & (x <= 1140)],
        lambda x: x[x > 1140]
    )
    for stop_name in stops:
        if not stops[stop_name]: continue
        schedule = np.array(stops[stop_name])
        for i in range(6):
            selection = mask_func[i](schedule)
            if selection.size < 2: continue
            intervals = selection[1:] - selection[:-1]
            if np.all(intervals <= 0): continue
            periods[i].append(np.mean(intervals[intervals > 0]))
    for i in range(6):
        if not periods[i]:
            out.append('')
            continue
        stop_period = np.array(periods[i])
        mean = stop_period.mean()
        lim = stop_period.std()*1.5
        out.append('%.3f' % np.mean(stop_period[(stop_period >= mean-lim) & (stop_period <= mean+lim)]))
    return out

def main(schedules_fp: str, gpkg_fp: str):
    with open(PERIODS_FILE, 'w') as f:
        f.write("fid,cod,periodo_geral,periodo_fora1,periodo_pico1,periodo_fora2,periodo_pico2,periodo_fora3\n")
    # Read schedules
    with open(schedules_fp, 'rb') as f:
        schedules: dict[str, dict[str, list[int]]] = json.load(f)
    # Open GeoPackage
    with sqlite3.connect(gpkg_fp) as conn:
        cursor = conn.cursor()
        try:
            # Get feature layer
            cursor.execute("SELECT table_name FROM gpkg_contents LIMIT 1;")
            feature_table = cursor.fetchone()[0]
            # Append period records
            cursor.execute(f"SELECT fid, cod FROM {feature_table};")
            for (fid, code,) in cursor.fetchall():
                if not (stops := schedules.get(code)): continue
                with open(PERIODS_FILE, 'a') as f:
                    f.write(f"{fid},{code}," + ','.join(estimates_periods(stops)) + '\n')

        except Exception as e: print(f"\x1b[31mAn error occured:\x1b[0m\n{e!r}")

        finally: cursor.close()

if __name__ == "__main__":
    if len(argv[1:]) != 2:
        print(
            "Command:\n"
            "python <schedules_fp> <gpkg_fp>\n"
            "Parameters:\n"
            "schedules_fp   File path to schedules JSON generated with get_schedule.py\n"
            "gpkg_fp        File path to GeoPackage file that has bus lines. Will be\n"
            "               modified by this program."
        )
    else: main(argv[1], argv[2])
