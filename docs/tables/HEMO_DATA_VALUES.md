# HEMO_DATA_VALUES

> This table contains the hemodynamic measurement values collected during an invasive procedure performed in a catheterization lab. The table only includes the values selected by the performing physician in Study Review for the result report.

**Primary key:** `FINDING_ID`, `LINE`  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the finding record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HEMO_FIELD_FORM_COMP_ID_NESTCOMP_NAME` | VARCHAR |  | The record name for the component. |
| 4 | `HEMO_DISPLAY_VALUE` | VARCHAR |  | Stores a string representation of the hemodynamic data value including all components. |
| 5 | `HEMO_PHASE_KEY` | VARCHAR |  | Identifies the phase of the procedure when this value was measured. The value in this phase key item corresponds to the HEMO_PHASES_KEY column in the HEMO_DATA_PHASES table. |
| 6 | `HEMO_SOURCE_C_NAME` | VARCHAR |  | Indicates how the value was entered. |
| 7 | `HEMO_VALUE` | NUMERIC |  | Numeric item for the value for simple numeric fields. |
| 8 | `HEMO_SYSTOLIC` | INTEGER |  | Numeric item for the systolic portion of a pressure field. |
| 9 | `HEMO_DIASTOLIC` | INTEGER |  | Numeric item for the diastolic portion of a pressure field. |
| 10 | `HEMO_MEAN` | INTEGER |  | Numeric item for the mean portion of a pressure field. |
| 11 | `HEMO_END_DIASTOLIC` | INTEGER |  | Numeric item for the end diastolic portion of a pressure field. |
| 12 | `HEMO_FIELD_DAT` | FLOAT |  | Stores the contact for the field definition of this hemodynamic measurement value. |
| 13 | `HEMO_FIELD_DATE_REAL` | FLOAT |  | Stores the unique contact date in decimal format for the field definition of this hemodynamic measurement value in this row. This corresponds to the CONTACT_DATE_REAL column in the NESTED_FORM_COMPONENT_VER table. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

