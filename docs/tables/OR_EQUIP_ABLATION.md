# OR_EQUIP_ABLATION

> This table stores details about ablation usage during surgery.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the line record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ABLATION_REGION_C_NAME` | VARCHAR | org | This column stores the area of the body where the ablation was performed. |
| 4 | `SENSORY_RESPONSE` | NUMERIC |  | This column stores the stimulation level when the patient started feeling electric impulses. |
| 5 | `MOTOR_RESPONSE` | NUMERIC |  | This column stores the stimulation level when the patient started showing muscular reactions. |
| 6 | `INITIAL_IMPEDANCE` | NUMERIC |  | This column stores the impedence measured prior to applying the catheter to the patient. |
| 7 | `IMPEDANCE` | NUMERIC |  | This column stores the impedance measured after applying the catheter to the patient. |
| 8 | `POWER` | NUMERIC |  | This column stores the power level used for ablation. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

