# ENROLL_LINKED_CSN2

> The ENROLL_LINKED_CSN2 table identifies encounters, using Contact Serial Numbers (CSN), linked to a patient's enrollment in a research study. Unlike ENROLL_LINKED_REPL, this table includes any associated protocols, day numbers, treatment plans, and treatment days with the CSN as well. The ENROLL_LINKED_CSN view should be used instead of directly linking to this table. The actual data used by this view may be split between the ENROLL_LINKED_REPL or the ENROLL_LINKED_CSN2 tables. The ENROLL_LINKED_CSN view combines the data from both tables regardless of how the underlying data may be shifting between the two tables.

**Primary key:** `ENROLL_ID`, `LINE`  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ENROLL_ID` | NUMERIC | PK FK→ | The unique ID of the patient enrollment record for this row. This column is frequently used to link to the ENROLL_INFO table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PAT_CSN` | NUMERIC | FK→ | The unique contact serial number (CSN) for patient encounters linked to this enrollment. These numbers are unique across all patient encounters in your system. If you use IntraConnect this is the Unique Contact Identifier (UCI). |
| 4 | `PROTOCOL_CSN` | NUMERIC |  | The unique contact serial number (CSN) for protocols linked to this encounter. These numbers are unique across all protocol contacts in your system. If you use IntraConnect this is the Unique Contact Identifier (UCI). |
| 5 | `LINKED_UNIQ_DAY_NUM` | INTEGER |  | The timeline day ID for the timeline instantiation of a protocol. Once a protocol is assigned to a patient, any repeating cycles and treatment days defined in the protocol are expanded out into individual cycles and cycles in the timeline. This day ID is a unique value for the protocol contact serial number (CSN) assigned to the timeline and can be linked back to the original protocol through the CL_PRL_DAY_MAP table. |
| 6 | `TREATMENT_PLAN_CSN` | NUMERIC |  | The clinical treatment plan linked to the encounter. |
| 7 | `TREATMENT_DAY_CSN` | NUMERIC |  | The clinical treatment day linked to the encounter. This column may be linked to TRG_UPDATE_INFO.CONTACT_SERIAL_NUM. |
| 8 | `LINK_ENCOUNTER_USER_ID` | VARCHAR |  | The user who linked or unlinked an encounter to a study. |
| 9 | `LINK_ENCOUNTER_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 10 | `LINK_ENCOUNTER_DTTM` | DATETIME (UTC) |  | UTC formatted instant when user links or unlinks an encounter to a study. |
| 11 | `TREATMENT_DAY_LINE` | INTEGER |  | The line number of the treatment day in the treatment plan that this encounter is linked to. |
| 12 | `LINK_ENC_SOURCE_C_NAME` | VARCHAR |  | Contains how this encounter got linked to this enrollment. Blank is an unspecified process (before the data was collected) |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ENROLL_ID` | [ENROLL_INFO](ENROLL_INFO.md) | sole_pk | high |
| `PAT_CSN` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

