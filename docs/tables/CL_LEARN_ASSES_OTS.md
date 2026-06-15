# CL_LEARN_ASSES_OTS

> It stores information that changes over time, such as patient contact date, whether or not the assessment was verified, and the last time assessment was edited or entered.

**Primary key:** `LEARNING_ASSMT_ID`, `CONTACT_DATE_REAL`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LEARNING_ASSMT_ID` | NUMERIC | PK FK→ | The unique ID for the patient learning assessment record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 3 | `CONTACT_DATE` | DATETIME |  | The contact date in external format. |
| 4 | `CONTACT_NUM` | VARCHAR |  | The contact number for the contact. |
| 5 | `PAT_DAT` | VARCHAR |  | Patient visit date for the patient learning assessment record contact. |
| 6 | `EPT_CSN` | NUMERIC |  | The unique contact serial number of the patient contact to which this patient learning assessment record is associated. |
| 7 | `VERIFIED_YN` | VARCHAR |  | Indicates whether the assessment is verified for this contact. |
| 8 | `INSTANT_OF_ENTRY` | DATETIME (Attached) |  | The date and time when the learning assessment was entered. |
| 9 | `INSTANT_OF_EDIT` | DATETIME (Attached) |  | The date and time when the learning assessment was edited. |
| 10 | `END_CONT_DATE_REAL` | FLOAT |  | This is a numeric representation of the date of the last encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 11 | `IS_DELETED_YN` | VARCHAR |  | Indicates whether the assessment is deleted for this contact. Y indicates that the learning assessment is deleted; N or a null value indicates that the learning assessment is not deleted. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `LEARNING_ASSMT_ID` | [CL_LEARN_ASSESS_NS](CL_LEARN_ASSESS_NS.md) | sole_pk | high |

