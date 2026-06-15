# OUTCOME_MED_ADHERE_INFO

> This table will hold med adherence information around the medications associated with an outcome.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 22  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `OUTCOME_KEY_MED_ADH` | INTEGER |  | This item stores the outcome's key. This key is unique for an outcome on a particular RDI record. This item is used to link the current outcomes group (I RDI 42010) with the med adherence data stored here. |
| 4 | `OUTCOME_MED_NAME` | VARCHAR |  | The medication name relevant to an adherence measure. |
| 5 | `OUTCOME_MED_NDC_ID` | VARCHAR |  | The NDC record ID for the medication listed. |
| 6 | `OUTCOME_MED_NDC_ID_NDC_CODE` | VARCHAR |  | The external code for the National Drug Code (NDC). An NDC represents packages of medications. |
| 7 | `OUTCOME_MED_FIRST_FILL_DATE` | DATETIME |  | The date this medication was first filled. |
| 8 | `OUTCOME_MED_LAST_FILL_DATE` | DATETIME |  | The most recent fill date for the medication. |
| 9 | `OUTCOME_MED_NEXT_FILL_DATE` | DATETIME |  | The expected next fill date for the medication. This is based on last fill date + days supplied. |
| 10 | `OUTCOME_MED_DAYS_SUPPLY` | INTEGER |  | The number of days that the latest medication fill should last if taken as prescribed. |
| 11 | `OUTCOME_MED_ELIG_EXT_DAY_SUP_C_NAME` | VARCHAR | org | Whether the patient is eligible for a larger medication supply. |
| 12 | `OUTCOME_MED_REFILLS_REMAINING` | INTEGER |  | The number of refills a patient can obtain before their provider must authorize more. |
| 13 | `OUTCOME_MED_PRESCRIBER_NAME` | VARCHAR |  | The name of the provider who prescribed the medication. |
| 14 | `OUTCOME_MED_PRESCRIBER_NPI` | VARCHAR |  | The National Provider Identifier (NPI) of the provider who prescribed the medication. |
| 15 | `OUTCOME_MED_PRESCRIBER_PHONE` | VARCHAR |  | The phone number of the provider who prescribed the medication. |
| 16 | `OUTCOME_MED_PHARMACY_NAME` | VARCHAR |  | The name of the pharmacy where the patient obtained the medication. |
| 17 | `OUTCOME_MED_PHARMACY_NPI` | VARCHAR |  | The National Provider Identifier (NPI) of the pharmacy where the patient obtained the medication. |
| 18 | `OUTCOME_MED_PHARMACY_PHONE` | VARCHAR |  | The phone number of the pharmacy where the patient obtained the medication. |
| 19 | `OUTCOME_MED_PHARMACY_SRC_C_NAME` | VARCHAR | org | The method of distribution used by the pharmacy where the patient obtained the medication. |
| 20 | `OUTCOME_MED_PREF_PHARMACY_YN` | VARCHAR |  | Whether the pharmacy where the patient obtained the medication is a preferred pharmacy for the payer. Patients often have lower out-of-pocket costs at preferred pharmacies. |
| 21 | `OUTCOME_MED_IS_REVERSED_YN` | VARCHAR |  | Whether the medication on this line is reversed - meaning it was not picked up by the patient. This is a calculation by comparing the "most recent medication" on historical contacts to those on subsequent contacts to determine if a specific medication has been reversed. |
| 22 | `OUTCOME_MED_RAW_NDC` | VARCHAR |  | The raw NDC string for the medication associated with the gap. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

