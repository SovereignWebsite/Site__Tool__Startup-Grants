# grants.json schema (version 1.0)

File: https://startup-grants.tool.sovereignweb.site/data/grants.json

Public data for reuse, including by PrompTugal News. Each programme is written by the site's keeper from the programme's own official public page. The Notion database "European Startup Grant Programs (2026 Edition)" was used only as the starting list of names and official links, and none of its text was copied.

## Rules for every field

- A field the official page does not state is an empty string or empty list. Nothing is estimated.
- `official_url` is the page the entry was written from. `date_checked` is the day it was read (YYYY-MM-DD).
- Amounts and rates are given as stated, in text. There is no computed number.

## Top level

| Key | Meaning |
| --- | --- |
| `schema_version` | This schema's version, "1.0". |
| `generated` | Date the file was built. |
| `credits.starting_list` | The Notion starting list: `name`, `url`, `used_for`. |
| `vocabularies` | `stages`, `sectors`, `countries`: code to plain label. |
| `programmes` | Array of programmes (below). |
| `not_yet_read` | Starting-list items not yet written up, each with `name`, `country`, `starting_list_url` and a plain `reason`. |

## Programme

| Key | Type | Meaning |
| --- | --- | --- |
| `id` | string | Stable slug. |
| `name` | string | Programme name as the official page gives it. |
| `organisation` | string | Who runs it. |
| `countries` | string[] | Codes from `vocabularies.countries` (ISO 3166 where one exists; `EU` for EU-wide; `GB-NIR` for Northern Ireland). |
| `geography` | string | `national`, `regional` or `eu`. |
| `kind` | string | `programme`, `route` (a way to submit an idea) or `tax-relief` (for investors). |
| `stages` | string[] | Codes from `vocabularies.stages`. |
| `sectors` | string[] | Codes from `vocabularies.sectors`. `any` means the page says all fields. |
| `funding_amount_text` | string | Amount as stated. |
| `funding_rate_text` | string | Share of costs as stated. |
| `how_to_apply` | string | One plain sentence. |
| `deadline_type` | string | `fixed`, `rolling`, `annual`, `windows` or `not-stated`. |
| `deadline_text` | string | Deadline as stated, with caveats. |
| `deadline_dates` | string[] | ISO dates stated on the page, where there are clear ones. |
| `eligibility_notes` | string | Short notes in the keeper's words. |
| `official_url` | string | Official page the entry was written from. |
| `further_official_urls` | string[] | Other official pages read for the entry. |
| `date_checked` | string | YYYY-MM-DD. |
| `notes` | string | Anything a reader should know, such as a page that contradicts itself. |
| `in_starting_list` | boolean | Whether the programme was in the Notion starting list. |

Deadlines change. Check `official_url` before acting.
