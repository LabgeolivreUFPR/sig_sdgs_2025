from collections.abc import Generator
from time import sleep, time
from re import finditer
import numpy as np
import requests
import json

def minutes(string: str) -> int:
    h,m = string.split(':')
    int_h = int(h)
    if int_h < 5: return 1440 + int_h*60 + int(m)
    return int_h*60 + int(m)

def iter_schedules(text: str) -> Generator[tuple[str, list[int]]]:
    for match in finditer(r"<h3\s+class\s*=\s*\"schedule\">.+:\s*(\w.*\w)\s*<\/h3>[\s\S]*?<\/ul>", text):
        yield (
            match.group(1),
            [minutes(x.group(1)) for x in finditer(r"<li>(\S+)<\/li>", match.group(0))]
        )

def save_tree(tree: dict):
    with open(f"schedules_{int(time()):x}.json", 'w', encoding = "utf-8") as f:
        json.dump(tree, f)

def main() -> int:
    bus_codes = np.genfromtxt("cod_linhas.csv", [("code",'U3'), ("nome", 'U32')], delimiter=',', encoding="utf-8")
    tree: dict[str, dict[str, list[int]]] = {}
    for code in bus_codes["code"]:
        print(code)
        try:
            response = requests.get(
                url = f"https://www.urbs.curitiba.pr.gov.br/horario-de-onibus/{code}/1",
                headers = {
                    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) "
                                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                                  "Chrome/142.0.0.0 "
                                  "Mobile Safari/537.36"
                },
                timeout = 15
            )
        except Exception as e:
            save_tree(tree)
            print(f"\x1b[31mRequest error:\x1b[0m{e!r}")
            return 2
        if response.status_code != 200:
            save_tree(tree)
            print(f"\x1b[31mAn error occured while accessing {code}:\x1b[0m\n{response.text}")
            return 1
        tree[code] = {}
        for terminal, schedule in iter_schedules(response.text):
            if terminal in tree[code]: continue
            print(f"    {terminal}")
            tree[code][terminal] = schedule
        sleep(3)
    save_tree(tree)
    return 0

if __name__ == "__main__": print("Return code:", main())