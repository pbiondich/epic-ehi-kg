# CL_PAT_EDU_OS

> This table stores the Patient Education information that is linked to a specific patient encounter and changes from one patient encounter to the next such as the Patient Education note for each encounter and when Patient Education was last documented for each encounter.

**Primary key:** `PED_ID`, `CONTACT_DATE_REAL`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PED_ID` | NUMERIC | PK FK→ | The Unique ID for the Patient Education Record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 3 | `CONTACT_DATE` | DATETIME |  | The contact date in external format. |
| 4 | `CONTACT_NUM` | INTEGER |  | The contact number for the patient education record contact. |
| 5 | `PAT_CSN` | NUMERIC | FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 6 | `EDUCATION_NOTE_ID` | VARCHAR |  | The unique ID of the note that is associated with this patient education contact. |
| 7 | `INSTANT_OF_ENTRY` | DATETIME (Attached) |  | Date/Time stamp for the instance when the when data was entered in a patient education contact. |
| 8 | `INSTANT_OF_EDIT` | DATETIME (Attached) |  | Date/Time stamp for the instance when the when data was edited in a patient education contact. |
| 9 | `LAST_TAUGHT_AT` | DATETIME (Local) |  | The instant when the patient education was last taught. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_CSN` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `PED_ID` | [CL_PAT_EDU_NS](CL_PAT_EDU_NS.md) | sole_pk | high |

