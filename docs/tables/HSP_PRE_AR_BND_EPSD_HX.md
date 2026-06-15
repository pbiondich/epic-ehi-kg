# HSP_PRE_AR_BND_EPSD_HX

> This table contains bundled episode history for Hospital Billing temporary transactions. This table is limited to charge temporary transactions that have not yet been posted to the account.

**Primary key:** `HTT_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HTT_ID` | NUMERIC | PK FK→ | The unique identifier for the transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HTT_LINE` | INTEGER |  | Holds the line number in the charge data related group that this line corresponds to. |
| 4 | `ACTION_DTTM` | DATETIME (UTC) |  | The date and time that this transaction was linked/unlinked to the bundled episode. |
| 5 | `EPISODE_ID` | NUMERIC | FK→ | Holds bundled episode records linked to this transaction. |
| 6 | `ACTION_C_NAME` | VARCHAR |  | The current state of this transaction and episode, whether it is linked or unlinked. |
| 7 | `SOURCE_C_NAME` | VARCHAR |  | The source of the link or unlink of this bundled episode to this transaction. |
| 8 | `USER_ID` | VARCHAR | FK→ | The user who performed the link or unlink of this episode to the transaction line. |
| 9 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EPISODE_ID` | [EPISODE](EPISODE.md) | name_stem | high |
| `HTT_ID` | [HSP_PRE_AR_SESSION](HSP_PRE_AR_SESSION.md) | sole_pk | high |
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

