# UCL_BUNDLED_EPISODE

> Information about the episodes related to a charge line.

**Primary key:** `UCL_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `UCL_ID` | VARCHAR | PK FK→ | The unique identifier for the charge line record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `LAST_UPDT_INST_UTC_DTTM` | DATETIME (UTC) |  | Stores the instant the bundled episode was updated on this charge line. |
| 4 | `EPISODE_ID` | NUMERIC | FK→ | The bundled episode whose link is defined on this line |
| 5 | `LINK_STATUS_C_NAME` | VARCHAR |  | This indicates whether this episode is linked to the universal charge line. |
| 6 | `LINK_SOURCE_C_NAME` | VARCHAR |  | Indicates whether it's a user-override or something different that set the link. |
| 7 | `LINK_USER_ID` | VARCHAR |  | Indicates the user who set the episode status for the charge line. |
| 8 | `LINK_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EPISODE_ID` | [EPISODE](EPISODE.md) | name_stem | high |
| `UCL_ID` | [CLARITY_UCL](CLARITY_UCL.md) | sole_pk | high |

