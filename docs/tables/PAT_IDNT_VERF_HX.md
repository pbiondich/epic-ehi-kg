# PAT_IDNT_VERF_HX

> Stores information pertaining to a Patient Identifier verification query.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | Patient ID for the patient whose Patient Identifier is being verified |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PAT_IDNT_MSG_S_TM` | DATETIME (UTC) |  | Instant that verification query was sent |
| 4 | `PAT_IDNT_MSG_R_TM` | DATETIME (UTC) |  | Instant that verification response was received |
| 5 | `PAT_IDNT_MSG_ID` | VARCHAR |  | Record ID in General Use Notes (HNO) for items sent message (I HNO 16120) and received message (I HNO 16125). |
| 6 | `PAT_IDNT_RESP` | VARCHAR |  | This item stores the query response for a Patient Identifier verification query |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

