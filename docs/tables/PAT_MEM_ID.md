# PAT_MEM_ID

> This table is used to link patients to a member ID associated with one of the patients coverages.

**Primary key:** `PATIENT_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PATIENT_ID` | VARCHAR | PK | This is the Epic Patient ID. |
| 2 | `LINE` | INTEGER | PK | The line number. |
| 3 | `MEMBER_ID` | VARCHAR |  | This is the patient's Member ID associated with a carrier. You can use this number to look up the patient and his/her family members. |
| 4 | `LONG_MEMBER_ID` | VARCHAR |  | This is the patient's Member ID preceded by a chart or Medical Record Number. This column contains the data that is stored in the Member ID super item (EPT 5001). |
| 5 | `MEM_ID_CARRIER_ID` | VARCHAR |  | Member ID maintained by a carrier |
| 6 | `MEM_ID_CARRIER_ID_CARRIER_NAME` | VARCHAR |  | The name of the carrier record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

