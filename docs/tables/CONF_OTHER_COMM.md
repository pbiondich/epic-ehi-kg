# CONF_OTHER_COMM

> This table stores information about the miscellaneous confidential communication devices that can be used to reach the patient. Examples include Mobile, Home Phone, and Work Phone.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CONF_COMM_DEVI_C_NAME` | VARCHAR | org | The confidential communication device type. Examples include Mobile, Home Phone, and Work Phone. |
| 4 | `CONF_COMM_NUMB` | VARCHAR |  | The confidential communication number that corresponds to the device type returned in the column CONF_COMM_DEVI_C. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

