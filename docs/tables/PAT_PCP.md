# PAT_PCP

> This table contains the Primary Care Provider (PCP) information for your patients over time. It can also contain data about providers that are not PCPs but are still on the patients' EpicCare-Ambulatory care teams.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 18  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PCP_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 4 | `EFF_DATE` | DATETIME |  | The date from which the provider is in effect as the member’s PCP. |
| 5 | `TERM_DATE` | DATETIME |  | The last date for which the provider was the member’s PCP. |
| 6 | `PCP_TYPE_C_NAME` | VARCHAR | org | The category value associated with the type of the PCP. This is only populated when the provider is a patient's PCP and is null otherwise. |
| 7 | `SPECIALTY_C_NAME` | VARCHAR | org | The specialty category ID for the patient care team member. |
| 8 | `RESULTS_C_NAME` | VARCHAR |  | The results to receive category ID for the patient care team member. |
| 9 | `PCP_MESSAGE_YN` | VARCHAR |  | Indicates whether a provider on a patient's care team wishes to be included as a recipient of messages sent to the patient's PCP. A “Y” indicates that the provider wishes to receive messages, a “N” indicates that the provider does not wish to receive the messages. |
| 10 | `RELATIONSHIP_C_NAME` | VARCHAR | org | The relationship to patient category ID for the patient care team member. |
| 11 | `OTHER_NAME` | VARCHAR |  | The name for patient care team members that don't have a provider and resource record. |
| 12 | `OTHER_ADDRESS` | VARCHAR |  | The address for patient care team members that don't have a provider and resource record. Lines are delimited with character 9s. |
| 13 | `OTHER_PHONE` | VARCHAR |  | The phone number for patient care team members that don't have a provider and resource record. |
| 14 | `OTHER_PAGER` | VARCHAR |  | The pager number for patient care team members that don't have a provider and resource record. |
| 15 | `OTHER_FAX` | VARCHAR |  | The fax number for patient care team members that don't have a provider and resource record. |
| 16 | `OTHER_EMAIL` | VARCHAR |  | The email address for patient care team members that don't have a provider and resource record. |
| 17 | `PCP_HX_COMMENTS` | VARCHAR |  | Free text comments that can be entered for a provider that is part of the care team for this patient. |
| 18 | `PCP_ADDRESS_ID` | VARCHAR |  | The unique ID of the address in the provider record that should be used to contact the patient's PCP. This column is frequently used in conjunction with the PCP_PROV_ID column to link to the CLARITY_SER_ADDR table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

