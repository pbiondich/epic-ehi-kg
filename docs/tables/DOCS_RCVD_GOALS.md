# DOCS_RCVD_GOALS

> This table stores goal information received from outside sources.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 18  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | This item stores the Received Document record ID. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `GOAL_REF_ID` | VARCHAR |  | This item stores the unique reference identifier associated with the goal. |
| 6 | `GOAL_NAME` | VARCHAR |  | This item stores the name of the goal. |
| 7 | `GOAL_DESC_ID` | VARCHAR |  | This item stores the identifier of the Notes (HNO) record that stores the goal description. |
| 8 | `GOAL_CREATION_INST_DTTM` | DATETIME (Local) |  | This item stores the instant when the goal was created by the external system. |
| 9 | `GOAL_RCNT_INST_DTTM` | DATETIME (Local) |  | This item stores the instant when the value of the patient's recent progress for the goal was changed by an external system. |
| 10 | `GOAL_CONTRIBUTOR_C_NAME` | VARCHAR |  | This item stores the contributor of the goal. |
| 11 | `GOAL_SRC_DXR_CSN` | NUMERIC |  | This item stores the contact serial number of the Received Documents record that owns the instance of this goal. |
| 12 | `GOAL_RECENT_VALUE` | VARCHAR |  | This item stores the value of the patient's recent progress for the goal. |
| 13 | `GOAL_ID` | NUMERIC | FK→ | This item stores the Discrete Goals Template (IGT) record IDs that maps to the goal. |
| 14 | `GOAL_ID_GOAL_TEMPLATE_NAME` | VARCHAR |  | The goal template name. |
| 15 | `GOAL_LST_UPD_INST_DTTM` | DATETIME (UTC) |  | This item stores the last update instant in UTC for the goal. |
| 16 | `GOAL_TYPE_C_NAME` | VARCHAR | org | This item stores the goal type. |
| 17 | `GOAL_VAL_COMP_YN` | VARCHAR |  | This item stores the whether the goal recent value is compliant. |
| 18 | `GOAL_CATEGORY_C_NAME` | VARCHAR |  | This column stores the categorization of the goal. It will be null if the category cannot be determined. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `GOAL_ID` | [GOAL](GOAL.md) | name_stem | high |

