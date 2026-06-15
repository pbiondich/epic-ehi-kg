# OUT_MED_ADHERE_INFO_HX

> This table stores historical medication fill information for the patient. Each row represents a medication.

**Primary key:** `REGISTRY_DATA_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 22  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `OUTCOME_KEY_MED_ADH_HX` | INTEGER |  | The unique outcome key that links medication data to the rest of the outcome data. |
| 5 | `OUTCOME_MED_NAME_HX` | VARCHAR |  | The medication name relevant to an adherence measure. |
| 6 | `OUTCOME_MED_HX_NDC_ID` | VARCHAR |  | The networked NDC record ID. |
| 7 | `OUTCOME_MED_HX_NDC_ID_NDC_CODE` | VARCHAR |  | The external code for the National Drug Code (NDC). An NDC represents packages of medications. |
| 8 | `OUTCOME_MED_FIRST_FILL_HX_DATE` | DATETIME |  | The date this medication was first filled. |
| 9 | `OUTCOME_MED_LAST_FILL_HX_DATE` | DATETIME |  | The most recent fill date for the medication. |
| 10 | `OUTCOME_MED_NEXT_FILL_HX_DATE` | DATETIME |  | The expected next fill date for the medication. |
| 11 | `OUTCOME_MED_DAYS_SUPPLY_HX` | INTEGER |  | The number of days that the latest medication fill should last if taken as prescribed. |
| 12 | `OUT_HX_MED_ELIG_EXT_DAY_SUP_C_NAME` | VARCHAR | org | Whether the patient is eligible for a larger medication supply. |
| 13 | `OUTCOME_MED_REFILLS_REMAIN_HX` | INTEGER |  | The number of refills a patient can obtain before their provider must authorize more. |
| 14 | `OUTCOME_MED_PRESCRIBER_NAME_HX` | VARCHAR |  | The name of the provider who prescribed the medication. |
| 15 | `OUTCOME_MED_PRESCRIBER_NPI_HX` | VARCHAR |  | The National Provider Identifier (NPI) of the provider who prescribed the medication. |
| 16 | `OUTCOME_MED_PRESCRIBER_PH_HX` | VARCHAR |  | The phone number of the provider who prescribed the medication. |
| 17 | `OUTCOME_MED_PHARMACY_NAME_HX` | VARCHAR |  | The name of the pharmacy where the patient obtained the medication. |
| 18 | `OUTCOME_MED_PHARMACY_NPI_HX` | VARCHAR |  | The National Provider Identifier (NPI) of the pharmacy where the patient obtained the medication. |
| 19 | `OUTCOME_MED_PHARMACY_PHONE_HX` | VARCHAR |  | The phone number of the pharmacy where the patient obtained the medication. |
| 20 | `OUTCOME_HX_MED_PHARMACY_SRC_C_NAME` | VARCHAR | org | The method of distribution used by the pharmacy where the patient obtained the medication. |
| 21 | `OUTCOME_MED_PREF_PHARM_HX_YN` | VARCHAR |  | Whether the pharmacy where the patient obtained the medication is a preferred pharmacy for the payer. Patients often have lower out-of-pocket costs at preferred pharmacies. |
| 22 | `OUTCOME_MED_HX_RAW_NDC` | VARCHAR |  | The raw NDC string for the medication associated with the gap. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

