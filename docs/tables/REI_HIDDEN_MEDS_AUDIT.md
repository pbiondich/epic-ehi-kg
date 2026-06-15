# REI_HIDDEN_MEDS_AUDIT

> This table lists changes to the medications that have been hidden or unhidden in the Stimulation Summary activity. When users hide or unhide medications, a line is added along with who made the change and the exact instant.

**Primary key:** `CYCLE_ID`, `LINE`  
**Columns:** 13  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CYCLE_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the cycle record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HIDDEN_AUDIT_PAT_ID` | VARCHAR | FK→ | Stores the patient record ID for the patient that has a medication hidden/unhidden (Multiple patients can be linked to a single cycle record). |
| 4 | `HIDDEN_AUDIT_MED_PRBLM_LIST_ID` | NUMERIC |  | Stores the ID for the simple generic form of the hidden/unhidden medication. |
| 5 | `HIDDEN_AUDIT_DISP_QTYUNIT_C_NAME` | VARCHAR | org | Stores the units of the hidden/unhidden medication. |
| 6 | `HIDDEN_AUDIT_FREQ_ID` | VARCHAR |  | Stores the frequency ID of the hidden/unhidden medication. |
| 7 | `HIDDEN_AUDIT_FREQ_ID_FREQ_NAME` | VARCHAR |  | The name of the frequency record. |
| 8 | `HIDDEN_AUDIT_MED_ROUTE_C_NAME` | VARCHAR | org | Stores the route of the hidden/unhidden medication. |
| 9 | `HIDDEN_AUDIT_MEDICATION_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 10 | `HIDDEN_AUDIT_USER_ID` | VARCHAR |  | Stores the user ID that hid/unhid the medication. |
| 11 | `HIDDEN_AUDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 12 | `HIDDEN_AUDIT_INST_UTC_DTTM` | DATETIME (UTC) |  | The instant in which the medication was hidden/unhidden. |
| 13 | `HIDDEN_AUDIT_STATUS_YN` | VARCHAR |  | Status of whether or not the medication is hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CYCLE_ID` | [INFERTILITY_CYCLE](INFERTILITY_CYCLE.md) | sole_pk | high |
| `HIDDEN_AUDIT_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |

