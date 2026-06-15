# ACUITY_RULE_SCORE

> Extracted table for rule-related data from scoring system data filed to RDI.

**Primary key:** `REGISTRY_DATA_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `RULE_ID` | VARCHAR | shared | The unique ID of the CER rule used in the scoring system. |
| 5 | `RULE_ID_RULE_NAME` | VARCHAR |  | The name of the rule. |
| 6 | `RULE_SCORE` | NUMERIC |  | The score from the rule in RULE_ID. |
| 7 | `RULE_TYPE_C_NAME` | VARCHAR | org | The rule type category ID for the scoring system rule in RULE_ID. |
| 8 | `SCORE_CALC_UTC_DTTM` | DATETIME (UTC) |  | The date and time when the rule score is filed in UTC. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

