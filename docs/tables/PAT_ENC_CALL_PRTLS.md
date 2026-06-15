# PAT_ENC_CALL_PRTLS

> This table lists the Protocols (LPT records) used in clinical calls.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LINE` | INTEGER | PK | The line number for the patient call protocols. |
| 2 | `PROTOCOL_ID` | NUMERIC | shared | The unique ID of the protocol used during the call. |
| 3 | `PROTOCOL_ID_PROTOCOL_NAME` | VARCHAR |  | The display name of the protocol. |
| 4 | `PROTOCOL_CONTACT` | FLOAT |  | The contact of the protocol used. |
| 5 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | A unique serial number for this encounter. This number is unique across all patients and encounters in the system. |
| 6 | `PROTOCOL_USED_YN` | VARCHAR |  | Specifies whether the protocol was used or simply viewed during the encounter. If the protocol was actually used, this item will be set to yes. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

