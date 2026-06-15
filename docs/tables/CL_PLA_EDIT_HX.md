# CL_PLA_EDIT_HX

> Enterprise reporting table that contains the editing history of learning assessment contacts. It identifies the user who edited the assessment.

**Primary key:** `LEARNING_ASSMT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LEARNING_ASSMT_ID` | NUMERIC | PK FK→ | The unique ID for the patient learning assessment record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 3 | `LINE` | INTEGER | PK | The Line Counter for the edit instance and editing user of the patient learning assessment record. |
| 4 | `CONTACT_DATE` | DATETIME |  | The contact date in external format. |
| 5 | `EDIT_USER_ID` | VARCHAR |  | Record ID for the user who edited the patient learning assessment record contact. It is related to the Edit Instance and is stored in internal ID format. Points to EMP user record. |
| 6 | `EDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `EDIT_INSTANCE` | DATETIME (Local) |  | Date/Time stamp for instance of editing the patient learning assessment record contact. It is related to the Edit User. |
| 8 | `END_CONT_DATE_REAL` | FLOAT |  | This is a numeric representation of the date of the last encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 9 | `EDIT_IS_DELETED_YN` | VARCHAR |  | Indicates whether the learning assessment was deleted in this line in the learning assessment's edit history. Y indicates that the learning assessment was deleted; N or a null value indicates that the learning assessment was not deleted. |
| 10 | `EDIT_DEL_COMMENT` | VARCHAR |  | The comments entered by the user who deleted the learning assessment. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `LEARNING_ASSMT_ID` | [CL_LEARN_ASSESS_NS](CL_LEARN_ASSESS_NS.md) | sole_pk | high |

