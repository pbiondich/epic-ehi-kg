# FAMILY_HX

> The FAMILY_HX table contains data recorded in the family history contacts entered in the patient's chart during a clinical system encounter. Note: This table is designed to hold a patient's history over time; however, it is most typically implemented to only extract the latest patient history contact.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 12  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LINE` | INTEGER | PK | The line number to identify the family history contact within the patient’s record. NOTE: Each line of history is stored in enterprise reporting as its own record; a given patient may have multiple records (identified by line number) that reflect multiple lines of history. |
| 2 | `MEDICAL_HX_C_NAME` | VARCHAR | org | The category value associated with the Problem documented in the patient’s family history. |
| 3 | `MEDICAL_OTHER` | VARCHAR |  | The custom reason for visit or problem entered when the clinical system user chooses "Other" as a family history problem. NOTE: The comment is stored in the same item as MEDICAL_HX_C but is delimited from the response "Other" by the comment character, "[". The EPIC_GET_COMMENT function returns everything after the comment character. |
| 4 | `COMMENTS` | VARCHAR |  | Free-text comments entered with this problem. This column may be hidden in a public enterprise reporting view. |
| 5 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | A unique serial number for this encounter. This number is unique across all patients and encounters in the system. |
| 6 | `FAM_HX_SRC_C_NAME` | VARCHAR | org | This item contains the source of information for a patient's family medical history. |
| 7 | `RELATION_C_NAME` | VARCHAR | org | This is the category value associated with the family member who has or had this problem. An example might be sister, brother, or mother. |
| 8 | `FAM_RELATION_NAME` | VARCHAR |  | This is the first and/or last name of the patient's family member. This column is free-text and is meant to be used together with the RELATION_C category to form a unique key for the family member. If no name is entered this column will display an abbreviation of the family relation type beginning with ##. |
| 9 | `AGE_OF_ONSET` | NUMERIC |  | This item contains the age of onset of the patient's family member that is documented with a history of a problem. |
| 10 | `FAM_MED_REL_ID` | INTEGER |  | This item contains the unique ID of the patient's family member relationship for medical history. |
| 11 | `FAM_MEDICAL_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 12 | `AGE_OF_ONSET_END` | NUMERIC |  | When the age of onset for a family member's history of a problem is documented as an age range, this item contains the age at the end of the range. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

