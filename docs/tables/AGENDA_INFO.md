# AGENDA_INFO

> Table of no-add single row information about visit agendas (VANs).

**Primary key:** `AGENDA_ID`  
**Columns:** 3  
**Joined by:** 9 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `AGENDA_ID` | NUMERIC | PK | The unique identifier (.1 item) for the agenda record. |
| 2 | `CREATION_UTC_DTTM` | DATETIME (UTC) |  | UTC instant that the record was first created |
| 3 | `LINKED_PAT_ENC_CSN_ID` | NUMERIC | FK→ | Patient contact serial number this agenda is associated with |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `LINKED_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

## Joined in — referenced by (9)

| From | Column | Confidence |
|------|--------|------------|
| [AGENDA_CLINICIAN_TOPICS](AGENDA_CLINICIAN_TOPICS.md) | `AGENDA_ID` | high |
| [AGENDA_HX_EMP_TOPICS](AGENDA_HX_EMP_TOPICS.md) | `AGENDA_ID` | high |
| [AGENDA_HX_NET_EMP_USERS](AGENDA_HX_NET_EMP_USERS.md) | `AGENDA_ID` | high |
| [AGENDA_HX_NET_TOPICS](AGENDA_HX_NET_TOPICS.md) | `AGENDA_ID` | high |
| [AGENDA_HX_NET_WPR_USERS](AGENDA_HX_NET_WPR_USERS.md) | `AGENDA_ID` | high |
| [AGENDA_HX_REM_EMP_TOPICS](AGENDA_HX_REM_EMP_TOPICS.md) | `AGENDA_ID` | high |
| [AGENDA_HX_WPR_TOPICS](AGENDA_HX_WPR_TOPICS.md) | `AGENDA_ID` | high |
| [AGENDA_PAT_TOPICS](AGENDA_PAT_TOPICS.md) | `AGENDA_ID` | high |
| [AGENDA_RMV_CLIN_TOPICS](AGENDA_RMV_CLIN_TOPICS.md) | `AGENDA_ID` | high |

