# learnings.md: startup-grants.a

- A new page fails the deploy at share-check unless it has the 14 Open Graph and Twitter tags. Run `bash tools/check.sh` before every push; it runs every step of pages.yml.
- The CI axe check once stopped at one level under designs/; a fixed version now checks any depth. Also run axe in dark mode and in selected states, which CI does not.
- A deploy run has a build job first; the deploy job appears after it, so a missing deploy job soon after a push is not a failure.
- `sgit vault info` prints the passphrase. Redirect sgit output to a file and read back only the vault id. A read key (sgit_private_read_) is blocked from every published file by the leak scan; that is the owner's decision, not an edit to make.
- Do not work round a permission refusal (a browser re-read, printing a key file). Stop, say what was blocked and why, and carry on with the rest.
- Web-fetch sub-agents summarise pages; they do not give verbatim text. Keep amounts, rates and dates as short quotes and say in provenance who read the page.
- A 403, a bot check and a JS-only page are gaps, not facts. Never fill them from the Notion list, a research brief or memory.
- The Notion starting list is names and links only. A ChatGPT brief said it was private; it was public. Treat briefs as leads.
- PrompTugal's own provenance shape (read_by, how_read, source_license, file) is the format to match so PrompTugal News can reuse the data.
- Stylesheets get a content hash in the link (?v=...) so a cached copy is never served at the same address.
- Pages generated from the /start/ template lose the picker; run tools/add-picker.py after tools/build-pages.py.
