# now.md: startup-grants.a

Keeper: startup-grants.a@SovereignWebsite.dinis. Session: https://claude.ai/code/session_018yvwtLncdL4FKwnYNpqFHY. Updated 2026-11-25. State: handing over (see restart.md).

## State
- Data: 17 programmes and 25 open UK competitions from official pages, each with its link and date checked; 20 other addresses not yet read, each with a reason ([site/data/grants.json](site/data/grants.json), schema in [site/data/SCHEMA.md](site/data/SCHEMA.md)).
- Pages: home (filters), /fit/ (compare answers with stated criteria), /graph/, /provenance/ (with six screenshots), /plan/, and five design directions in two rounds (/designs/, /designs/round-2/). The "Choose a design" picker is on every page. Live pages use the cards layout until Dinis picks.
- Vault: dev.send.sgraph.ai, id req343ij, three snapshots. Its read-only address is not linked from the site (the leak scan blocks read keys). It is held in the old container only; see restart.md.
- Checks: `bash tools/check.sh` passes (build, share-check, quality, html-validate, axe at any depth). Site was at v0.1.18 (b8663a4) when last checked, then eefa5a7 and cd176bf were pushed.

## Open, waiting on Dinis
1. Which design to pick (recommended: 5, the deadline timeline with cards; a.design reviewed two rounds and agrees).
2. How to deliver the vault's read-only address, and whether to publish it.
3. Whether blocked official pages (403, bot check) may be re-read in a browser.

## Open work
- Gaps listed on the home page and /provenance/: 404 or refused addresses (French Tech Rise, EXIST research transfer, ZIM, VLAIO, Eurostars, Bpifrance i-Nov and i-Lab, FFG, Innovasjon Norge, CDTI Neotec), hubs not drilled into (Vinnova, EIT, ESA BIC, UKRI), and UK items not found on official pages (Smart grants, Launchpad, Biomedical Catalyst, Innovation Loans; Scottish Enterprise R&D grants and R&D tax relief addresses returned 404; Wales names no scheme).
- Refresh: designed on /plan/, not built.

## Incident, 2026-11-25
- What: `sgit vault info` printed a test vault's passphrase and its read key in the keeper's own tool output.
- Where: the keeper's session output only. Nothing was committed, pushed or published.
- Fix: that test vault (id ms2ll6lf) was deleted from the server with `sgit vault delete-on-remote`, and replaced by a new vault (id req343ij) whose keys are only in files outside the repository.
- Since then: sgit output is redirected to files and only the vault id is read back.
