# now.md: startup-grants.a

Keeper: startup-grants.a@SovereignWebsite.dinis. Session: https://claude.ai/code/session_018yvwtLncdL4FKwnYNpqFHY. Updated 2026-11-25.

## State
- Data: 17 programmes and 25 open UK competitions from official pages; 20 other addresses not yet read, each with a reason (site/data/grants.json).
- Pages: home (filters), /fit/, /graph/, /provenance/, /plan/, five design directions in two rounds (/designs/, /designs/round-2/). Live pages are on the cards design until Dinis picks.
- Vault: dev.send.sgraph.ai id req343ij, three snapshots (data, UK coverage and live screenshots, the vault's own second render). Read-only address given to Dinis, not published on the site. The same six screenshots are on /provenance/.
- Open questions for Dinis: which design; whether to publish the vault's read-only address (the site's leak scan blocks read keys); whether blocked pages may be re-read in a browser.

## Incident, 2026-11-25
- What: running `sgit vault info` in the keeper's session printed a test vault's passphrase and its read key in the keeper's own tool output.
- Where: the keeper's session output only. Nothing was committed, pushed or published.
- Fix: that test vault (id ms2ll6lf) was deleted from the server with `sgit vault delete-on-remote`, and replaced by a new vault (id req343ij) whose keys are only in files outside the repository.
- Since then: sgit output is redirected to files and only the vault id is read back.

## Next
- Done: screenshots from the live site and from the vault itself are in the vault and on /provenance/.
- Find official addresses for the pages that returned 404 (Scottish Enterprise R&D grants, UK R&D tax relief, Innovate UK funding page) and read more UK programmes.
- Refresh: see /plan/.
