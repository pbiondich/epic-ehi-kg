# OR_IMP_TISSUE_SOLN

> Tissue Preparation Solution Categories.

**Primary key:** `IMPLANT_ID`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMPLANT_ID` | VARCHAR | PK shared | The unique identifier for the implant record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PREP_SOLUTION_C_NAME` | VARCHAR | org | Solution used in tissue preparation. |
| 4 | `PREP_SOLN_SOAK_DURA` | INTEGER |  | The length of time each implant was prepared and soaked in different solutions per protocol. |
| 5 | `PREP_SOLN_MFR_C_NAME` | VARCHAR | org | This item is used to document the manufacturer of the tissue preparation solution. |
| 6 | `PREP_SOLN_SERIAL_NM` | VARCHAR |  | This item is used to document the tissue preparation solution serial number. |
| 7 | `TISSUE_PREP_START_DTTM` | DATETIME (Local) |  | This column stores the tissue prep start time. |
| 8 | `TISSUE_PREP_END_DTTM` | DATETIME (Local) |  | This column stores the tissue prep end time. |
| 9 | `PREP_SOLN_RINSE_DURATION` | INTEGER |  | Stores the length of time each implant is rinsed in different solutions. |
| 10 | `PREP_SOLN_QTY` | NUMERIC |  | Stores the number of tissue prep solution containers that were used. |
| 11 | `PREP_SOLN_TEMP` | VARCHAR |  | This item stores the temperature for the tissue preparation solution. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

