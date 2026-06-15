# REQ_ALL_MAIN

> The REQ_ALL_MAIN table contains basic information about Requisitions, Cases, and External System Patient Demographics.

**Primary key:** `REQUISITION_ID`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REQUISITION_ID` | NUMERIC | PK shared | The unique identifier for the requisition, case, or external system patient demographics record. |
| 2 | `REQ_TYPE_C_NAME` | VARCHAR |  | The type category ID for the requisition, case, or external system patient demographics record. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 4 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | The unique contact serial number (CSN) of the patient. If you use IntraConnect, this is the Unique Contact Identifier (UCI). For requisitions, this is the CSN for the Lab Requisition encounter associated with the requisition. For cases, this is the CSN for the encounter linked to the first order on the case. |
| 5 | `RQG_GROUPER_ID` | NUMERIC | FK→ | The unique ID of the requisition grouper associated with this record. |
| 6 | `CANCELED_YN` | VARCHAR |  | Indicates whether the record is canceled. 'Y' indicates that the record is a canceled requisition or case. 'N' indicates that the record is not canceled. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |
| `RQG_GROUPER_ID` | [RQG_DB_MAIN](RQG_DB_MAIN.md) | sole_pk | high |

