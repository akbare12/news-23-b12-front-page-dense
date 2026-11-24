[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/akbare12/news-23-b12-front-page-dense/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/akbare12/news-23-b12-front-page-dense/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

# The World Today — Monday 23 November 2026

A dense front page summing up the world's news of Monday 23 November 2026 in one
1024×1024 image: 31 stories across 6 regions.

**The day in one line:** the AI rout hits Asia (KOSPI −3.3%), the UN chief calls for
global AI safety rules in Bridgetown, and America's lead over China in the Asia
Power Index narrows to a record-low 5.3 points.

## What's on the page

- **Masthead + kicker** — the date, 23 November 2026, and the three lead stories.
- **Number strip** — −3.3% KOSPI · 5.3 US–China power gap · 11,762 Ebola cases in
  DRC · $450M Skubal to the Mets · 165 Russian missiles in a week.
- **Region bar** — Asia-Pacific 7 · Americas 8 · Europe 6 · Middle East 7 ·
  Africa 2 · World 1 (31 stories total).
- **The Day in UTC** — six timed milestones (times marked `~` are approximate).
- **3 hero scenes** — drawn illustrations of the AI rout, Guterres in Bridgetown,
  and the Asia Power Index bars.
- **10 illustrated cards** — Skubal, Anthropic's $107.3B IPO (raised at $83/share),
  Poland's 3 Russian missiles, COP31's day after, Zelenskyy's 165 missiles,
  Manchester, the Paris 2% billionaire-tax rally, Ebola in DRC, Lebanon's
  explosives seizure, Seoul's 10T-won fund.
- **World map + 13 numbered pins** and an 18-item "Also on Monday" list.
- **Date Check** — stories that are *not* 23 November (Democrats reach 258,
  Sparta II fire, El Chapo Isidro captured, EU–Indonesia pact, Nigeria boat,
  ICJ Myanmar ruling) are listed as left out, never as stories; plus a NOT YET
  line for still-developing items.
- **Chips** — REPORTED = confirmed by wires · CLAIM = one side alleges ·
  DENIAL = disputed · ONGOING = still developing.

Scenes are drawn illustrations, not photographs.

## How it runs

`draw.py` (Pillow) draws `entry.png`. `main.py` (standard library only) copies
`entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`, verifying the PNG header,
1024×1024 size, 1 MiB cap, and sha256 of the copy.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Sources

AP · Reuters · Bloomberg · AFP · Yonhap · Lowy Institute · UN News · wires read
23 Nov 2026.

## License

MIT — see [LICENSE](LICENSE).
