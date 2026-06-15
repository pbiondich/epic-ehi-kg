# RYAN_WHITE_MED_DATA

> Ryan White CAREWare Medication Import Table.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 14  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RW_MED_ORDER_ID` | NUMERIC |  | Stores the Medication Order Id for the Medication Import Table |
| 4 | `RW_MED_UNITS` | NUMERIC |  | Ryan White Medication Units |
| 5 | `RW_MED_STRENGTH` | INTEGER |  | Ryan White Medication Strength |
| 6 | `RW_MED_FREQUENCY_C_NAME` | VARCHAR | org | Ryan White Medication Frequency |
| 7 | `RW_MED_START_DATE` | DATETIME |  | Ryan White Medication Start Date |
| 8 | `RW_MED_END_DATE` | DATETIME |  | Ryan White Medication End Date |
| 9 | `RW_MED_INDICATION_C_NAME` | VARCHAR | org | Ryan White Medication Indication |
| 10 | `RW_MED_PRPHYLAXIS_C_NAME` | VARCHAR | org | Ryan White Medication Prophylaxis |
| 11 | `RW_MED_DIS_REASON_C_NAME` | VARCHAR | org | Ryan White Medication discontinue reason. Not the same concept as an Epic discontiunue reason |
| 12 | `RW_MED_COMMENT` | VARCHAR |  | Ryan White Medication Comment |
| 13 | `RW_MED_INSTRUCTIONS` | VARCHAR |  | Ryan White Medication Instructions |
| 14 | `RW_MED_MEDICATION_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

