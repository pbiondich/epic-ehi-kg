# EXT_DATA_REQ_PAYER_API

> Payer to Payer External Data Requests table.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EXT_REQ_PAYER_NAME` | VARCHAR |  | This item stores the free-text payer name, used when an external payer organization (DXO) is not available. |
| 4 | `EXT_REQ_PAYER_ORGANIZATION_ID` | NUMERIC |  | This item stores the external payer organization (DXO). |
| 5 | `EXT_REQ_PAYER_ORGANIZATION_ID_EXTERNAL_NAME` | VARCHAR |  | Organization's external name used as the display name on forms and user interfaces. |
| 6 | `OUTSIDE_COVERAGE_MEM_IDENT` | VARCHAR |  | This item stores the member ID for the coverage. |
| 7 | `EXT_DATA_REQ_STAT_C_NAME` | VARCHAR |  | This item tracks the current state of the data request for the line-level external coverage. |
| 8 | `EXT_REQ_GROUP_IDENT` | VARCHAR |  | This item stores the payer-assigned group ID. |
| 9 | `LST_COMP_REQ_UTC_DTTM` | DATETIME (UTC) |  | This item stores the time of the last completed Payer-to-Payer data exchange request. |
| 10 | `LNK_COVERAGE_ID` | NUMERIC |  | This item stores the coverage ID. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

