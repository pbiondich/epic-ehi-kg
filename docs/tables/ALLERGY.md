# ALLERGY

> The ALLERGY table contains information about the allergies noted in your patients' clinical system records. You would use this table if you wanted to report on the number of patients who are allergic to sulfa drugs, for example. To determine the allergic reaction, link to the ALLERGY_REACTIONS table.

**Primary key:** `ALLERGY_ID`  
**Columns:** 19  
**Org-specific columns:** 4  
**Joined by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ALLERGY_ID` | NUMERIC | PK | The unique ID used to identify the allergy record. |
| 2 | `ALLERGEN_ID` | NUMERIC | FK→ | The unique ID assigned to the allergen (Agent) record. |
| 3 | `ALLERGEN_ID_ALLERGEN_NAME` | VARCHAR |  | The name of the allergen record. |
| 4 | `REACTION` | VARCHAR |  | This column contains the free text reaction comments. The actual reaction category value responses are stored in the ALLERGY_REACTIONS table which is linked via the ALLERGY_ID columns in both tables. |
| 5 | `DATE_NOTED` | DATETIME |  | The date the patient made it known that they had experienced an allergic reaction in calendar format. |
| 6 | `ENTRY_USER_ID` | VARCHAR |  | The unique ID of the clinical system user who entered this allergy into the patient’s record. This ID may be encrypted. NOTE: If an allergy record is edited/updated, this will show the most recent change user ID. |
| 7 | `ENTRY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `SEVERITY_C_NAME` | VARCHAR | org | The allergy type category value, describing the nature or character of the allergy (i.e. systemic, topical, etc.). NOTE: This field refers to the field called "TYPE" in the Allergy module in clinical system. |
| 9 | `ALLERGY_SEVERITY_C_NAME` | VARCHAR |  | This item stores the severity of an allergy. |
| 10 | `ALRGY_STATUS_C_NAME` | VARCHAR |  | The status category number for this allergy record. The status can be active or deleted. |
| 11 | `ALRGY_DLET_RSN_C_NAME` | VARCHAR | org | Stores the reason for deleting an allergy. |
| 12 | `ALRGY_DLT_CMT` | VARCHAR |  | This item contains the comment about why an allergy was deleted from a patient's chart. |
| 13 | `CONTRA_EXP_DT` | DATETIME |  | The date that the contraindication will expire. |
| 14 | `ALRGY_ENTERED_DTTM` | DATETIME (Local) |  | The date and time the allergy was entered into the patient's record using a calendar format. NOTE: If an allergy record is edited/updated this will show the most recent change. |
| 15 | `ALLERGY_CERTAINTY_C_NAME` | VARCHAR | org | The certainty that this allergen is a risk to the patient. |
| 16 | `ALLERGY_SOURCE_C_NAME` | VARCHAR | org | The source of information for an allergy. |
| 17 | `ALLERGY_PAT_CSN` | NUMERIC | FK→ | The patient contact corresponding to the patient encounter in which this allergy was edited. |
| 18 | `ALLERGY_NOTED_DATE_ACCURACY_C_NAME` | VARCHAR |  | The noted date accuracy of an allergy determines the accuracy of the noted date specified in DATE_NOTED. A value of 1-Year indicates that the specific day in the DATE_NOTED column is accurate to the year and not to the specific day. Similarly a value of 2-Month indicates that it is accurate to the month. A value of 3-Exact Date or an empty value indicates that the corresponding value in DATE_NOTED column is accurate to that day. |
| 19 | `ALRGY_TRANSMTL_UTC_DTTM` | DATETIME (UTC) |  | This item is used to store the last successful instant of transmittal to an external allergies list. It is currently only used for the SFM PLL drug reactions list in Norway. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ALLERGEN_ID` | [CL_ELG](CL_ELG.md) | sole_pk | high |
| `ALLERGY_PAT_CSN` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

## Joined in — referenced by (1)

| From | Column | Confidence |
|------|--------|------------|
| [ALLERGY_REACTIONS](ALLERGY_REACTIONS.md) | `ALLERGY_ID` | high |

