# Salmon data scout (multi-site synchrony)

reviewed: false. 2026-11-06.

Checked by fetching files (columns verified) unless marked "not checked". Scratch copies: `/Users/pmahon/.claude/jobs/26482d7b/tmp/salmon/`.

## Ranked table

| # | Dataset | Species | Stocks x years | Variable | Coords? | Programmes | Access / licence |
|---|---|---|---|---|---|---|---|
| 1 | NCEAS Portfolio Effects "Salmon spawn and recruit data ... Alaska and North Pacific (1922-2014)" (KNB, pkg `df35b.298.15`) | sockeye (also pink, chum, chinook, coho) | 188 series; sockeye 70 series, 40 with >=40 brood years; 6212 rows | spawners, recruits (R/S computable) | YES, lat/lon per stock (table 2) but see caveat | ADF&G reports (Bristol Bay, Chignik, Cook Inlet, PWS, Kodiak) + Dorner et al. 2008 compilation (Fraser/DFO, Skeena, Pacific NW) | open, no login. Attribute to ADF&G + Dorner 2008, notify contacts, ADF&G disclaimer (EML intellectualRights) |
| 2 | PSC Fraser Sockeye Stock-Recruit Dataset | Fraser sockeye | 27 production stocks (about 19 with >=50 brood years), 1948-2019, 1405 rows | spawners, EFS, recruits by age (R = sum of age columns) | NO (stock names only; Fraser lakes geocodable by hand) | DFO spawner counts + PSC recruitment | open CSV. Terms: psc.org/terms-conditions (not read); copyright PSC |
| 3 | `sockeye` in atsalibrary (R pkg; Bristol Bay, 8 rivers, 1952-2005, + PDO) | sockeye | 8 x 54 | spawners, recruits (thousands), PDO | no (named rivers) | ADF&G via RAM Legacy | open (GitHub); subset of #1 in spirit. Not downloaded |
| 4 | Pacific Salmon Explorer data library (data.salmonwatersheds.ca) | all BC | CU level | recruits/spawner datasets exist | CU-level | DFO / PSF | open per PSF, but site returned empty to fetch, exact files NOT found. Not checked further |
| 5 | Dorner, Catalano & Peterman 2018 (Chinook covariation) | chinook | ~15-25 | R/S residuals | ? | mixed | NO public data found (no repo / data statement located) |
| - | RAM Legacy; Ruggerone & Irvine 2018 | | not checked | | | | |

## Recommendation: #1 (primary), with #2 as extension for Fraser to 2019

Why: only open source found with coordinates, >=10 stocks over >=40 yr, and two agencies' pipelines (ADF&G Alaska; DFO via Dorner 2008 for Fraser and Skeena).

```
mkdir -p salmon && cd salmon
curl -L -o sr.csv  https://knb.ecoinformatics.org/knb/d1/mn/v2/object/df35b.296.15   # 573 KB
curl -L -o loc.csv https://knb.ecoinformatics.org/knb/d1/mn/v2/object/df35b.300.6    # 6.6 KB
curl -L -o meta.xml https://knb.ecoinformatics.org/knb/d1/mn/v2/object/df35b.298.15  # EML
# Fraser extension:
curl -L -o fr_summary.csv https://www.psc.org/download/726/stock-recruit-data-sets/19741/stock-recruit-data_summary-format.csv
```
Columns, sr.csv (quoted CSV): `stock, sourceReport, BY, locationCode, species, region, area, spawners, recruits`. loc.csv (NOT quoted, header `locationCode,stock,region,lat,lon`), joined on `locationCode`. PSC: `production_stock_name, broodyr, total_broodyr_spawners, total_broodyr_EFS, recruits_ageXY..., dataset_version`.

Verified sockeye subsets with >=40 brood years:
- Bristol Bay: 8 rivers 1959-2014 (Kvichak, Naknek, Egegik, Ugashik, Wood, Igushik, Nushagak, Togiak) + Alagnak.
- Fraser: 16 stocks 1950-1998 (DFO-sourced, Dorner 2008).
- Others: Skeena 1950-1999; Chignik (Black, Chignik Lake) 1950-1996; Copper, Coghill, Eshamy (PWS); Kenai, Kasilof, Russian (Cook Inlet); Frazer Lake (Kodiak) 1966-2012.
- Common window across Bristol Bay + Fraser + Cook Inlet + PWS = about 1969-1998 (30 yr), NOT 40. 40 yr only within region groups. Bristol Bay + Chignik: 1959-1996 (38).

## Caveats (verify before use)
- Fraser rows in loc.csv carry one placeholder coordinate (49.12, -123.06) for all stocks; Fraser lake coordinates must be added by hand. Also several Alaska locations are region centroids (e.g. Nushagak 58.62,-158.59 vs Wood River 58.9,-158.5).
- Duplicate/overlapping series: Chignik appears under several names (Black, Chignik, Chignik River Watershed, Black Lake-early, Chignik Lake-late); Kvichak and "Nushagak" vs "Nuyakuk/Wood" overlap with systems. Dedupe by sourceReport.
- Mixed sourceReports (Dorner2008 3440 rows + ~15 FMS reports), different reconstruction methods: protocol differences are a confound, though this is also the desired heterogeneity.
- Pink/chum/chinook have few long series; effectively a sockeye dataset.
- I assumed package `df35b.298.15` is the latest revision (versions .2 to .15 exist); not checked for a newer one. Fraser PSC file is a different, later reconstruction than Dorner 2008, so don't mix them in one series.
- Spawner units differ (some rows in thousands?): check magnitude per stock (e.g. Adams rows 2810 vs 3287680). Use log R/S only after checking.

## What the literature says drives covariation (from search snippets and background; not read in full)
- Adkison et al. 1996 (USGS pubs 1012938): Bristol Bay productivity covaries among stocks, strongly related to climate; Fraser stocks little explained by models.
- Dorner et al. 2008 (CJFAS 65:1842): 120 pink/chum/sockeye stocks, Kalman-filter productivity; regional shared trends, weaker at larger scales.
- Dorner, Catalano, Peterman 2018 (Chinook, CJFAS 75:1082): covariation strong at regional scale, weaker at larger scales.
- Background (not fetched): PDO/North Pacific regime shifts (1976-77, 1989), early marine and SST conditions; Schindler 2010 Bristol Bay: portfolio effect from asynchronous river systems; Ruggerone and Irvine 2018: hatchery pink/chum competition in the ocean.
