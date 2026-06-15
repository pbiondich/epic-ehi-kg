# RYAN_WHITE_PREGNANCY_DATA

> This table contains the pregnancy information from Ryan White abstractions.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RYN_WHT_PREG_CONCEPTION_DATE` | DATETIME |  | Ryan White pregnancy conception date |
| 4 | `RYN_WHT_PREG_PRENATAL_DATE` | DATETIME |  | Ryan White pregnancy prenatal care date |
| 5 | `RYN_WHT_PREG_PRENATAL_COUNT` | INTEGER |  | Ryan white pregnancy prenatal visit count |
| 6 | `RYN_WHT_PREG_ART_COUNSELED_C_NAME` | VARCHAR |  | Ryan White pregnancy Assistant Reproduction Technology (ART) counseled |
| 7 | `RYN_WHT_PREG_ART_OFFERED_C_NAME` | VARCHAR |  | Ryan White pregnancy Assistant Reproduction Technology (ART) offered |
| 8 | `RYN_WHT_PREG_ART_TAKEN_C_NAME` | VARCHAR |  | Ryan White pregnancy Assistant Reproduction Technology (ART) taken |
| 9 | `RYN_WHT_PREG_ART_DATE` | DATETIME |  | Ryan White pregnancy Assistant Reproduction Technology (ART) date |
| 10 | `RYN_WHT_PREG_OUTCOME_C_NAME` | VARCHAR |  | Ryan White pregnancy outcome |
| 11 | `RYN_WHT_PREG_DELIVERY_DATE` | DATETIME |  | Ryan White pregnancy delivery date |
| 12 | `RYN_WHT_PREG_NEWBORN_STAT_C_NAME` | VARCHAR |  | Ryan White pregnancy newborn HIV status |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

