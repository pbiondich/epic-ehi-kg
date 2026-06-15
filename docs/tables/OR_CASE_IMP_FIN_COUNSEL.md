# OR_CASE_IMP_FIN_COUNSEL

> Stores the implant financial counseling information.

**Primary key:** `CASE_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CASE_ID` | VARCHAR | PK shared | The unique identifier for the case request record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `IMPLANT_INV_ITEM_ID` | VARCHAR |  | Stores the supply record for a requested implant. |
| 4 | `IMPLANT_INV_ITEM_ID_SUPPLY_NAME` | VARCHAR |  | The name of the inventory item. |
| 5 | `IMPLANT_CLASS_C_NAME` | VARCHAR | org | Stores the class of the implant. |
| 6 | `PATIENT_REQUESTED_C_NAME` | VARCHAR | org | Stores if the implant was requested by the patient. |
| 7 | `IMPLANT_CLIN_CMTS` | VARCHAR |  | Stores the comment for the implant. |
| 8 | `CLINICAL_IND_C_NAME` | VARCHAR | org | Stores the clinical indication for the requested implant. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

