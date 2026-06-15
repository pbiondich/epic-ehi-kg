# PAT_ENC_RSN_VISIT

> The PAT_ENC_RSN_VISIT contains the data entered as the Reason for Visit for a clinical system encounter. Each row in this table is one reason for visit associated with a patient encounter. One patient encounter may have multiple reasons for visit; therefore, the item LINE is used to identify each reason for visit within an encounter.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | A unique serial number for this encounter. This number is unique across all patients and encounters in the system. |
| 2 | `LINE` | INTEGER | PK | The line number of the reason for visit within the encounter. |
| 3 | `ENC_REASON_ID_REASON_VISIT_NAME` | VARCHAR |  | The name of the Reason for Visit record. |
| 4 | `COMMENTS` | VARCHAR |  | The comments associated with the reason for visit entered in a clinical system exam encounter. |
| 5 | `RFV_ONSET_DT` | DATETIME |  | The onset date for reason for call/visit stored on this line. Typically this value will only be collected during call workflows such as a telephone encounter. |
| 6 | `BODY_LOC_ID` | NUMERIC |  | The body location associated with the reason for visit for this patient encounter. This column is frequently used to link to the VESSEL_DOC table. |
| 7 | `BODY_LOC_ID_RECORD_NAME` | VARCHAR |  | Stores record name (.2) |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

