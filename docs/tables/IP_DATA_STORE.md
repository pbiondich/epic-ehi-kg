# IP_DATA_STORE

> This table contains generic information related to a patient's inpatient stay, including data on patient education, notes, and other topics.

**Primary key:** `INPATIENT_DATA_ID`  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INPATIENT_DATA_ID` | VARCHAR | PK shared | The unique ID of the inpatient data store record. |
| 2 | `TEMPLATE_ID` | VARCHAR | shared | The unique ID of the flowsheet template. |
| 3 | `TEMPLATE_ID_DISPLAY_NAME` | VARCHAR |  | The display name associated with this template. |
| 4 | `DISCH_INST_HNO_ID` | VARCHAR |  | The HNO ID of the patient's discharge instructions, for discharge instructions created in version Epic Aug 2021 or prior. In version Epic Nov 2021 and later, the discharge instruction information that was previously stored in INP will now be stored in HNO for Note Type 18-Discharge Instructions, with information about instances where discharge instructions were reviewed, updated, or signed extracted in the Clarity table DISCH_INSTR_HISTORY. |
| 5 | `RECORD_STATUS_C_NAME` | VARCHAR |  | The current status of the Inpatient Data record: active or resolved. |
| 6 | `EPT_CSN` | NUMERIC |  | Link to Contact Serial Number in EPT for associated encounter. |
| 7 | `BRST_STAT_INST_TM` | DATETIME (Local) |  | Stores the last instant that Breastfeeding Status was saved. |
| 8 | `PAIN_EDU_INST_TM` | DATETIME (Local) |  | Stores the last instant the Pain Education was saved. |
| 9 | `HC_INSTANT_TM` | DATETIME (Local) |  | Stores the last instant that the Head Circumference was saved. |
| 10 | `PF_INSTANT_TM` | DATETIME (Local) |  | Stores the last instant that Peak Flow was saved. |
| 11 | `EXINGC_INSTANT_TM` | DATETIME (Local) |  | Stores the last instant that Exclude in Growth Charts information was saved. |
| 12 | `ALT_PRINT_INST_TM` | DATETIME (Local) |  | Stores the last instant OurPractice Advisory (OPA) alert information was saved. |
| 13 | `IP_NOTE_MOD_INST_TM` | DATETIME (UTC) |  | The time the Notes were last modified for this Inpatient Data record. |
| 14 | `UPDATE_DATE` | DATETIME (Local) |  | The date and time this row was last updated (the last time it was extracted or this column was backfilled). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

