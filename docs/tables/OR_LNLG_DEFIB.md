# OR_LNLG_DEFIB

> The OR_LNLG_DEFIB table contains information about defibrillator power and defibrillator time applied during IntraOp.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 13  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique identifier for the line record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DEFIB_POWER` | INTEGER |  | Document the power settings for the defibrillator. |
| 4 | `DEFIB_APPLIED_DTTM` | DATETIME (UTC) |  | Document when the defibrillator was applied to the patient. |
| 5 | `DEFIB_APPLIED_DT` | DATETIME |  | Stores the date defibrillation was performed during surgery. |
| 6 | `DEFIB_APPLIED_TM` | DATETIME (UTC) |  | Stores the time defibrillation was performed during surgery. |
| 7 | `DEFIB_MODIFIER_C_NAME` | VARCHAR | org | Stores the modification made to the defibrillator. |
| 8 | `DEFIB_SERIAL_NUMBER` | NUMERIC |  | This item stores the defibrillator serial number. |
| 9 | `DEFIB_PAD_SIZE` | NUMERIC |  | This item stores the defibrillator pad size. |
| 10 | `DEFIB_PAD_LOCATION_C_NAME` | VARCHAR | org | This item stores the defibrillator pad location. |
| 11 | `DEFIB_END_TM` | DATETIME (Local) |  | This item stores the time defibrillation was ended. |
| 12 | `OPERATED_BY_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 13 | `DEFIB_MODE_C_NAME` | NUMERIC | org | This item documents the mode the defibrillator is being run in. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

