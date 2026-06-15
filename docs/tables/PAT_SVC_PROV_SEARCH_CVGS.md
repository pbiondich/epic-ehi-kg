# PAT_SVC_PROV_SEARCH_CVGS

> Related multi table for the patient coverage list store in the patient choice list metadata.

**Primary key:** `PAT_ENC_CSN_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this contact. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this contact. |
| 4 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 5 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 6 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 7 | `PAT_COVERAGE_ID` | NUMERIC |  | The list of coverages that were used to provide insurance acceptance information for service providers on the patient choice list. Taken from the hospital account filing order. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

