# news-image-20261121

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/BIDGDCB/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/BIDGDCB/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

One image summing up the world news of **Saturday 21 November 2026**, for the
make.fun competition `news-image-20261121`. Built for [make.fun's bounty](https://make.fun/bounty/news-image-20261121).

## The image

`entry.png` (1024x1024, drawn with Pillow by `draw.py`) covers six stories:

1. **Top story — Missiles land in Poland**: Russia's huge overnight strike
   on Ukraine (400+ drones, 110+ missiles) crossed the border; Poland's PM
   calls it a deliberate provocation, and Kyiv's bridges were hit.
2. **Iran** — the Revolutionary Guard shot down a US drone over Hormuz as
   talks stall; Trump weighs new strikes.
3. **Peru** — a magnitude 6.9 earthquake shook the Andes, felt in Lima; no
   damage or casualties reported at first.
4. **COP31** — climate talks in Antalya run into overtime, deadlocked over
   fossil fuels.
5. **Health** — the pill daraxonrasib made tumours undetectable in 1 in 12
   pancreatic cancer patients in a trial.
6. **Also today** — UK & EU sign post-Brexit deals in Brussels; Verstappen
   takes pole in Las Vegas; Gen Z protests spread across 25 countries.

Sources: Reuters, AP, BBC, Al Jazeera, USGS.

## Files

- `draw.py` — the Pillow script that draws `entry.png` (deterministic).
- `entry.png` — the 1024x1024 image.
- `main.ts` — Node 22 entrypoint: copies `entry.png` to
  `$MAKEFUN_OUTPUT_DIR/entry.png`, refusing if it is over 1 MiB.

## Run

```sh
python3 draw.py            # regenerate entry.png
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts   # write out/entry.png
```
